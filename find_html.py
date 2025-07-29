import os

from pathlib import Path

html_files = {}

def find_html_files():
    for month in Path(os.getcwd()).iterdir():
        if month.is_dir() and month.name.startswith('2025'):    # is_dir判斷是否為資料夾
            for items in month.iterdir():
                if items.is_dir() and items.name.endswith('_Test'):
                    item = str(items).rstrip("\\").split("\\")[-1]
                    if item not in html_files:
                        html_files[item] = {}

                    for mobile in items.iterdir():
                        if mobile.is_dir():
                            for file in mobile.glob('*.html'):
                                html_files[item][mobile.name] = str(file)

    # print(html_files)

    return html_files


if __name__ == '__main__':
    find_html_files()