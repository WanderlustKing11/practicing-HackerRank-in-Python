# HackerRank - Algorithms
# Angry Professor
# By Douglas Horville

# A Discrete Mathematics professor has a class of students. Frustrated with their 
# lack of discipline, the professor decides to cancel class if fewer than some number of 
# students are present when class starts. Arrival times go from on time (arrivalTime <= 0) to 
# arrived late (arrivalTime > 0).

# Given the arrival time of each student and a threshhold number of attendees, 
# determine if the class is cancelled.

# angryProfessor has the following parameter(s):
# int k: the threshold number of students
# int a[n]: the arrival times of the  students

# Returns string: either YES or NO

###############################################################
###########  Solve  ###########

def angryProfessor(k, a):
  early_students = 0
  for arrival in a:
    if arrival <= 0:
      early_students += 1
  
  if early_students >= k:
    return 'NO'
  else:
    return 'YES'    
      


###############################################################
###########  Main ###########

def main():
  print(angryProfessor(3, [-2,-1,0,1,2]))
  print(angryProfessor(3, [-1,-3,4,2]))
  print(angryProfessor(2, [0,-1,2,1]))

main()

# Std In is not complete. Will update input file and main function soon