# HackerRank - Algorithms
# Circular Array Rotation
# By Douglas Horville

# John Watson knows of an operation called a right circular rotation on an array of integers. 
# One rotation operation moves the last array element to the first position and shifts all 
# remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an 
# array of integers. Sherlock is to perform the rotation operation a number of times then 
# determine the value of the element at a given position.
# For each array, perform a number of right circular rotations and return the values of the 
# elements at the given indices.

# circularArrayRotation has the following parameter(s):
# int a[n]: the array to rotate
# int k: the rotation count
# int queries[1]: the indices to report

# Returns int[q]: the values in the rotated `a` as requested in `m` 

###############################################################
###########  Solve  ###########

def circularArrayRotation(a, k, queries):
    results = []
    diff = (k % len(a)) - 1
    # print(f'diff = {diff}')
    final_rotation_front_index = (len(a) - 1) - diff
    # print(f'target index: {final_rotation_front_index}')
    # first_num = a[final_rotation_front_index]
    # print(f'target number: {first_num}')
    first_half = a[:final_rotation_front_index]
    # print(f'first half: {first_half}')
    second_half = a[final_rotation_front_index:]
    # print(f'isolated array: {second_half}')
    fully_rotated_array = second_half + first_half
    # print(f'updated array: {fully_rotated_array}')
    for q in queries:
        results.append(fully_rotated_array[q])
    # print(f'values for queries: {queries}:')
    return results

###############################################################
###########  Alternative Solutions  ###########

## This solution was my first attempt. But it was too slow. The above solution is more optimal.

def circularArrayRotation_b(a, k, queries):
    restults = []
    num_of_rotations = 0
    while num_of_rotations < k:
       last_index = a.pop()
       a = [last_index] + a
       # a.instert(0, last_index) # here's another option for using the insert() method
       num_of_rotations += 1
    for q in queries:
       restults.append(a[q])
    return restults



###############################################################
###########  Main ###########

def main():
  print(circularArrayRotation([3, 4, 5], 2, [1, 2])) # expected output: [5, 3]
  print(circularArrayRotation([1, 2, 3], 2, [0, 1, 2])) # expected output: [2, 3, 1]
  print(circularArrayRotation([21, 23, 25, 27, 29, 31, 33], 10, [0, 6])) # expected output: [29, 27]

main()

# Std In is not complete. Will update input file and main function soon