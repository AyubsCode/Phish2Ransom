import os
from datetime import datetime


TARGET_EXTENSIONS = (
    '.doc', '.docx',
    '.pdf',
    '.xls', '.xlsx',
    '.ppt', '.pptx'
)

USER_HOME = os.environ.get("USERPROFILE")


TARGET_FOLDERS = [
    os.path.join(USER_HOME, "Documents"),
    os.path.join(USER_HOME, "Downloads"),
    os.path.join(USER_HOME, "Pictures"),
    os.path.join(USER_HOME, "Videos")
]


REPORT_FILE = "important_files_report.txt"


def scan_files():
    found_files = []

    for folder in TARGET_FOLDERS:
        if not os.path.exists(folder):
            continue

        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(TARGET_EXTENSIONS):
                    full_path = os.path.join(root, file)
                    stats = os.stat(full_path)

                    found_files.append({
                        "name": file,
                        "path": full_path,
                        "size_kb": stats.st_size // 1024,
                        "modified": datetime.fromtimestamp(stats.st_mtime)
                    })

    return found_files


def write_report(files):
    with open(REPORT_FILE, "w", encoding="utf-8") as f:

        for file in files:
            f.write(f"File Name   : {file['name']}\n")
            f.write(f"Path        : {file['path']}\n")
            f.write("-" * 50 + "\n")

    print(f"[+] Report saved to {REPORT_FILE}")


if __name__ == "__main__":
    results = scan_files()
    write_report(results)
    print(f"[+] Total files found: {len(results)}")
