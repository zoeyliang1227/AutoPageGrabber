import os

from pathlib import Path

def find_html_files():
    html_place=''
    html_files = {}
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".html"):
                # print(root, dirs, file)
                full_path = os.path.join(Path(root), file)
                html_place = Path(root)
                html_files[file]=html_place
                # print("找到 HTML 檔案：", full_path)
    
    # print(html_files)

    return html_place, html_files


if __name__ == "__main__":
    find_html_files()