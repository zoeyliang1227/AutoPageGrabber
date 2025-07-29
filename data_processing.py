
import os
import re
import pandas as pd

from pathlib import Path

filename = "ConfirmPhone.xlsx"

check_mobile = {}

def mobile_excel():    
    # 找 screenshot_folder
    screenshot_folders = [f for f in os.listdir(os.getcwd())
                      if os.path.isdir(os.path.join(os.getcwd(), f)) and "screenshot" in f.lower()]
    for screenshot in screenshot_folders:
        screenshot_path = os.path.join(os.getcwd(), screenshot)

    for folder in os.listdir(screenshot_path):
        print(screenshot_path)
        folder_path = os.path.join(screenshot_path, folder)

        if not os.path.isdir(folder_path):
            continue

        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            if not os.path.isdir(item_path):
                continue

            for file in os.listdir(item_path):
                mobile_name = os.path.splitext(file)[0]

                if folder not in check_mobile:
                    check_mobile[folder] = {}
                if item not in check_mobile[folder]:
                    check_mobile[folder][item] = {}

                if file.lower().endswith(".png"):
                    check_mobile[folder][item][mobile_name] = 1
                else:
                    check_mobile[folder][item][mobile_name] = 0

    # print(check_mobile)
    load_excel(item)

def load_excel(item):
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for folder, values in check_mobile.items():
            df = pd.DataFrame.from_dict(values, orient="index")
            df.index.name = "Mobile"
            df.fillna("", inplace=True)
            new_folder = re.sub(r"[\[\]]", "_", folder)
            df.to_excel(writer, index=True, sheet_name=new_folder)

    print(f"Excel 檔已建立：{filename}")


if __name__ == "__main__":
    mobile_excel()