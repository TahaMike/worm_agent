from assertix.config import MAX_CONTEXT_FILES

def build_context(files, exclude_file):
    context = ""
    count = 0

    for f in files:
        if f == exclude_file:
            continue

        try:
            with open(f, "r", encoding="utf-8") as file:
                content = file.read()[:2000]  # truncate
                context += f"\n# File: {f}\n{content}\n"
                count += 1
        except:
            continue

        if count >= MAX_CONTEXT_FILES:
            break

    return context