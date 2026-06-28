import difflib

def show_diff(old, new):
    diff = difflib.unified_diff(
        old.splitlines(),
        new.splitlines(),
        lineterm="",
        fromfile="original",
        tofile="updated"
    )

    diff_text = "\n".join(diff)
    print(diff_text)
    return diff_text