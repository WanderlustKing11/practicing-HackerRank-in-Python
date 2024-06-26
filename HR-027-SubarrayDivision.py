# HackerRank - Algorithms
# Subarray Division
# By Douglas Horville

# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

# birthday has the following parameter(s):
# int s[n]: the numbers on each of the squares of chocolate
# int d: Ron's birth day
# int m: Ron's birth month
# Returns:
# int: the number of ways the bar can be divided


###############################################################################
#####################  Solve  #####################

def birhtdays(s, d, m):
  count = 0
  for i in range(len(s) - (m - 1)):
    seg_length = m
    temp_sum = 0
    while seg_length > 0:
      temp_sum += s[i]
      seg_length -= 1
      i += 1
    if temp_sum == d:
      count += 1
  return count

###############################################################################
#####################  Main  #####################

def main():
  print(birhtdays([2,2,1,3,2], 4, 2))  # Expected output: 2
  print(birhtdays([1,2,1,3,2], 3, 2))  # Expected output: 2
  print(birhtdays([1,1,1,1,1,1], 3, 2))  # Expected output: 0
  print(19%3)
main()