# Assignments: Dive Deeper

# 1. Decisions at the Crossroad

# number = input("Enter a number: ")

# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

number = input("Enter a number: ")

if int(number) > 0:
    print("The number is positive.")
elif int(number) == 0:
    print("The number is zero.")
else:
    int(number) < 0
    print("The number is negative.")

# 2. The Greatest Showdown
# Task 1: Identify the Greatest

num_1, num_2, num_3 = int(input("Enter first number:\n")), int(input("Enter second number:\n")), int(input("Enter third number:\n"))

if num_1 >= num_2 and num_3:
    print(f"The largest number is {num_1} ")
elif num_2 >= num_1 and num_3:
    print(f"The largest number is {num_2} ")
else:
    print(f"The largest number is {num_3}")  