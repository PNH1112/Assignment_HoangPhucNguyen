
#1`
import random
def all():
    dice = random.randint(1, 6)
    list = []
    while True:
        dice = random.randint(1, 6)
        list.append(dice)
        if dice ==6:
            break
    print(list)
    return list
all()

#2
import random
def maxdice():
    max = int(input("Enter the number of sides: "))
    list = []
    while True:
        dice = random.randint(1, max)
        list.append(dice)
        if dice == max:
            break
    print(list)
    return list
maxdice()

#6.3
def gasoline(lit):
    gallon = lit*3.78541
    return gallon
while True:
    lit = int(input("Enter your lit to convert to gallon: "))
    if lit < 0 :
        break
    print(f"{lit} littes conver to {gasoline(lit)} gallons")

#4
def sumlist():
    total = sum(list_number)
    return total
list_number = []
while True:
    number = int(input("Enter your number(negative to quit): "))
    if number <0 :
        break
    else:
        list_number.append(number)
print(f"Sum of all number have been inputed: {sumlist()}")

#5
def list_all():
    for i in list_original:
        if i % 2 == 0:
            list_even.append(i)
    return list_even
list_original=[]
list_even=[]
while True:
    number = int(input("Enter your number(negative to quit): "))
    if number < 0:
        break
    else:
        list_original.append(number)
print(f"All number have been inputed: {list_original}")
print(f"Even number: {list_all()}")
#6
#d is the diameter of the pizza(cm)
#p is the price of the pizza
#u is the unit of the pizza(price/m^2)
import math
def pizza(d,p):
    r = (d/2)/100
    s = math.pi*r*r
    u = p/s
    return u
pizza1 = pizza(30,10)
pizza2 = pizza(29,8.8)
if pizza1 < pizza2:
    print(f"the unit price of pizza 1 is ({pizza1:.2f}) lower than the unit price of pizza 2 ({pizza2:.2f})")
elif pizza2 < pizza1:
    print(f"the unit price of pizza 2 is ({pizza2:.2f}) lower than the unit price of pizza 1 ({pizza1:.2f})")
else:
    print("the unit price of 2 pizzas is the same")

