# HackerRank - Data Structures
# Dynamic Array
# By Douglas Horville

# Declare a 2-dimensional array, , of  empty arrays. All arrays are zero indexed.
# Declare an integer, , and initialize it to .

# There are  types of queries, given as an array of strings for you to parse:

# Query: 1 x y
# Let .
# Append the integer  to .
# Query: 2 x y
# Let .
# Assign the value  to .
# Store the new value of  to an answers array.
# Note:  is the bitwise XOR operation, which corresponds to the ^ operator in 
# most languages. Learn more about it on Wikipedia.  is the modulo operator.
# Finally, size(arr[idx]) is the number of elements in arr[idx]

# Function Description

# Complete the dynamicArray function below.

# dynamicArray has the following parameters:
# - int n: the number of empty arrays to initialize in 
# - string queries[q]: query strings that contain 3 space-separated integers

#############################################################################
#########  Solution  #########

def dynamicArray(n, queries):
    lastAnswer = 0
    arr = []
    answers = []
    for i in range(n + 1):
        arr.append([])
    
    for query in queries:
        if query[0] == 1:
            idx = (query[1] ^ lastAnswer) % n
            arr[idx].append(query[2])
        if query[0] == 2:
            idx = (query[1] ^ lastAnswer) % n
            lastAnswer = arr[idx][query[2] % len(arr[idx])]
            answers.append(lastAnswer)

    return answers


#############################################################################
#########  Main  #########

def main():
    ourFile = open("./test/008-out.txt", "r")
    firstMultipleInput = ourFile.readline().rstrip().split()
    n = int(firstMultipleInput[0])
    q = int(firstMultipleInput[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, ourFile.readline().rstrip().split())))

    result = dynamicArray(n, queries)
    print(result)
    # print(queries)


main()

