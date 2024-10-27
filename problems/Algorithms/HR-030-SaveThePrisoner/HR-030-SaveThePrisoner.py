# HackerRank - Algorithms
# Save the Prisoner
# By Douglas Horville

# A jail has a number of prisoners and a number of treats to pass out to them. Their jailer 
# decides the fairest way to divide the treats is to seat the prisoners around a circular table in 
# sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the 
# prisoner in that chair, one candy will be handed to each prisoner sequentially around the 
# table until all have been distributed.
# The jailer is playing a little joke, though. The last piece of candy looks like all the others, 
# but it tastes awful. Determine the chair number occupied by the prisoner who will receive that 
# candy.

# saveThePrisoner has the following parameter(s):
# int n: the number of prisoners
# int m: the number of sweets
# int s: the chair number to begin passing out sweets from

# Returns int: the chair number of the prisoner to warn

###############################################################
###########  Solve  ###########


def saveThePrisoner(n, m, s):
  result = (s + m - 1) % n
  if result == 0:
    return n
  else:
    return result


###############################################################
###########  Alternative Solutions  ###########

def whileLoopPrisoner(n, m, s):
    current_seat = s  # Start distributing from seat 's'
    candies_left = m  # Total candies to distribute

    # While there are candies left to distribute
    while candies_left > 1:  # We stop when 1 candy is left
        current_seat += 1  # Move to the next seat
        candies_left -= 1   # Distribute one candy

        # Wrap around to seat 1 if we've gone past the last seat
        if current_seat > n:
            current_seat = 1

    return current_seat  # The last seat to receive candy

# Example usage
print(saveThePrisoner(4, 6, 2))  # Expected output: 3



###############################################################
###########  Main ###########

def main():
  print(saveThePrisoner(4, 6, 2)) # expected output: 3
  print(saveThePrisoner(5, 2, 1)) # expected output: 1
  print(saveThePrisoner(5, 2, 2)) # expected output: 2
  print('While loop method:', whileLoopPrisoner(4, 6, 2)) # expected output: 3

main()

# Std In is not complete. Will update input file and main function soon