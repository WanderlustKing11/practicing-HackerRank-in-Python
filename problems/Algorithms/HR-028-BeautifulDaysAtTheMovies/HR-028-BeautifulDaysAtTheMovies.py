# HackerRank - Algorithms
# Angry Professor
# By Douglas Horville

# Lily likes to play games with integers. She has created a new game where she 
# determines the difference between a number and its reverse. For instance, 
# given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, 
# and their difference is 99.

# She decides to apply her game to decision making. She will look at a numbered range of 
# days and will only go to a movie on a beautiful day.

# Given a range of numbered days, [i...j] and a number k, determine the number of days in 
# the range that are beautiful. Beautiful numbers are defined as numbers where |i-reversed(i)| is 
# evenly divisible by k. If a day's value is a beautiful number, it is a beautiful day. 
# Return the number of beautiful days in the range.

# beautifulDays has the following parameter(s):
# int i: the starting day number
# int j: the ending day number
# int k: the divisor

# Returns int: the number of beautiful days in the range

###############################################################
###########  Solve  ###########

def beautifulDays(i, j, k):
  num_of_beautiful_days = 0
  for day in range(i, j + 1):
    reversed_day = int(str(day)[::-1])

    if abs(day - reversed_day) % k == 0:
      num_of_beautiful_days += 1
    
  return num_of_beautiful_days
      

###############################################################
###########  Main ###########

def main():
  print(beautifulDays(20, 23, 6))

main()

# Std In is not complete. Will update input file and main function soon