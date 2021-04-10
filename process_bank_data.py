"""
Input: All the collected input csv files should be inside ./data/ folder
Output: Transformed data of Integrated multiple Banks Transaction files
Config: Currently configured the only for 3 different kinds of Bank Csv attributes.
Maintainability: For integrating new Bank's data one must analyse the data and must extend the configuration
"""

import csv
import json
from os import listdir
from datetime import datetime

def main():
    """ The main starts from here """
    mypath = "data/"
    print(f"All files in {mypath} folders are" , listdir(mypath))

    all_files_list = []
    for filename in listdir(mypath):
        file = mypath + filename
        # with open(file, newline="") as csvfile:
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            print("#"*50)
            print(f"{file}".center(50))
            print("#"*50)
            print(f"Before Processing".center(30, "-"))
            each_file_list = ProcessCsv(reader)
            all_files_list.extend(each_file_list)
            print(f"After Processing".center(30, "-"))
            print("\n".join([json.dumps(item) for item in each_file_list]))
            print()
    print("The formatted collective data as below")
    print("\n".join([json.dumps(item) for item in all_files_list]))
    first_row = all_files_list[0]
    desired_headers = list(first_row.keys())
    # desired_headers = ['date', 'transaction', 'from', 'to', 'amount']
    json_to_csv(all_files_list, desired_headers)


def ProcessCsv(reader):
    """ Accepts csv.DictReader as input and return transformed data """
    each_file_list = []
    for row in reader:
        print(row)
        new_dict = {}
        for key, val in uniform_attr_names.items():
            if key == "amount":
                for item in val:
                    if isinstance(item, list) and all([ei in row for ei in item]):
                        new_dict[key] = ".".join([row[i] for i in item])
                    elif item in row:
                        new_dict[key] = row[item]
                        break
                assert new_dict[key]
                continue
            for item in val:
                if item in row:
                    if key == "date":
                        new_dict[key] = datetime.strptime(row[item], val[item]).strftime("%Y-%b-%d")
                        break
                    else:
                        new_dict[key] = row[item]
        each_file_list.append(new_dict)
    return each_file_list


def json_to_csv(all_records: list, desired_headers : list):
    f = csv.writer(open("test.csv", "w+", newline=''))

    # Write CSV Header, If you dont need that, remove this line
    f.writerow(desired_headers)

    for x in all_records:
        f.writerow([x[header] for header in desired_headers])

if __name__ == "__main__":
    uniform_attr_names = {
        "date": {
            "date": "%d-%m-%Y",
            "timestamp": "%b %d %Y",
            "date_readable": "%d %b %Y"
        },
        "transaction": ["type", "transaction"],
        "amount": ["amount", "amounts", ["euro", "cents"]],
        "from": ["from"],
        "to": ["to"]
    }
    main()