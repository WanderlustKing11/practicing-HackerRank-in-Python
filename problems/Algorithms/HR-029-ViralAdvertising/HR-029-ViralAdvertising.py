# HackerRank - Algorithms
# Viral Advertising
# By Douglas Horville

# HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a 
# new product, they advertise it to exactly 5 people on social media.
# On the first day, half of those 5 people (i.e., floor(5/2)=2 ) like the advertisement and 
# each shares it with 3 of their friends. At the beginning of the second day, 
# floor(5/2) x 3 = 2 x 3 = 6 people receive the advertisement.
# Each day, floor(recipients/2) of the recipients like the advertisement and will share it 
# with 3 friends on the following day. Assuming nobody receives the advertisement twice, 
# determine how many people have liked the ad by the end of a given day, beginning with 
# launch day as day 1.

# viralAdvertising has the following parameter(s):
# int n: the day number to report
# Returns int: the cumulative likes at that day

###############################################################
###########  Solve  ###########
import math

def viralAdvertising(n):
  if n == 0:
    return 0
  elif n == 1:
    return 2

  day = 1
  recipients = 5
  likes = 2
  cumulative_likes = 2

  while day < n:
    day += 1
    recipients = likes * 3
    likes = math.floor(recipients/2)
    cumulative_likes += likes
    print(f'day:{day}, recipients:{recipients}, likes:{likes}, cum_likes:{cumulative_likes}')

  return cumulative_likes

# The Recursive Approach:
# def viralAdvertising(n, day=1, recipients=5, cumulative_likes=0):
#     # Base case: if we've reached day n, return cumulative likes
#     if day > n:
#         return cumulative_likes
    
#     # Calculate likes for the current day
#     likes = recipients // 2
#     cumulative_likes += likes
    
#     # Calculate new recipients for the next day
#     new_recipients = likes * 3
    
#     # Recursive call for the next day
#     return viralAdvertising(n, day + 1, new_recipients, cumulative_likes)

      

###############################################################
###########  Main ###########

def main():
  # print(viralAdvertising(1))
  # print(viralAdvertising(2))
  # print(viralAdvertising(3))
  # print(viralAdvertising(4))
  print(viralAdvertising(5))

main()

# Std In is not complete. Will update input file and main function soon