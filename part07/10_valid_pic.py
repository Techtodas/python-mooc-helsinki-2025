# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    # Allowed str for control character
    valid_str = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    # Assigning marker
    if "+" in pic:
        marker = "+"
    elif "-" in pic:
        marker = "-"
    elif "A" in pic:
        marker = "A"
    else:
        return False
            
    # PIC parts
    parts = pic.split(marker)
    day = int(parts[0][:2])
    month = int(parts[0][2:4])
    year = int(parts[0][-2:])
    control_char = parts[1][-1]

    if marker == "+":
        year+=1800
    elif marker == "-":
        year+=1900
    elif marker == "A":
        year+=2000

    try:
        valid_date_format = datetime(year, month, day)
        pid_num = int(parts[1][:-1])
    except ValueError:
        return False
    except ValueError:
        return False

    # Possition of the control character base on the computation.
    control_char_base = int(f"{day:02d}{month:02d}{year%100:02d}{pid_num:03d}")%31
    
    checker = True
    if not (control_char == valid_str[control_char_base]):
        checker = False

    return checker

if __name__ == "__main__":
    print(is_it_valid("230827-906F1"))