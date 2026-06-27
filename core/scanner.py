import os

def get_python_files(root="."):
    py_files = []
    for root, _, files in os.walk(root):
        for file in files:
            if file.endswith(".py") and "__pycache__" not in root:
                py_files.append(os.path.join(root, file))
    return py_files