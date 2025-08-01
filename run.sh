#!/bin/bash
 
# 執行 Robot Framework 測試
python robot_test.py
    # --testlevelsplit 把「每一個 test case」都視為一個獨立單位
    # --outputdir results 執行結果輸出到 results/ 資料夾
pabot --processes 4 --testlevelsplit --outputdir results mobile.robot   
python data_processing.py

if [ $? -eq 0 ]; then
    echo 'Python script data_processing.py executed successfully.'
    echo 'Robot Framework results are available, check xlsx.'

else
    echo 'Python script data_processing.py encountered an error.'
    
fi


 