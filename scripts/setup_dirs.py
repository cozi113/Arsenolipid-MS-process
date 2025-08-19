from pathlib import Path

def make(root="."):
    root = Path(root)
    dirs = [
        "data/raw", "data/interim", "data/processed",
        "notebooks", "src", "docs/assets", ".github/workflows"
    ]
    for d in dirs:
        (root/d).mkdir(parents=True, exist_ok=True)
    # 占位文件
    for f in [
        "data/raw/.gitkeep", "data/interim/.gitkeep", "data/processed/.gitkeep",
        "notebooks/.gitkeep", "src/.gitkeep", "docs/assets/.gitkeep"
    ]:
        (root/f).touch(exist_ok=True)
    print(f"Created {len(dirs)} folders under {root.resolve()}")

if __name__ == "__main__":
    make(".")
