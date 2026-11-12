import os
import shutil
import subprocess

# Change this path to wherever you want your game log stored
LOG_FILE = os.path.expanduser("~/Documents/completed_games.txt")


def main():
    print("--- Log a Completed Game ---")
    game = input("Game Title: ").strip()
    console = input("Console Played On: ").strip()
    year = input("Year Completed: ").strip()

    if not game or not console or not year:
        print("All fields are required. Entry canceled.")
        return

    entry = f"{game} | {console} | {year}\n"

    # Create the file with a header if it doesn't exist yet
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        if not file_exists:
            f.write("Game Title | Console | Year Completed\n")
            f.write("-" * 45 + "\n")
        f.write(entry)

    print(f"\nSaved to {LOG_FILE}!")
    open_in_sublime(LOG_FILE)


def open_in_sublime(filepath):
    # Check if the 'subl' command line tool is available in PATH
    if shutil.which("subl"):
        subprocess.run(["subl", filepath])
        return

    # Fallback paths for standard installations if 'subl' isn't in PATH
    common_paths = [
        "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl",  # macOS
        r"C:\Program Files\Sublime Text\subl.exe",  # Windows
        r"C:\Program Files\Sublime Text 3\subl.exe",  # Windows (ST3)
        "/usr/bin/subl",  # Linux
    ]

    for path in common_paths:
        if os.path.exists(path):
            subprocess.run([path, filepath])
            return

    print(
        "Note: Could not launch Sublime Text automatically. Open the file"
        " manually or add 'subl' to your system PATH."
    )


if __name__ == "__main__":
    main()
