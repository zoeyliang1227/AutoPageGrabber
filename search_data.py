import os
import re
import time

from datetime import datetime
from bs4 import BeautifulSoup

timestamp = datetime.now().strftime("%Y%m%d")
screenshot_root = os.path.join(os.getcwd(), f"{timestamp}_screenshot")

def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def search_data_from_html(page, html, item, target_item):
    soup = BeautifulSoup(html, "html.parser")
    step_list = soup.find("div", class_="step-list")
    get_mobile_name = re.search(r"mobile_name:\s*(\S+)", page.locator("#step-right").inner_text())
    if get_mobile_name:
        mobile_name = get_mobile_name.group(1)
        # print(f"mobile_name = {mobile_name}")

    for step in step_list:
        index = step.get("index")
        text = step.text.strip()
        # print(f"index: {index}, 內容: {text}")
        if index == '3' and '4[log]Ip Address' in text:
            screenshot(page, index, text, 'inet 10.0.0.', mobile_name, item, target_item)

        elif index == '4' and '5[log]SSID' in text:
            screenshot(page, index, text, 'SSID: ', mobile_name, item, target_item)
        
        elif index == '6' and '7[log]Ping Test' in text:
            screenshot(page, index, text, 'PING 8.8.8.8 (8.8.8.8)', mobile_name, item, target_item)

        elif index == '8' and '9[log]Ping Test' in text:
            screenshot(page, index, text, 'PING www.google.com', mobile_name, item, target_item)
        

            # print(f"-"*32)
            break

def screenshot(page, index, text, keyword, mobile_name, item, target_item):
    page.locator('div.step[index="'+str(index)+'"]').click()
    ping_test_2 = page.locator("#step-right")
    if keyword in ping_test_2.inner_text():
        ensure_folder(screenshot_root)
        folder = re.match(r"^(#\s*\d+\[log\].*?)(\d+s\s+\d+ms)?$", text)
        if folder:
            folder_name = f"{folder.group(1)}"
        folder_path = os.path.join(screenshot_root, folder_name)
        ensure_folder(folder_path)
        if target_item and item == target_item:
            page.screenshot(path=f"{folder_path}/{item}/{mobile_name}.png")
            print(f"處理 {mobile_name} index={index} {item} → {folder_name}")


# if __name__ == "__main__":
#     extract_data_from_html()