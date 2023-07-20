import os
import pathlib

USERPROFILE = pathlib.Path("C:\\Users\\Damien")

PATH_AND_EXTENSION = {
    USERPROFILE / "Music": ["mp3", "flac"],
    USERPROFILE / "Drawing" / "Photo_ref": ["jpg", "png"],
    USERPROFILE / "Downloads" / "Film": ["mp4", "mkv"],
    USERPROFILE / "Downloads" / "Torrent": ["torrent"],
}

PATH_TO_CHECK = [
    USERPROFILE / "Downloads",
    USERPROFILE / "Desktop",
]

count = 0
for current_path in PATH_TO_CHECK:
    for file in os.listdir(current_path):
        for target_path, extensions in PATH_AND_EXTENSION.items():
            try:
                if file.lower().split(".")[-1] in extensions:
                    (current_path / file).replace(target_path / file)
                    count += 1
            except PermissionError:
                continue

print(f"In total {count} file were moved")
