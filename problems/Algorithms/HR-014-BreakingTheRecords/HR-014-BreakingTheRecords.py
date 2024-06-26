# HackerRank - Algorithms
# Breaking the Records
# By Douglas Horville

# Maria plays college basketball and wants to go pro. 
# Each season she maintains a record of her play. 
# She tabulates the number of times she breaks her season record for 
# most points and least points in a game. Points scored in the first 
# game establish her record for the season, and she begins counting from there.

# Given the scores for a season, determine the number of times Maria breaks 
# her records for most and least points scored during the season.

# breakingRecords has the following parameter(s):
# int scores[n]: points scored per game

# Returns
# int[2]: An array with the numbers of times she broke her records. 
# Index 0 is for breaking most points records, 
# and index 1 is for breaking least points records.


###############################################################################
#####################  Solve  #####################
import os

def breakingRecords(scores):
  records = {
    'rec_high' : 0,
    'rec_low' : 0,
    'min' : 0,
    'max' : 0
  }
  ans = []
  records['rec_high'] = scores[0]
  records['rec_low'] = scores[0]
  print("First Game, initial start", records)
  for score in scores:
    if score > records['rec_high']:
      records['rec_high'] = score
      records['max'] += 1
      print('New high score:', records)
    if score < records['rec_low']:
      records['rec_low'] = score
      records['min'] += 1
      print('New low score:', records)
  ans.append(records['max'])
  ans.append(records['min'])
  return ans


###############################################################################
#####################  Main  #####################

def main():
  script_dir = os.path.dirname(os.path.abspath(__file__))
  input_file_path = os.path.join(script_dir, 'test', 'A-014-input.txt')

  inputFile = open(input_file_path, 'r')
  content = inputFile.readlines()
  inputFile.close()

  n = content[0].rstrip()
  string_list = content[1].split()
  scores = list(map(int, string_list))
  print(breakingRecords(scores))

main()