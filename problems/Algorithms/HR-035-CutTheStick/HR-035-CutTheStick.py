# HackerRank - Algorithms
# Cut The Stick
# By Douglas Horville

# You are given a number of sticks of varying lengths. You will iteratively cut the 
# sticks into smaller sticks, discarding the shortest pieces until there are none left. 
# At each iteration you will determine the length of the shortest stick remaining, cut that 
# length from each of the longer sticks and then discard all the pieces of that shortest length. 
# When all the remaining sticks are the same length, they cannot be shortened so discard them.

# Given the lengths of n sticks, print the number of sticks that are left before each 
# iteration until there are none left.

# Complete the cutTheSticks function in the editor below. It should return an array of 
# integers representing the number of sticks before each cut operation is performed.

# cutTheSticks has the following parameter(s):
# int arr[n]: the lengths of each stick
# Returns int[]: the number of sticks after each iteration

###############################################################
###########  Solve  ###########

# def cutTheSticks(arr):
#     # Write your code here
#     num_of_sticks = []
#     arr.sort()
#     print(f'sorted array: {arr}')
#     while len(arr) > 0:
#         num_of_sticks.append(len(arr))
#         print(f'sticks = {num_of_sticks}')
#         for i in range(len(arr) - 1):
#             arr[i] -= arr[0]
#             print(f'i - arr[0] -> {i} - {arr[0]} = {i - arr[0]}')
#             arr.pop(0)

#     return num_of_sticks


###################################################################
####### 2nd Attempt #######

def cutTheSticks(arr):

    #1. store a list num_of_sticks = []
    num_of_sticks = []
    #2. sort the arr
    arr.sort()
    #3. isolate the first element, save it in a variable (smallest_stick)
    smallest_stick = arr[0]
    #4. While loop to keep cutting more sticks
    while len(arr) > 0:
        #5. append the current length of the array into our stored list: num_of_sticks.append(len(arr))
        num_of_sticks.append(len(arr))
        #6. nested for loop through the sorted arr (by range so that I can use the index)
        for i in range(len(arr) - 1):
        #7. subtract `smallest_stick` from every element (i) # arr[i] -= smallest_stick
            print(f'smallest stick = {smallest_stick}')
            arr[i] = arr[i] - smallest_stick
            print(arr)
            #8. condition: if (after subtraction) arr[i] == 0:
            if arr[i] == 0:
                #9. then remove that element from the list -> arr.pop(arr[i])
                arr.pop(i)
    #10. return num_of_sticks
    print(f'sticks = {num_of_sticks}')
    return num_of_sticks

###############################################################
###########  Main ###########

def main():
    print(cutTheSticks([1,2,3])) # expected output: [3,2,1]
    print(cutTheSticks([5,4,4,2,2,8])) # expected output: [6,4,2,1]

main()

# Std In is not complete. Will update input file and main function soon