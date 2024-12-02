def calculate_diff(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    max_num = max(n1,n2)
    min_num = min(n1,n2)
    return max_num - min_num

def calculate_similarity(n1, list):
    n1 = int(n1)
    multiplier = 0
    for num in list:
        if int(num) == n1:
            multiplier = multiplier + 1
    return n1 * multiplier
    

def read_file(input):
    f = open(input, "r")
    list1 = []
    list2 = []
    for line in f:
        num1 = line.split("   ")[0]
        num2 = line.split("   ")[1]
        list1.append(num1)
        list2.append(num2)
    list1.sort()
    list2.sort()
    return [list1,list2]

def main_1():
    i = 0
    total_distance = 0
    lists = read_file("Inputs/day1.txt")
    print (lists[0])
    while i < len(lists[0]):
        diff = calculate_diff(lists[0][i],lists[1][i])
        total_distance += diff
        i = i + 1
    print(total_distance)

def main_2():
    i = 0
    total_similarity = 0
    lists = read_file("Inputs/day1.txt")
    while i < len(lists[0]):
        similarity = calculate_similarity(lists[0][i],lists[1])
        total_similarity = total_similarity + similarity
        i = i+1
    print(total_similarity)
    return total_similarity


#main_1()
main_2()