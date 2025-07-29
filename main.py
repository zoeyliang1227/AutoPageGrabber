import os
import re
import time

from datetime import datetime
from playwright.sync_api import sync_playwright

from find_html import find_html_files  
from search_data import search_data_from_html

timestamp = datetime.now().strftime("%Y%m%d")
screenshot_root = os.path.join(os.getcwd(), f"{timestamp}_screenshot")
html_files = find_html_files()

def extract_data_from_html():
    for file, path in html_files[1].items():
        # print(file, path)
        file_path = os.path.join(path, file)
        result = convert_web_page(file_path)
        # print(f"{file_path}：{result}")

def convert_web_page(file_path):
    html_path = os.path.abspath(file_path)
    url = "file://" + html_path  

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        html = page.content()
        search_data_from_html(page, html)

if __name__ == "__main__":
    extract_data_from_html()