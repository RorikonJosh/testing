# COMP 1080SEF/S208F
# Quiz 2

"""
Important notice:
1. To complete this quiz, you need to complete ALL the tasks (where there are #TODO marks) and demonstrate the results to your tutor on Week 6.
2. You SHOULD NOT modify the given code for the questions, unless they are marked as #TODO.
2. You need to run this program in scripting mode (in command prompt or Anaconda command prompt).
3. To test your program, the tutor will give some test cases. Your program will only be considered as correct when it can pass all the test cases.
"""

print("\nDeclaration on Academic Integrity")

# Declaration on Academic Integrity
your_name = input("Please input your name: ")
print("I, " + your_name + ", declare that I complete this quiz independently, \nand the following solution is the result of my own work. \nI understand the violation of academic honesty will have severe consequences. ") 



# ============================================ TASK 1 ============================================
print("\nTask #1")
# In Quiz 1, you calculated the body mass index (BMI)
# BMI is calculated by weight (in KG) / the sequare of height (in meters)
# For example, a person, weighing 52KG and 155 cm tall, the BMI is 21.6 (preserving ONE decimal place)
weight = input("Input your weight (in KG): ")  
height = input("Input your height (in cm): ")  
bmi = int(weight) / ((int(height)/100) ** 2)   
result_part_1 = "You weigh {}KG and is {}cm tall, your BMI is {:.1f}.".format(weight, height, bmi) # The answer of Quiz 1 Task 2.

# This is the World Health Organization's (WHO) recommended body weight based on BMI values for adults. It is used for both men and women, age 20 or older. 
# We hope the program can give some instructions to the user based on their BMI. 
# For example, if a user has BMI below 16, we may tell him/her that he/she is suffering severe thinness. 

'''
BMI              |    Category 
< 16             |  Severe Thiness
16 <= BMI < 17   |  Moderate Thiness
17 <= BMI < 18.5 |  Mild Thiness
18.5 <= BMI < 25 |  Normal
25 <= BMI < 30   |  Overweight
30 <= BMI < 35   |  Obsese Class I 
35 <= BMI < 40   |  Obsese Class II 
40 <= BMI        |  Obsese Class III 
'''

# You may need decision structure to achieve the goal.
# ===============Your solution ===============#
def switch(bmi):
    if bmi < 16 :
        return "Severe Thiness"
    elif bmi < 17 :
        return "Moderate Thiness"
    elif bmi < 18.5 :
        return "Mild Thiness"
    elif bmi < 25 :
        return "Normal"
    elif bmi < 30 :
        return "Overweight"
    elif bmi < 35 :
        return "Obsese Class I "
    elif bmi < 40 :
        return "Obsese Class II "
    elif bmi >= 40 :
        return "Obsese Class III "
    
print(result_part_1, "Your BMI is", switch(bmi))
    #TODO
    #TODO
#TODO

"""
">" means the output is in command prompt. You do not need to include ">" in the outputs.

* Example
> Input your weight (in KG): 52
> Input your height (in cm): 155
> You weigh 52KG and is 155cm tall, your BMI is 21.6. Your BMI is Normal.

> Input your weight (in KG): 60
> Input your height (in cm): 140
> You weigh 60KG and is 140cm tall, your BMI is 30.6. Your BMI is Obsese Class I.

> Input your weight (in KG): 60
> Input your height (in cm): 190
> You weigh 60KG and is 190cm tall, your BMI is 16.6. Your BMI is Moderate Thiness.

"""


# ============================================ TASK 2 ============================================
print("\nTask #2")
# In this task, you need to find out all the numbers, between 1 and 100, that are divisible by 
# the two numbers given by the tutor.
# "A is divisible by B" means no remainder when A is divided by B.
# For example, 10 is divisible by 5 (remainder is 0), but is not divisible by 3 (remainder is 1)

# Note:
# 1. The for-loop for checking every integer from 1 to 100 is given. You only need to define the 
# condition structure that is needed.
# 2. The numbers should be printed in ONE LINE and separated by spaces. 

x_1 = int(input("Input the first number: "))

x_2 = int(input("Input the second number: "))

for i in range(1, 101):
    #print(i) # for you to understand what the variable i is. Can be removed.
    mod1 = i % x_1
    mod2 = i % x_2
    if int(mod1) == 0 :
        if int(mod2) == 0 :
            print(i, end=" ") #TODO
    #TODO
    #TODO


"""
* Example
> Input the first number: 3
> Input the first number: 7
> 21 42 63 84

> Input the first number: 8
> Input the first number: 12
> 24 48 72 96

> Input the first number: 5
> Input the first number: 10
> 10 20 30 40 50 60 70 80 90 100

* Requirement
1. You need to complete the #TODO part, which is a conditional structure under the for loop.
2. The numbers will be given by the tutor during the tutorial.
3. Hint: How can we know if a number is divisible by another number, i.e., no remainder.
"""
