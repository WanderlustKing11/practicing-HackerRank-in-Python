# HackerRank - Algorithms
# Bill Division
# By Douglas Horville

# Two friends Anna and Brian, are deciding how to split the 
# bill at a dinner. Each will only pay for the items they consume. 
# Brian gets the check and calculates Anna's portion. 
# You must determine if his calculation is correct.

# Print 'Bon Appetit' if the bill is fairly split. Otherwise, it
# should print the integer amount of money that Brian owes Anna.

# bonAppetit has the following parameters(s):
# - bill: an array of integers representing the cost of each 
#         item ordered
# - k: an integer represting the zero-based index of the item 
#      Anna doesn't eat
# - b: the amount of money that Anna contributed to the bill

################################################################
#########################  Solve  ##############################

def bonAppetit(bill, k, b):
    print('The bill is:', bill)
    print('The item Anna didnt want cost:', bill[k])
    print(f"Annas contribution to the bill was: {b}")
    total = 0
    for item in bill:
        total += item
    annas_bill = (total - bill[k]) / 2
    if annas_bill == b:
        return "Bon Appetit"
    else:
        refund = int(b - annas_bill)
        return refund



################################################################
#########################  Main  ##############################

def main():
    print(bonAppetit([3, 10, 2, 9], 1, 12))


main()

