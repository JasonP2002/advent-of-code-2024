import re

INPUT = "input.txt"

def calculate_sub_total(arr):
    subtotal = 0
    for x in arr:
        subtotal += int(x[0]) * int(x[1])
    return subtotal

def parse_part_one(line):
    # Matches format mul(X,Y), where X and Y are numbers with 1-3 digits
    regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    numbers = regex.findall(line)
    return calculate_sub_total(numbers)

def parse_part_two(input):
    total = 0
    REGEX_DONT = r'don\'t\(\)'
    REGEX_DO = r'do\(\)'
    # Split input by don't()
    clean = re.split(REGEX_DONT, input)

    # As mul() is enabled initially we add all mul() calls, prior to the first dont(), to our total
    total += parse_part_one(clean[0])
    for i in range (1, len(clean)):
        # If we have a do() call in our current line
        # (We do not want to add lines where dont() has been called prior to our total)
        if (re.search(REGEX_DO, clean[i]) != None):

            ## Split line by do()
            current = re.split(REGEX_DO, clean[i])

            # Starting from index 1, as index 0 stores our line before the first do() call 
            for j in range (1, len(current)):
                total += parse_part_one(current[j])

    return total

def read_file_one():
    total = 0
    with open(INPUT, "r") as f:
        for line in f:
            total += parse_part_one(line)
    return total

def read_file_two():
    f = open(INPUT, "r")
    input = f.read()
    f.close()
    return parse_part_two(input)

print("TOTAL PART ONE: " + str(read_file_one()))
print("TOTAL PART TWO: " + str(read_file_two()))
