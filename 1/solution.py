INPUT = "input.txt"
COLUMNS = 1000

left=[]
right=[]

def init_input():
    f = open(INPUT, "r")

    i = 0
    while (i < 1000):
        left.append(f.read(5))
        f.read(3)
        right.append(f.read(5))
        f.read(1)
        i += 1

    left.sort()
    right.sort()

def calc_distance():
    distance = 0

    i = 0
    while (i < COLUMNS):
        left_num = int(left[i])
        right_num = int(right[i])

        if left_num < right_num:
            distance += right_num - left_num
        elif left_num > right_num:
            distance += left_num - right_num
        
        i += 1
    
    print("Distance: " + str(distance))

def calc_similarity():
    similarity = 0

    i = 0
    while (i < COLUMNS):
        left_num = int(left[i]) 
        similarity += left_num * right.count(left[i])
        i = i + 1
        
    print("Similarity Score: " + str(similarity))

init_input()
calc_distance() # PART ONE
calc_similarity() # PART TWO