# HackerRank
# Number Line Jumps
# By Kris & Doug

# Figure out a way to get both kangaroos at the same 
# location at the same time as part of the show. 
# If it is possible, return YES, otherwise return NO.

# int x1, int v1: starting position and jump distance for kangaroo 1
# int x2, int v2: starting position and jump distance for kangaroo 2

def kangaroo(x1, v1, x2, v2):
  if x1 >= x2 and v1 > v2:
    return 'NO'
  if x2 >= x1 and v2 > v1:
    return 'NO'
  if x1 == x2 and v1 == v2:
    return 'YES'
  if x1 == x2 and v1 != v2:
    return 'NO'
  if x1 != x2 and v1 == v2:
    return 'NO'

  starting = abs(x1 - x2)
  velocity = abs(v1 - v2)
  if starting % velocity == 0:
    return 'YES'
  else:
    return 'NO'
  

def main():
  print(kangaroo(0, 3, 4, 2))  # Expected output: 'YES'
  print(kangaroo(0, 2, 5, 3))  # Expected output: 'NO'
  print(kangaroo(2, 3, 2, 3))  # Expected output: 'YES'



main()