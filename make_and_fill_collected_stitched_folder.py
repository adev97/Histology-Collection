from pathlib import Path
import shutil

HISTOLOGY = Path(
    r"R:\Basic_Sciences\Phys\SenzaiLab\Aparna\Data_by_mouse\m002\histology"
)
DESTINATION = HISTOLOGY / "collected_stitched"


def find_stitched_folders(parent):
    """Find stitched folders without searching inside matched folders."""
    for folder in sorted(parent.iterdir()):
        if not folder.is_dir() or folder == DESTINATION:
            continue

        if folder.name.lower().endswith("-stitched"):
            yield folder
        else:
            yield from find_stitched_folders(folder)


def main():
    if not HISTOLOGY.is_dir():
        raise FileNotFoundError(f"Histology folder not found: {HISTOLOGY}")

    # Prevent accidental merging or overwriting on subsequent runs.
    if DESTINATION.exists():
        raise FileExistsError(
            f"Destination already exists: {DESTINATION}\n"
            "Choose a different destination name before running again."
        )

    stitched_folders = []

    for group in sorted(HISTOLOGY.iterdir()):
        if not group.is_dir() or group == DESTINATION:
            continue

        for stitched in find_stitched_folders(group):
            relative_path = stitched.relative_to(HISTOLOGY)
            file_count = sum(
                1 for item in stitched.rglob("*") if item.is_file()
            )
            stitched_folders.append((stitched, relative_path, file_count))

    if not stitched_folders:
        print("No folders ending in '-stitched' were found.")
        return

    print(f"{'Folder (relative to histology)':<90} {'Files':>8}")
    print("-" * 100)

    for _, relative_path, file_count in stitched_folders:
        print(f"{str(relative_path):<90} {file_count:>8}")

    print(f"\nFound {len(stitched_folders)} stitched folders.")

    DESTINATION.mkdir()

    for source, relative_path, _ in stitched_folders:
        target = DESTINATION / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        print(f"Copying: {relative_path}")
        shutil.copytree(source, target)

    print(f"\nFinished. Copies saved to:\n{DESTINATION}")


if __name__ == "__main__":
    main()