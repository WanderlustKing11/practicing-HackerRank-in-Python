# HackerRank - Algorithms
# Plus Minus
# By Douglas Horville

# Given an array of integers, calculate the ratios of its 
# elements that are positive, negative, and zero. Print the decimal 
# value of each fraction on a new line with  places after the decimal.

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    print("%.6f" % (positive / len(arr)))
    print("%.6f" % (negative / len(arr)))
    print("%.6f" % (zero / len(arr)))


def main():
    plusMinus([-4,3,-9,0,4,1])

main()