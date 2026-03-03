# Write your solution here
hourly_wage = float(input("Hourly wage:"))
hours_worked = float(input("Hours worked:"))
day = input("Day of the week:")

if day == "Sunday":
    hourly_wage*=2

rate = hourly_wage*hours_worked
print("Daily wages:", rate, "euros")