import csv
import re

"""
Given a CSV file, write a function that will open this file, validate the data and output a new file (good_data.csv).
"""
GOOD_DATA_FILE_NAME = "good_data.csv"


def validate_and_load_files(file_name):
    """
    Given a file name
    Open and validate this file based on the requirements given (see "Column validation" in part_one.txt)
    Save the good data to a new file
    """
    csvdata = readsheet(file_name)
    newsheet = list()
    newsheet.append(csvdata.pop(0))
    valid_data = validate_data(csvdata)
    newsheet.extend(valid_data)
    write_csv(newsheet)
        

def readsheet(file_name):
    with open(file_name, encoding='utf8') as csvfile:
        csvhandler = csv.reader(csvfile, delimiter=',')
        data = list()
        linecount = 0
        for row in csvhandler:
            data.append(row)
        csvfile.close()
    return data

def write_csv(newcsv):
    with open (GOOD_DATA_FILE_NAME, 'w+', newline ='', encoding='utf8') as new_csv:
        write = csv.writer(new_csv)
        write.writerows(newcsv)
    new_csv.close()

def validate_data(csv_list):
    vdata = list()
    for row in csv_list:
        check = list()
        for c in range(len(row) - 1):
            # The logic I applied here is a bit ham-fisted, verbose,
            # and inelegant (and not very DRY). It works in test?
            if c == 0:
                if not row[c].isdigit() or row[c] == '':
                    check.append(False)
                else:
                    check.append(True)
            if c == 1:
                if not isinstance(row[c], str):
                    check.append(False)
                else:
                    check.append(True)
            if c == 2:
                if not isinstance(row[c], str):
                    check.append(False)
                else:
                    check.append(True)
            if c == 3:
                if not validate_email(row[c]) or row[c] == '':
                    check.append(False)
                else:
                    check.append(True)
            if c == 4:
                # Gender is not specifically called out in project
                # brief. As this is an evolving concept that I lack
                # detailed knowledge of, I chose to treat it as 
                # string-only.
                if not isinstance(row[c], str):
                    check.append(False)
                else:
                    check.append(True)
            if c == 5:
                if not validate_eircode(row[c]) or row[c] == '':
                    check.append(False)
                else:
                    check.append(True)
        if all(check) == True:
            vdata.append(row)
    return vdata

def validate_email(email):
    # Added additional values to check lengths of email address
    # and domain and username substrings.
    parts = email.split("@")
    if len(email) > 320 or len(parts[0]) > 64 or len(parts[1]) > 255:
        return False
    rex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(rex, email):
        return True
    else:
        return False

def validate_eircode(eircode):
    # A Whitespace should generally be allowed for Eircode, which would
    # allow a str length of 7 or 8 and regex to allow a ' ' if present.
    # I did not implement this.
    if len(eircode) != 7:
        return False
    rex = r'[A-Z]{1}[0-9]{1}[W0-9]{1}[A-Z0-9]{4}'
    if re.fullmatch(rex, eircode):
        return True
    else:
        return False

if __name__ == "__main__":
    file_name = "mock_data_1000.csv"
    validate_and_load_files(file_name)
