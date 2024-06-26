# HackerRank - Algorithms
# Diagonal Difference
# By Douglas Horville

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.


def diagonalDifference(arr):
    [primary_d, i , j] = [0, 0, 0]
    while i < len(arr):      # loop through all the rows
        primary_d += arr[i][j]
        i += 1
        j += 1

    # start at the top right of the matrix, so m (rows) is 0 for the top row, 
    # but n (columns) is -1 to be the last element of the array
    [secondary_d, m, n] = [0, 0, -1]
    while m < len(arr):      # loop through all the rows
        secondary_d += arr[m][n]
        m += 1
        n -= 1
    result = abs(primary_d - secondary_d)
    return result


def main():
    print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))

main()