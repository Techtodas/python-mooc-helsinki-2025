# Write your solution here
import csv
from datetime import datetime, time, timedelta


def load_start_time(start_time: str):
    start_times = {}
    with open(start_time) as f:
        for line in csv.reader(f, delimiter=";"):
            time = datetime.strptime(line[1], "%H:%M")
            start_times[line[0]] = time

    return start_times


def load_submissions(submission: str):
    submissions = {}
    with open(submission) as f:
        for line in csv.reader(f, delimiter=";"):
            name = line[0]
            submission_data = line[1:]

            if name not in submissions:
                submissions[name] = []
            
            submissions[name].append(submission_data)

    return submissions


def cheaters():
    start_times = load_start_time("start_times.csv")
    submissions = load_submissions("submissions.csv")

    name_time_subs = {}
    for key, value in submissions.items():
        name_time_subs[key] = []
        for data in value:
            time = data[-1]
            name_time_subs[key].append(time)

    earliest_submission = {}
    for name, times in name_time_subs.items():
        earliest_time = max(times)
        earliest_submission[name] = earliest_time

    cheaters = []
    for name, submission_time in earliest_submission.items():
        t1 = start_times[name]
        t2 = datetime.strptime(submission_time, "%H:%M")
        diff = t2 - t1

        limit = timedelta(hours=3)
        if diff > limit:
            cheaters.append(name)


    return cheaters


def main():
    #print(load_start_time("start_times.csv"))
    #print(load_submissions("submissions.csv"))
    print(cheaters())

if __name__ == "__main__":
    main()