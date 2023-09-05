
#1
number = 1
while 1 <= number <= 1000:
    number += 1
    if number % 3 == 0:
        print(f"the number {number} is devided by 3")

#2
inch = int(input("Input inch to convert"))
while inch >= 0:
    cm = inch * 2.54
    print("Here is the convert's result: ", cm)
    inch = int(input("Input inch to convert"))
print("Negative number detected")

#3
no = []
while True:
    number = input("Enter your number")
    if number == "":
        break
    no.append(float(number))

l = max(no)
s = min(no)
print("Largest number: ", l)
print("Smallest number: ", s)

#4
import random
number = int(input("What is your number? "))
ran_no = random.randint(1, 10)

while ran_no != number:
    if ran_no < number:
        print("Too high")
        number = int(input("Guess again"))
    elif number < ran_no:
        print("Too low")
        number = int(input("Guess again"))
    else:
        print("Invalid number, please input number from 1 to 10")
        number = int(input("Input again"))
print("Hooray, you found it")

#5
user = "python"
password = "rules"
count = 0
while count < 5:
    count += 1
    us = input("Please enter your user name")
    pw = input("Enter your password")
    if us == user and pw == password:
        print("Welcome, python")
        break
    elif us != user or pw != password:
        print("Wrong credentials, you have" , (5-count), "times less")
if count == 5:
    print("Access is denied.")

#6
import random
N = int(input("Enter your number of total points: "))
n = 0

for _ in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    point_inside = x**2 + y**2
    if point_inside < 1:
        n += 1
print("Total points inside the circle: ", n)
pi_number = (4*n)/N
print("Pi number is: ", pi_number)





