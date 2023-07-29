import pathlib

USERPROFILE = pathlib.Path("C:\\Users\\Damien")

FROM = [
    USERPROFILE / "Downloads",
    USERPROFILE / "Desktop",
]

TO = {
    # audio
    "mp3": USERPROFILE / "Music",
    "flac": USERPROFILE / "Music",
    # image
    "jpg": USERPROFILE / "Drawing" / "Photo_ref",
    "png": USERPROFILE / "Drawing" / "Photo_ref",
    # video
    "mp4": USERPROFILE / "Downloads" / "Film",
    "mkv": USERPROFILE / "Downloads" / "Film",
    # torrent
    "torrent": USERPROFILE / "Downloads" / "Torrent",
}


def move_file(old, new, file):
    try:
        (old / file).replace(new / file)
        print(f"Moved {file}")
        print(f"From  {old}")
        print(f"To    {new}")
        print()

    except PermissionError:
        pass


def main():
    for old_folder in FROM:
        for file in filter(lambda x: x.is_file(), old_folder.iterdir()):
            file_extension = file.name.lower().split(".")[-1]
            if file_extension in TO.keys():
                move_file(old_folder, TO[file_extension], file.name)


if __name__ == "__main__":
    main()
