# HackerRank - Algorithms
# Sparse Arrays
# By Douglas Horville

# There is a collection of input strings and a collection of query strings. 
#For each query string, determine how many times it occurs in the list of input strings. 
# Return an array of the results. The function must return an array 
# of integers representing the frequency of occurrence of each query string in stringList.

def matchingStrings(stringList, queries):
  answer = []
  for q in queries:
    count = 0
    for s in stringList:
      if q == s:
        count += 1
    answer.append(count)
  return answer


def main():
  print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))

main()
