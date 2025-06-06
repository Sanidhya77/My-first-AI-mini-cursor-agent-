def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except:
        return "Failed to read file."

from pathlib import Path

def write_file(path: str, content: str):
    full_path = Path(path)
    full_path.parent.mkdir(parents=True, exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Written to {path}"
