# HackerRank - Algorithms
# Compare the Triplets
# By Douglas Horville

# Given an array of integers, find the sum of its elements.

# Print the sum of the array's elements as a single integer.

def simpleArraySum(ar):
    sum = 0
    for num in ar:
        sum += num
    return sum

def main():
    print(simpleArraySum([1,2,3]))  # Expected output: 6
    print(simpleArraySum([1,2,3,4,10,11]))  # Expected output: 31

main()