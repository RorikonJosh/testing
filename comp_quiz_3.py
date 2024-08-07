# ============================================ TASK 3 ============================================
print("\nTask #3")
# In Task 2, the solution has been more reasonable and complete. We want to make it even better in Task 3.
# We hope the program can wait for and check on another input value. In such case, an infinite while True loop should be used.

# To maintain a good user experience, we hope the user has the decision to continue or not.
# When "Q" or "q" is input, the infinite loop should break, and the program should stop.



# --------------------- Your Solution Begins Here ---------------------

while True:
    num = input("Enter a number (Enter Q/q to Quit): ")
    #TODO
    try:
        num = int(num)
    except ValueError:
        if num == "Q" or num == "q":
            break
        else:
            print(f"{num} is not a number")
    else:
        is_prime = True
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
            if is_prime:
                print(num, "is a prime number")
            else:
                print(num, "is not a prime number")
        else:
            print(f'{num} is not greater than 1')

# --------------------- Your Solution Ends Here ---------------------

"""
* Example
!!Note the following inputs/outputs are in a single execution
======Start======
> Enter a number (Enter Q/q to Quit): 15
> 15 is not a prime number
> Enter a number (Enter Q/q to Quit): 16
> 16 is not a prime number
> Enter a number (Enter Q/q to Quit): 17
> 17 is a prime number
> Enter a number (Enter Q/q to Quit): -1
> -1 is not greater than 1
> Enter a number (Enter Q/q to Quit): 1
> 1 is not greater than 1
> Enter a number (Enter Q/q to Quit): c
> c is not a number
> Enter a number (Enter Q/q to Quit): Roy
> Roy is not a number
> Enter a number (Enter Q/q to Quit): Q    ##OR##  > Enter a number (Enter Q/q to Quit): q
======Stop======

* Requirement
1. You need to complete the #TODO part using a while-loop or a for-loop with suitable input validation in an infinite while True loop.
2. The number will be given by the tutor during the tutorial.
3. For this step, input validation is required to make sure the input is a number rather than a string. A new round of input and checking must start when the previous checking is finished.
4. You will get scores of Tasks 1, 2, and 3 if your solution satisfies the requirements of Task 3.
"""



############### IMPORTANT NOTICE ##################
# When checking your solution, please inform the tutor which task you have completed.
# Then, you can comment out the programs of other tasks, and only demonstrate the solution of ONE task to the tutor.

# If all the tasks are finished, you can remove the codes of Tasks 1 and 2, and only show your solution of Task 3 to the tutor. You will get scores for Tasks 1, 2, and 3 if your solution for Task 3 is fully correct.
# If only tasks 1 and 2 are finished, you can remove the codes of Tasks 1 and 3, and only show your solution of Task 2 to the tutor. You will get scores for Tasks 1 and 2 if your solution for Task 2 is fully correct.
# If only task 1 is finished, you can remove the codes if Tasks 2 and 3, and only show your solution of Task 1 to the tutor. You will get score for Task 1 if your solution for Task 1 is fully correct.

