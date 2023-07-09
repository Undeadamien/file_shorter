import os
import pathlib

PATH_AND_EXTENSION = {
    pathlib.Path("C:\\Users\\Damien\\Music"): ["mp3", "flac"],
    pathlib.Path("C:\\Users\\Damien\\Drawing\\Photo_ref"): ["jpg", "gif", "png"],
    pathlib.Path("C:\\Users\\Damien\\Downloads\\Film"): ["mp4", "mkv"],
    pathlib.Path("C:\\Users\\Damien\\Downloads\\Torrent"): ["torrent"],
}
PATH_TO_CHECK = [
    pathlib.Path("C:\\Users\\Damien\\Downloads"),
    pathlib.Path("C:\\Users\\Damien\\Desktop"),
]


for current_path in PATH_TO_CHECK:
    for file in os.listdir(current_path):
        for target_path, extensions in PATH_AND_EXTENSION.items():
            try:
                if file.lower().split(".")[-1] in extensions:
                    (current_path / file).replace(target_path / file)
            except PermissionError:
                continue
