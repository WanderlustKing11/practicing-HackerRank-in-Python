# Solve Algorithms 11/24/2024
# Douglas Horville
# Minimum Path Sum in a Grid


# Given a 2D grid of size 𝑚 × 𝑛, filled with non-negative integers, find a path from the 
# top-left corner to the bottom-right corner that minimizes the sum of all numbers along its path. 
# You can only move either down or right at any point in time.

def minPathSum(arr):
    m = 0
    n = 0
    min_sum = arr[m][n]
    while m < len(arr) - 1 and n < len(arr) - 1:
        if m < len(arr) - 1 and arr[m + 1][n] > arr[m][n + 1]:
            m += 1
            min_sum += arr[m][n]
        elif n < len(arr) - 1 and arr[m][n + 1] > arr[m + 1][n]:
            n += 1
            min_sum += arr[m][n]
        elif m == len(arr) -1:
            n += 1
            min_sum += arr[m][n]
        elif n == len(arr) - 1:
            m += 1
            min_sum += arr[m][n]

    return min_sum


###################################################################
##### Solution ######


def minPathSum_sol(arr):
    m, n = len(arr), len(arr[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = arr[0][0]
    
    # Initialize first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + arr[0][j]
    
    # Initialize first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + arr[i][0]
    
    # Fill up the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]
    
    return dp[-1][-1]

def main():
    # print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(minPathSum_sol([[1,3,1],[1,5,1],[4,2,1]]))


if __name__ == '__main__':
    main()



def main():
    print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

if __name__ == '__main__':
    main()