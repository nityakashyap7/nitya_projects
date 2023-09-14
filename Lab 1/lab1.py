'''
    Nitya Kashyap
    Lab 1
    CIS 41A
    1/14/2023
    Description: numbers, strings, arithmetic operators, IO
'''


# Create a constant named MAX and set it to 40.
MAX = 40

'''Prompt and read in the user’s name.
# The user can enter their name in any combination of upper and lower case.'''
name = input("Enter your name: ").title()

'''Ask the user for the number of previous programming classes they’ve taken,
and read in the data as a number'''
numOfProgClass = int(input("Enter the number of programming classes you've taken: "))

'''Ask the user for their goal when taking the CIS 41A class. 
The user can enter upper or lower case letters.'''
goal = input("Enter the goal you have for this class: ")

# Print a blank line
print()

#print user's name in a box with specified format:
'''A line of MAX number of asterisks (*). Don’t hard code 40 here.'''
print("*"*MAX)

'''A line with * at the beginning and end, 
and an appropriate number of spaces in between.'''
print("*" + " "*(MAX-2) + "*")

'''A line with * at the beginning and end, 
and the user’s name centered within the 2 *’s.
The user’s first and last names should have the first letter in uppercase, 
and all other letters in lowercase.'''
numSpaces = (MAX - 2 - len(name))
leftSideSpaces = numSpaces//2
rightSideSpaces = numSpaces - leftSideSpaces
print("*" + " "*leftSideSpaces + name + " "*rightSideSpaces + "*")

'''A line with * at the beginning and end, 
and an appropriate number of spaces in between.'''
print("*" + " "*(MAX-2) + "*")

'''A line of MAX number of *’s'''
print("*"*MAX)

'''Print the number of previous programming classes that the user has taken, 
with explanation text.'''
print(f"You've taken {numOfProgClass} programming classes")

'''Print a header line of text, 
then print the user’s goal for taking CIS 41A on a second line. 
The user’s goal should be in all uppercase.'''
print(f"Your goal for this class is:\n{goal.upper()}")


'''Test Run #1:
Enter your name: Nitya Kashyap
Enter the number of programming classes you've taken: 2
Enter the goal you have for this class: Learn Python to use in the intro to data science class (CIS 9)!

****************************************
*                                      *
*            Nitya Kashyap             *
*                                      *
****************************************
You've taken 2 programming classes
Your goal for this class is:
LEARN PYTHON TO USE IN THE INTRO TO DATA SCIENCE CLASS (CIS 9)!

Test Run #2:
Enter your name: Nitya  Kashyap
Enter the number of programming classes you've taken: 2
Enter the goal you have for this class: Learn Python to use in the intro to data science class (CIS 9)!

****************************************
*                                      *
*            Nitya  Kashyap            *
*                                      *
****************************************
You've taken 2 programming classes
Your goal for this class is:
LEARN PYTHON TO USE IN THE INTRO TO DATA SCIENCE CLASS (CIS 9)!
'''



