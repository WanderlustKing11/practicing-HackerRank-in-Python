# HackerRank - Data Structures
# 2D Array
# By Douglas Horville

# Given a 6 x 6 2D Array (arr), calculate the hourglass sum for every 
# hourglass in , then print the maximum hourglass sum.

def hourglassSum(arr):
    [a,b,c,d,e,f,g] = [0,0,0,0,0,0,0]   # 7 elements comprises a complete hourglass
    largestSum = -100
    for i in range(4):  # 4 possible columns in 2D array
        for j in range(4): # 4 possible rows in 2D array
            a = arr[i][j]
            b = arr[i][j + 1]
            c = arr[i][j + 2]
            d = arr[i + 1][j + 1]
            e = arr[i + 2][j]
            f = arr[i + 2][j + 1]
            g = arr[i + 2][j + 2]
            hourglassSum = a + b + c + d + e + f + g
            if hourglassSum > largestSum:   # save the largest hoursglass sum
                largestSum = hourglassSum
        #     print(hourglassSum, end=', ') # All hourglass sums
        # print()
    return largestSum


def main():
    # print(hourglassSum([
    #     [-9,-9,-9,1,1,1],
    #     [0,-9,0,4,3,2],
    #     [-9,-9,-9,1,2,3],
    #     [0,0,8,6,6,0],
    #     [0,0,0,-2,0,0],
    #     [0,0,1,2,4,0]
    # ]))
    print(hourglassSum([
        [-1, -1, 0, -9, -2, -2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5],
    ]))

# Expected Output:
# [-63, -34, -9, 12]
# [-10,   0, 28, 23]
# [-27, -11, -2, 10]
# [9,  17, 25, 18]
# The highest hourglass sum is 28
# from the hourglass beginning at row 1, column 2:
# 0, 4, 3
#    1
# 8, 6, 6

main()