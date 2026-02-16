from __future__ import annotations

from pathlib import Path
from collections import Counter


def create_tmp_dir(base: Path) -> Path:
    tmp_dir = base / "tmp"

    #vorher prüfen
    if not tmp_dir.exists():
        tmp_dir.mkdir()
    else:
        # wenn da nix tun 
        pass

    return tmp_dir


def create_tmp_dir_try(base: Path) -> Path:
 
    tmp_dir = base / "tmp"

    try:
        tmp_dir.mkdir()
    except FileExistsError:
        pass
    return tmp_dir


def create_files(tmp_dir: Path) -> list[Path]:
    filenames = ["test.txt", "file.txt", "README.md", "random.py"]
    paths = []
    for name in filenames:
        p = tmp_dir / name
        p.write_text(f"This is {name}\n", encoding="utf-8")
        paths.append(p)
    return paths


def count_file_endings(tmp_dir: Path) -> Counter:
    # nur Dateien zählen
    endings = [p.suffix for p in tmp_dir.iterdir() if p.is_file()]
    return Counter(endings)


def last_modified_file(tmp_dir: Path) -> Path | None:
    files = [p for p in tmp_dir.iterdir() if p.is_file()]
    if not files:
        return None
    # max nach mtime
    return max(files, key=lambda p: p.stat().st_mtime)


def cleanup(tmp_dir: Path) -> None:
    for p in tmp_dir.iterdir():
        if p.is_file():
            p.unlink()
    tmp_dir.rmdir()



def main() -> None:
    base = Path.cwd()  
    tmp_dir = create_tmp_dir(base)

    print("tmp dir:", tmp_dir)

    created = create_files(tmp_dir)
    print("created files:", [p.name for p in created])

    c = count_file_endings(tmp_dir)
    print("Counter:", c)  # z.B. Counter({'.txt': 2, '.md': 1, '.py': 1})

    last = last_modified_file(tmp_dir)
    print("last modified:", last.name if last else None)

    cleanup(tmp_dir)
    print("cleanup done. tmp exists?", tmp_dir.exists())


if __name__ == "__main__":
    main()
