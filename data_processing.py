
import os
import re
import pandas as pd

filename = "ConfirmPhone.xlsx"

def mobile_excel(file):
    check_mobile = {}
    mobile = re.sub(r'\.html$', '', file)
    check_mobile[mobile] = 0
    print(check_mobile)
    df = pd.DataFrame()
    df['mobile'] = list(check_mobile.keys())
    df['value'] = list(check_mobile.values())
    if os.path.exists(filename):
        df.to_excel(filename, index=False)
    else:
        df.to_excel(filename, index=False)


if __name__ == "__main__":
    find_html_files()