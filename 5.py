
#1
import random
di=[]
sum = 0
total_dice = int(input("How many dice do you want to roll? "))
for i in range (total_dice):
    dice = random.randint(1,6)
    sum += dice
    di.append(dice)
print(di)
print(sum)

#2
list = []
number = input("Enter your number: ")
while number != "":
    number = input("Enter your number: ")
    if number == "":
        break
    numb = float(number)
    list.append(numb)
list.sort(reverse=True)
print(list[:5])

#3
number = int(input("Enter your number: "))
numb = 1
count = 0
for i in range (2, number):
    if number % i == 0:
        count += 1
if count != 0 or number == 1:
    print("This is not a prime number")
else:
    print("This is a prime numnber")

#4
list_city = []
city = input("Enter your city's name: ")
list_city.append(city)
for i in list_city:
    city = input("Enter your city's name: ")
    if city == "":
        break
    list_city.append(city)
for a,b in enumerate(list_city, start=1):
    print(f"{a}.{b}")
