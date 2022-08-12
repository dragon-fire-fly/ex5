###### Exercise 5 #######

#---- Task 1 ----#

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if num1 == num2 == num3:
    triple = (num1 + num2 + num3) * 3
    print(f"The triple sum is: {triple}")
else:
    sum = num1 + num2 + num3
    print(f"The sum is: {sum}")

#---- Task 2 ---- #

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if num1 > num2:
    calc1 = (num1 - num2) * 2
    print(f"The result of the calculation is {calc1}")
else:
    calc2 = abs(num1-num2)
    print(f"The result of the calculation is {calc2}")

#---- Task 3 ----#
 #Already completed in exercise 1

#---- Task 4 ----#
import math

radius = float(input("Enter youe desired radius: "))
pi = math.pi
# calculation for area is π (Pi) times the radius squared
area = round(pi * (radius * radius), 2)

print(f"The area of the circle with radius {radius} is: {area}")


#---- Task 5 ----#
import random

random_num = random.randint(1,10)
user_correct = False
print(random_num)

while user_correct == False:
    user_guess = int(input("Guess a number between 1-9: "))
    if user_guess == random_num:
        user_correct = True
        print(f"Well guessed! The number was {random_num}")
    else:
        print(f"Sorry, the number is not {user_guess}, please try again!")


#---- Task 6 ----#
# Formula = C/5 = F-32/9

temp_num = int(input("Please choose a temperature you'd like to convert: "))
degrees = input("Degrees C or F? ").lower()

if degrees == "c":
    f_convert = round((temp_num * (9/5)) + 32, 1)
    print(f"{temp_num} degrees C is {f_convert} degrees F")
elif degrees == "f":
    c_convert = round((temp_num - 32) * 5/9, 1)
    print(f"{temp_num} degrees F is {c_convert} degrees C")



#Task 7#

# print("*\n**\n***\n****\n*****\n****\n***\n**\n*")
# size = 7
# for i in range(1,size+1): print("*" * i)
# for i in range(size-1,0,-1): print("*" * i)

# print("*" * i)

# user_stars = int(input("How many lines of stars do you want? "))
# list_of_stars = []
# for star in range(user_stars+1):
#     print(star * "*")
# for star in range(user_stars+1, 0, -1):
#     print(star * "*")

# print(list_of_stars)


## Task 8 ##
fib_list = [0,1]

for number in range(0,51):
    new_number = fib_list[-2] + fib_list[-1]
    fib_list.append(new_number)
print(fib_list)

