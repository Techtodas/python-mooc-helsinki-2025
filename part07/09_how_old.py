# Write your solution here
from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if year <= 1999:
    age = datetime(1999, 12, 31) - datetime(year, month, day)
    print(f"You were {age.days} days old on the eve of the new millennium.")
else:
    print("   You weren't born yet on the eve of the new millennium.")
