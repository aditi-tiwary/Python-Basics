Control Flow: How programs "make decisions" by evaluating different conditions, and start introducing logic into our code

If Statement: An if statement is used to test a condition for truth:

If the condition evaluates to True, code in the if part is executed.
If the condition evaluates to False, code is skipped.

Problem: Create a grades.py program that checks whether a grade is above or below 55.

Start by creating a variable called grade and give it a value between 0-100.

Write a if/else statement for the following:

If grade is greater than or equal to 55, then print "You passed."
Else, print "You failed."
After you run the code, change grade's value and rerun it. Do this a few times to make sure it's working as intended.

Solution
import random
grade = random.randint(0,100)
if grade > 90:
  print('You passed!')
else:
  print('Fail')
