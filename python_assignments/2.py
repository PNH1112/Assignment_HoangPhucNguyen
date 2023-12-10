
#1
name = input("What's your name?")
print("Hello,", name)

#2
import math
rad = input("What is radius of circle?")
r = float(rad)
result = math.pi*r**2
print(f"The area of the circle: , {result:2.2f}")

#3
import math
length = input("What is the length of the rectangle?")
l = float(length)
width = input("What is the width of the rectangle?")
w = float(width)
pe = (l+w)*2
print("The perimeter of the rectangle is:", pe)
area = (l*w)
print("The area of the rectangle is:", area)

#4
a = float(input("What is the integer no.1?"))
b = float(input("What is the integer no.2?"))
c = float(input("What is the integer no.3?"))
sum = a+b+c
product = a*b*c
average = (a+b+c)/3
print(f"Sum of those are:, {sum:2.2f}")
print(f"Product of those are:, {product:2.2f}")
print(f"Average of those are:, {average:2.2f}")

#5
ta = float(input("Enter talents"))
po = float(input("Enter pounds"))
lo = float(input("Enter lots"))

ta_to_po = ta*20
po_to_lo = po*32
all_po = ta_to_po + po
all_lots = all_po*32 + lo
gr = all_lots*13.3
kilo = gr//1000
gram = gr % 1000
print("The weight in modern units")
print(f"{kilo} kilograms and, {gram:5.2f} grams")

#6
import random
no = int(input("Choose 3 or 4 digit code?"))
if no == 3:
    code = [random.randint(0, 9) for _ in range(3)]
    print("Here is your 3-digit code", code)
elif no== 4:
    code = [random.randint(1,6) for _ in range(4)]
    print("Here is your 4-digit code", code)
else:
    print("Please input 3 or 4")
