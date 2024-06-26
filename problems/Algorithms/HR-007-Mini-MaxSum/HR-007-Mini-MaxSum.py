# HackerRank - Algorithms
# Mini-Max Sum
# By Douglas Horville

# Given five positive integers, find the minimum and maximum values that 
# can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of 
# two space-separated long integers.

# miniMaxSum has the following parameter(s):
# arr: an array of 5 integers

# Print two space-separated integers on one line: 
# the minimum sum and the maximum sum of 4 of 5 elements.

def miniMaxSum(arr):
    # sort the array using insertion sort
    for i in range(1, len(arr)):   # exclusive range, so 1-4
        pos = i
        temp = arr[i]

        while pos > 0 and arr[pos -1] > temp:
            arr[pos] = arr[pos - 1]     # shift left
            pos -= 1
        arr[pos] = temp

    # Find the min and max sums
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(f"{min_sum} {max_sum}")


def main():
    print(miniMaxSum([1,3,5,7,9]))  # Expected output: 16 24
    print(miniMaxSum([1,2,3,4,5]))  # Expected output: 10 14

main()