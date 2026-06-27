import sys
import os
import re
import ast

from core.scanner import get_python_files
from core.context_builder import build_context
from core.prompt_builder import build_prompt
from core.ollama_client import query_ollama
from core.diff_engine import show_diff


def is_valid_python(code):
    try:
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)


def extract_code(response):
    if "```" in response:
        blocks = re.findall(r"```(?:python)?(.*?)```", response, re.DOTALL)
        if blocks:
            return blocks[-1].strip()
    return response.strip()


def retry_fix(user_prompt, broken_code, error_msg, context):
    retry_prompt = f"""
        You generated invalid Python code.
        
        ERROR:
        {error_msg}
        
        BROKEN CODE:
        {broken_code}
        
        PROJECT CONTEXT:
        {context}
        
        Fix it.
        
        STRICT RULES:
        - Output ONLY valid Python code
        - No markdown
        - No explanation
        - No comments
        """

    fixed = query_ollama(retry_prompt)
    return extract_code(fixed)[:20000]


def read_stdin():
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return None


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    if len(sys.argv) < 2:
        print("Usage:\n worm <file.py> \"prompt\"\n OR\n cat file.py | worm \"prompt\"")
        return

    user_prompt = sys.argv[-1]
    piped_code = read_stdin()

    if piped_code:
        print("[*] Using piped input")
        target_code = piped_code
        target_file = "piped_input.py"
    else:
        target_file = sys.argv[1]
        target_code = read_file(target_file)

    files = get_python_files()
    context = build_context(files, target_file)

    prompt = build_prompt(user_prompt, target_code, context)

    print("[*] Thinking...")
    raw_result = query_ollama(prompt)
    result = extract_code(raw_result)

    MAX_RETRIES = 3

    for attempt in range(MAX_RETRIES + 1):
        valid, error = is_valid_python(result)

        if valid:
            if attempt == 0:
                print("[✔] Code valid on first attempt")
            else:
                print(f"[✔] Auto-fix successful after {attempt} retry(s)")
            break

        print(f"[!] Attempt {attempt + 1}: Syntax error detected")
        print(f"    → {error}")

        if attempt == MAX_RETRIES:
            print("[✖] Failed after max retries. Aborting.")
            return

        result = retry_fix(user_prompt, result, error, context)

    print("\n--- DIFF ---\n")
    show_diff(target_code, result)

    choice = input("\nApply changes? (y/n): ").lower()

    if choice == "y" and not piped_code:
        write_file(target_file, result)
        print("[✔] File updated")
    else:
        print("[✖] Changes discarded")


if __name__ == "__main__":
    main()