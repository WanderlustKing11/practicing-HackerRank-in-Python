# HackerRank - Algorithms
# Between Two Sets
# By Douglas Horville

# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# 1. The elements of the first array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Complete the getTotalX function in the editor below. 
# It should return the number of integers that are betwen the sets.

# getTotalX has the following parameter(s):
# int a[n]: an array of integers
# int b[m]: an array of integers

# Returns:
# int: the number of integers that are between the sets

###############################################################################
#####################  Solve  #####################

def getTotalX(a,b):
  ans = {}
  nope = {}
  x = a[-1]
  y = b[0]
  c = a + b
  for i in range(x, y + 1, x):
    for num in c:
      if num > i:
        larger = num
        smaller = i
      else:
        larger = i
        smaller = num
      if larger % smaller == 0:
        if i in ans:
          ans[i] += 1
        else:
          ans[i] = 1
      else:
        if i in nope:
          nope[i] += 1
        else:
          nope[i] = 1
    if i in nope and i in ans:
      del ans[i]
  return len(ans)
  # print("Ans:", ans, "Nope:", nope)
  # print(len(ans))


###############################################################################
#####################  Main  #####################

def main():
  print(getTotalX([2, 6], [24, 36]))  # Expected output: 2
  print(getTotalX([2,4], [16, 32, 96]))   # Expected output: 3
  print(getTotalX([3,4], [24, 48]))   # Expected output: 2

main()