# Write your solution here
from datetime import datetime, timedelta


def record_user_time(filename: str):
    date_str = input("Starting date: ")
    date_start = datetime.strptime(date_str, "%d.%m.%Y")
    days = int(input("How many days: "))

    print("Please type in screen time in minutes on each day (TV computer mobile):")
    with open(filename, "w") as f:
        for i in range(days):
            count_days = date_start + timedelta(days=i)
            formatted_date = count_days.strftime("%d.%m.%Y")
            screen_time = input(f"Screen time {formatted_date}: ")
            f.write(f"{formatted_date}: {screen_time}\n")
    print(f"Data stored in file {filename}")


def load_time_entries(filename: str):
    user_entries = {}

    with open(filename) as f:
        for line in f:
            line = line.strip()
            parts = line.split(":")
            min_part = parts[1].split()
            user_entries[parts[0]] = min_part

    for value in user_entries.values():
        for i in range(len(value)):
            value[i] = int(value[i])
        
    return user_entries


def update_time_summary(filename: str):
    user_entries = load_time_entries(filename)
    keys = list(user_entries.keys())
    values = list(user_entries.values())

    time_period = f"{keys[0]}-{keys[-1]}"
    tot_min = 0
    avg_min = 0

    for value in values:
        for i in range(len(value)):
            tot_min += value[i]
        avg_min = tot_min/len(keys)

    with open(filename, "w") as f:
        f.write(f"Time period: {time_period}\n")
        f.write(f"Total minutes: {tot_min}\n")
        f.write(f"Average minutes: {avg_min}\n")
        for key, value in user_entries.items():
            minutes = "/".join(str(n) for n in value)
            f.write(f"{key}: {minutes}\n")


def main():
    filename = input("Filename: ")
    record_user_time(filename)
    update_time_summary(filename)


main()