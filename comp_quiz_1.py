# COMP 1080SEF/S208F
# Quiz 1

"""
Important notice:
1. To complete this quiz, you need to complete ALL the three tasks (where there are #TODO marks) and demonstrate the results to your tutor on Week 6.
2. You SHOULD NOT modify the given code for the questions, unless they are marked as #TODO.
2. You need to run this program in scripting mode (in command prompt or Anaconda command prompt).
3. To test your program, the tutor will give some test cases. Your program will only be considered as correct when it can pass all the test cases.
"""

# ============================================ TASK 1 ============================================
print("\n Task #1")
# In this first task, you need to format the string output.

# Declaration on Academic Integrity
your_name = input("Please input your name: ")
print("I, ", your_name, ", declare that I complete this quiz independently, \nand the following solution is the result of my own work.", sep='') #TODO

"""
* Example
> Please input your name: Roy Li (you need to input your own name for declaration)
> I, Roy Li, declare that I complete this quiz independently, 
and the following solution is the result of my own work.

* Requirement:
1. You can only use ONE print() function. 
2. The spaces and lines of the output must be consistent with the example. The following outputs will not be accepted:
(1) I,Roy Li,declare that ... (lack of spaces)
(2) I, Roy Li , declare that ... (extra spaces)
(3) I, Roy Li, declare that I complete this quiz independently, and the following ... (no newline)
"""


# ============================================ TASK 2 ============================================
print("\n Task #2")
# In the second task, you need to ask for the user inputs to calculate the body mass index (BMI)
# BMI is calculated by weight (in KG) / the sequare of height (in meters)
# For example, a person, weighing 52KG and 155 cm tall, the BMI is 21.6 (preserving ONE decimal place)
weight = int(input("Input your weight (in KG): "))#TODO
height = int(input("Input your height (in cm): "))#TODO
bmi = weight / pow((height / 100), 2)#TODO
print("You weigh ", weight, "KG and is ", height, "cm tall, your BMI is ", round(bmi, 1), ".", sep='') #TODO

"""
* Example
> Input your weight (in KG): 52
> Input your height (in cm): 155
> You weigh 52KG and is 155cm tall, your BMI is 21.6.

* Requirement:
1. The values of weight (in KG) and height (in cm) will be provided by the tutor. 
2. The result should be rounded into one decimal place.
3. The spaces of the output must be consistent with the example. The following outputs will not be accepted:
(1) You weigh 52KG and is 155cm tall, your BMI is21.6 (lack of spaces and period)
(2) You weigh 52 KG and is 155 cm tall, your BMI is 21.6. (extra spaces)
"""


# ============================================ TASK 3 ============================================
print("\n Task #3")
# In the last task, you need to format the output and display the content as requested.

string_1 = "Hong Kong"
string_2 = "Met"
string_3 = "ropolitan Univ"
string_4 = "ersity,"
string_5 = "Jockey Club Campu"
string_6 = "lock D"

print(string_1, string_2, end = '') #TODO)
print(string_3, string_4, sep='') #TODO)
print(string_5, "s, B", string_6, sep='') #TODO)

"""
* Example
> Hong Kong Metropolitan University,
Jockey Club Campus, Block D

* Requirement
1. You should only modify the #TODO parts in three print() functions, and remain all the strings unchanged.
2. The results should be consistent with the example.
3. Hint: You may change the separators to more than spaces (" "), newlines ("\n"), and tabs ("\t"). You can try other character(s).
"""
