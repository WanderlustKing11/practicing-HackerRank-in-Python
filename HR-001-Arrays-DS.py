# HackerRank
# 001: Arrays - DS
# 3/12/24
# By Douglas Horville

# An array is a type of data structure that stores elements of the same 
# type in a contiguous block of memory. In an array, , of size , each 
# memory location has some unique index,  (where ), that can be 
# referenced as  or .

# Reverse an array of integers.

def reverseArray(a):
    n = []
    i = -1
    while i > (len(a) * -1) - 1:
        n.append(a[i])
        i -= 1
    return n
        

def main():
    print(reverseArray([1,2,3,4]))

main()