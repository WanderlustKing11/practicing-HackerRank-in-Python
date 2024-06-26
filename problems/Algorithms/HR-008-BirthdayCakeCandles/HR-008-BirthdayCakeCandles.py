# HackerRank - Algorithms
# Birthday Cake Candles
# By Douglas Horville

# You are in charge of the cake for a child's birthday. You have 
# decided the cake will have one candle for each year of their total age. 
# The age of the child will be the number of integers given, most likely in an array.
# Each candle/integer will have its own height, and the maximum height of the candles
# is `n` units high (minimum is 1).
# They will only be able to blow out the tallest of the candles. 

# Count how many candles are tallest.


# First try, save state in variables

# def birhtdayCakeCandles(candles):
#     tallest_candle = 0
#     numOfTallest = 1
#     for i in candles:
#         if i > tallest_candle:
#             tallest_candle = i
#             numOfTallest = 1
#         elif i == tallest_candle:
#             numOfTallest += 1
#     print("Tallest candle =", tallest_candle)
#     print(f"There are {numOfTallest} candles he can blow out.")
#     return numOfTallest

######################################################################################

# Second method, store values in dictionary

def birthdayCakeCandles(candles):
  stored_candles = {}
  for i in candles:
    if i in stored_candles:
      stored_candles[i] += 1
    else:
      stored_candles[i] = 1
  tallest_candle = max(stored_candles)
  print((f"The tallest candles were {tallest_candle} units high"))
  print(f"There were {stored_candles[tallest_candle]}")
  return stored_candles[tallest_candle]


def main():
  print(birthdayCakeCandles([3,2,1,3,3,3,3]))
  # print(birthdayCakeCandles([2,2,2,2,2,7,8,6,3,4,5,6,8,7,5,3,4,1,2,2,2,2,2,2]))

main()