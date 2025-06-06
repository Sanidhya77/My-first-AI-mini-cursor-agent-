import os

def create_project_structure(project_name: str, structure: dict, base_path: str = "."):
    def make_structure(structure_map, current_path):
        for name, value in structure_map.items():
            path = os.path.join(current_path, name)
            if isinstance(value, dict):
                os.makedirs(path, exist_ok=True)
                make_structure(value, path)
            else:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(value or "")  # write "" if value is None or empty

    root_path = os.path.join(base_path, project_name)
    os.makedirs(root_path, exist_ok=True)
    make_structure(structure, root_path)

    return f"✅ Project '{project_name}' created successfully at {root_path}"
