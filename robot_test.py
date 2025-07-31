from find_html import find_html_files

robot_filename="test.robot"

def robot_file():
    data = find_html_files()

    test_cases = []

    for item, mobile_dict in data.items():
        for mobile in mobile_dict.keys():
            test_name = f"{item}_{mobile}".replace(" ", "_")
            case = f"""{test_name}
    extract_data_from_html    {mobile}
"""
            test_cases.append(case)

    with open(robot_filename, "w", encoding="utf-8") as f:
        f.write("*** Settings ***\n")
        f.write("Library    main.py\n\n")
        f.write("*** Test Cases ***\n")
        f.write("\n".join(test_cases))

    print(f"✅ Robot test file generated: {robot_filename}")

if __name__ == "__main__":
    robot_file()
