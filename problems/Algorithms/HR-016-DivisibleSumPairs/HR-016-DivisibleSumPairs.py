# HackerRank - Algorithms
# Subarray Division
# By Douglas Horville

# Given an array of integers and a positive integer k, determine the number of 
# (i,j) pairs where i < j and ar[i] + ar[j] is divisible by k.

# divisibleSumPairs has the following parameter(s):
# int n: the length of array ar
# int ar[n]: an array of integers
# int k: the integer divisor

# Return the number of pairs


###############################################################################
#####################  Solve  #####################

# def divisibleSumPairs(n, k, ar):
#   count = 0
#   for i in range(n):
#     j = i + 1
#     while j < n:
#       nSum = ar[i] + ar[j]
#       if nSum % k == 0:
#         count += 1
#       #   print(f'{ar[i]} + {ar[j]} = {nSum}: Yes')
#       #   print(f'Total count now = {count}')
#       # else:
#       #   print(f'{ar[i]} + {ar[j]} = {nSum}: No')
#       j += 1
#   return count

def divisibleSumPairs(n, k, ar):
  count = 0
  for i in range(n):
    for j in range(i + 1, n):
      nSum = ar[i] + ar[j]
      if nSum % k == 0:
        count += 1
      #   print(f'{ar[i]} + {ar[j]} = {nSum}: Yes')
      #   print(f'Total count now = {count}')
      # else:
      #   print(f'{ar[i]} + {ar[j]} = {nSum}: No')
  return count



###############################################################################
#####################  Main  #####################

def main():
  print(divisibleSumPairs(6, 5, [1,2,3,4,5,6]))  # Expected output: 3
  print(divisibleSumPairs(6, 3, [1,2,3,6,1,2]))  # Expected output: 5


main()
