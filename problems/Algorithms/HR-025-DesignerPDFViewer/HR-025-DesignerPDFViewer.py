# HackerRank - Algorithms
# Designer PDF Viewer
# By Douglas Horville

# When a contiguous block of text is selected in a PDF viewer, the 
# selection is highlighted with a blue rectangle. In this PDF viewer, 
# each word is highlighted independently.

# designerPdfViewer has the following parameter(s):
# int h[26]: the heights of each letter
# string word: a string

# Return int: the size of the highlighted area

###############################################################
###########  Solve  ###########

def designerPdfViewer(h, word):
    # Write your code here
    if len(h) == 1:
      return h[0]
    
    max_height = 0
    for letter in word:
      i = (ord(letter)) - 97
      if h[i] > max_height:
        max_height = h[i]
    
    return len(word) * max_height


###############################################################
###########  Main ###########

def main():
   print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], 'abc'))

main()

# Std In is not complete. Will update input file and main function soon