# Write your solution here
def filter_solutions():
    data = []
    correct = []
    incorrect = []

    with open("solutions.csv") as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            data.append(parts)
        
        for i in data:
            i[-1] = int(i[-1])
            if "-" in i[1]:
                i[1] = i[1].split("-")
                result = int(i[1][0]) - int(i[1][1])
                if result == i[-1]:
                    correct.append(f"{i[0]};{i[1][0]}-{i[1][1]};{i[2]}")
                else:
                    incorrect.append(f"{i[0]};{i[1][0]}-{i[1][1]};{i[2]}")
            elif "+" in i[1]:
                i[1] = i[1].split("+")
                i[1][0] = int(i[1][0])
                i[1][1] = int(i[1][1])
                result = int(i[1][0]) + int(i[1][1])
                if result == i[-1]:
                    correct.append(f"{i[0]};{i[1][0]}+{i[1][1]};{i[2]}")
                else:
                    incorrect.append(f"{i[0]};{i[1][0]}+{i[1][1]};{i[2]}")

        with open("correct.csv", "w") as correct_solution:
            for line in correct:
                correct_solution.write(line+"\n")
        
        with open("incorrect.csv", "w") as incorrect_solution:
            for line in incorrect:
                incorrect_solution.write(line+"\n")