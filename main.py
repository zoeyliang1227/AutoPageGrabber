import os
import re
import time

from datetime import datetime
from playwright.sync_api import sync_playwright
from data_processing import mobile_excel

from find_html import find_html_files  
from search_data import search_data_from_html

timestamp = datetime.now().strftime("%Y%m%d")
screenshot_root = os.path.join(os.getcwd(), f"{timestamp}_screenshot")

def extract_data_from_html(target_mobile=None):
    for item, path_list in find_html_files().items():
        for mobile, path in path_list.items():
            if target_mobile and mobile != target_mobile:
                continue
            convert_web_page(mobile, str(path), item)
        
    mobile_excel()

def convert_web_page(mobile, file_path, item):
    html_path = os.path.abspath(file_path)
    url = "file://" + html_path  

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        html = page.content()
        search_data_from_html(page, html, item)

if __name__ == "__main__":
    extract_data_from_html()