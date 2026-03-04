# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dates: list):
    year_list = []
    for date in dates:
        year_list.append(date.year)

    return sorted(year_list)