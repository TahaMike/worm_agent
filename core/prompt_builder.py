def build_prompt(user_prompt, target_code, context):
    return f"""
        You are a senior software engineer working on a real production codebase.
        
        TASK:
        {user_prompt}
        
        TARGET FILE:
        {target_code}
        
        PROJECT CONTEXT:
        {context}
        
        STRICT RULES:
        - Return ONLY updated version of TARGET FILE
        - Do NOT explain anything
        - Do NOT include ``` or markdown
        - Keep imports correct
        - Do not break existing functionality unless fixing a bug
        - Do NOT include explanations
        - Do NOT include comments
        - Return ONLY raw Python code
        
        """