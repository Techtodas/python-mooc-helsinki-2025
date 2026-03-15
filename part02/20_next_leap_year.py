year = int(input("Year:"))
current_year = year
year += 1

while True:
    if year % 400 == 0:
        break
    elif year % 100 == 0:
        pass
    elif year % 4 == 0:
        break
    year+=1

print(f"The next leap year after {current_year} is {year}")