># Windows

## Description
- Use **playwright** and **beautifulsoup4** to create a `.html` page
- Extract the necessary data and integrate it into `Excel`
- Integrate reports using **Robot Framework**

## Install

- Install Python 3.11
- pip install --user pipenv
- python -m pipenv sync
- python -m pipenv shell

## Run
- main.py > Main program
- robot_file.py > Create .robot
- test.robot > Run the robot
- ./run.sh > Run the robot and data_processing.py

<!-- pyinstaller -F <python file>   # 打包成單執行檔，適合小檔
pyinstaller -D <python file>   # 打包成多個文件，適合框架類程式 -->
