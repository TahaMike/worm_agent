# WORM Agent 🐛⚙️

A lightweight, terminal-based AI code agent powered by local LLMs (via Ollama) designed to analyze, refactor, and auto-fix Python code with minimal user interaction.

## 🚀 Intent

The goal of this project is to simulate a **local AI engineering assistant** that operates directly from the terminal—without a GUI—capable of understanding project context, rewriting code, and ensuring syntactic correctness automatically.

This project was built to:
- Strengthen QA + Automation engineering skills
- Explore AI-assisted code generation workflows
- Build a Cursor-like experience using fully local infrastructure
- Create a practical, resume-level system demonstrating real-world problem solving

---

## 🧠 Core Features

- **Prompt-driven code transformation**
  - Pass instructions via terminal
  - Works on single files or piped input

- **Project-wide context awareness**
  - Scans repository
  - Builds contextual understanding before generating output

- **Clean code extraction**
  - Filters model output
  - Removes markdown, explanations, and noise

- **AST-based validation**
  - Ensures generated Python code is syntactically valid
  - Prevents corrupt or broken file writes

- **Auto-retry self-healing loop**
  - Detects syntax errors
  - Sends feedback to model
  - Iteratively fixes code

- **Diff preview before applying changes**
  - Full transparency of modifications
  - User-controlled write operation

---

## ⚙️ Tech Stack

- Python
- Ollama (Local LLM runtime)
- DeepSeek-Coder (or similar coding models)
- AST (Abstract Syntax Tree validation)
- Custom modular architecture

---

## 📂 Project Structure
worm-agent/
├── worm.py # Entry point (CLI logic)
├── config.py # Configuration
├── core/
│ ├── scanner.py # Project file discovery
│ ├── context_builder.py # Context generation
│ ├── prompt_builder.py # Prompt engineering
│ ├── ollama_client.py # Model communication
│ └── diff_engine.py # Code diff visualization


---

## 🧪 Example Usage

```bash
worm conftest.py "optimize and clean code"



Or with piped input:

```bash
type file_name.<extension> | worm "refactor and improve structure"
---

🔒 Safety Mechanisms
Code is never written directly
All changes go through:
Extraction
Validation
Diff preview
Manual confirmation


🎯 Future Improvements
Runtime execution + error fixing loop
Pytest integration for auto-fixing failing tests
Multi-file refactoring intelligence
Semantic diff editing (partial updates instead of full rewrites)



📌 Summary

WORM Agent is an experimental step toward building a self-correcting AI development assistant that runs entirely locally, giving developers full control, transparency, and privacy.