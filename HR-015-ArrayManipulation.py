# HackerRank - Algorithms
# Array Manipulation
# By Douglas Horville

# Starting with a 1-indexed array of zeros and a list of operations, 
# for each operation add a value to each the array element between two 
# given indices, inclusive. Once all operations have been performed, 
# return the maximum value in the array.


# V1.0 - My first attempt works correctly, but it holds O(n^2), if not worse. It failed the test because it was too slow

# def arrayManipulation(n, queries):
#   arr = [0] * n
#   max_value = 0
#   [a, b, k] = [0, 1, 2]

#   for q in queries:
#     for i in range(q[a] - 1, q[b]):
#       arr[i] += q[k]
#     print(arr)

#   for j in arr:
#     if j > max_value:
#       max_value = j  
#   return arr


################################################################################################

#Try to flatten the for loop:

# for a,b,k in queries:
#     arr[a-1] += k
#     arr[b] -= k
#     # print(arr)

# Instead of running an internal loop for the given range in each instruction-line and adding the ‘k’ value to each of those indices, we could simply add the ‘k’ value to the at the ‘a’th index and subtract the ‘k’ value from the ‘b’th index. And while finding the maximum value, we declare a max = 0 and a sum = 0 variable. We iterate through the resultant array and add each of its elements into the sum variable. At every iteration, we check whether the sum variable is bigger than the max variable or not. If yes, then we set max = sum.


################################################################################################

# V2.0 - The difference array technique which allows us to perform interval updates in constant time, and compute the resultant array values in linear time.

def arrayManipulation(n, queries):
  arr = [0] * (n + 1)

  for q in queries:
    a, b, k = q[0], q[1], q[2]
    arr[a - 1] += k
    if b < n:
      arr[b] -= k

  max_value = 0
  curr_value = 0
  for i in range(n):
    curr_value += arr[i]
    if curr_value > max_value:
      max_value = curr_value
  return arr, max_value

################################################################################################


# def arrayManipulation(n, queries):
#   arr = [0] * (n + 1)

#   for q in queries:
#     a, b, k = q[0], q[1], q[2]
#     arr[a - 1] = arr[a -1] + k
#     arr[b + 1] = arr[b + 1] - k
    
#   max_value = 0
#   curr_value = 0

#   for i in arr:
#     curr_value += arr[i - 1]
#     if curr_value > max_value:
#       max_value = curr_value


#   return max_value



def main():
  # print(arrayManipulation(10, [[1,5,3],[4,8,7],[6,9,1]]))
  # print(arrayManipulation(5, [[1,2,100],[2,5,100],[3,4,100]]))
  print(arrayManipulation(10, [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]))  # expected output: 31
  


main()