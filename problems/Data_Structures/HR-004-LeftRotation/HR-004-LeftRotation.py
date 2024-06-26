# HackerRank - Data Structures
# Left Rotation
# By Douglas Horville

# A left rotation operation on an array of size 'n' shifts each 
# of the array's elements 1 unit to the left. Given an integer, d, 
# rotate the array that many steps left and return the result.

# d = the amount to rotate by


def rotateLeft(d, arr):
    i = 0
    if d > len(arr):
        d = d % len(arr)
    newArr = arr[d:]
    del arr[d:]
    result = newArr + arr
    return result


def main():
    print(rotateLeft(54, [1,2,3,4,5,6,7,8,9,10]))


main()