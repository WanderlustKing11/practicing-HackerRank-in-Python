# HackerRank - Algorithms
# Grading Students
# By Douglas Horville

# HackerLand University has the following grading policy:

# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round grade up 
# to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

def gradingStudents(grades):
  final_grades = []
  for g in grades:
    if g < 38:
      final_grades.append(g)
    else:
      if (g + 1) % 5 == 0:
        g = g + 1
        final_grades.append(g)
      elif (g + 2) % 5 == 0:
        g = g + 2
        final_grades.append(g)
      else:
        final_grades.append(g)
  return final_grades


def main():
  print('Original grades: [73, 67, 38, 33]; Final grades:', gradingStudents([73, 67, 38, 33]))

main()
