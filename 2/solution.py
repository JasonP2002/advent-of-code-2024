INPUT = "input.txt"
COLUMNS = 1000

inputs = []

def init_input():
    f = open(INPUT, "r")
    temp = f.read().split("\n")
    for x in temp:
        inputs.append(x.split(" "))
    f.close()

def test_safety(x):
    valid = True
    asc = False
    desc = False
    for i in range(1, len(x)):
            prevNum = int(x[i-1])
            currentNum = int(x[i])

            if (prevNum + 1 <= currentNum <= prevNum + 3):
                asc = True
            elif (prevNum - 3 <= currentNum <= prevNum - 1):
                desc = True
            else:
                valid = False
                break

            if (asc == True & desc == True):
                valid = False
    return valid

def analyse_data_part_one():
    safe = 0
    for x in inputs:
        if (test_safety(x) == True):
            safe += 1
    return safe

def problem_dampener():
    safe = 0
    for x in inputs:
    
        if (test_safety(x) == True):
            safe += 1
        else:

            # If reading (current line of input) is not safe,
            # test it again after removing one of it's elements, for all of it's elements
            for i in range(0, len(x)):

                change = x.copy()
                change.pop(i)
                if (test_safety(change) == True):
                    safe += 1
                    break

    return safe

init_input()
print("Safe: " + str(analyse_data_part_one())) # PART ONE
print("Safe with Problem Dampener: " + str(problem_dampener())) # PART TWO
