#1
zander = float(input("How is the length of your zander?"))
if zander < 42:
    print("You must release the fish back into the lake. Your zander must be 42cm or more.")
else:
    print("Every thing is ok, you can go.")

#2
cabin = input("What is your cabin class?")
if cabin == "LUX" or cabin =="lux":
    print("Cabin class description : upper-deck cabin with a balcony")
elif cabin == "A" or cabin == "a":
    print("Cabin class description : above the car deck, equipped with a window")
elif cabin == "B" or cabin == "b":
    print("Cabin class description : windowless cabin above the car deck")
elif cabin == "C" or cabin =="c":
    print("Cabin class description : windowless cabin below the car deck")
else:
    print("Invalid cabin class")

#3
fe_ma = input("What is your gender?")
if fe_ma == "FEMALE":
    ask = float(input("What are the value of your biological?"))
    if 117 <= ask <= 155:
        print("You're okay")
    else:
        print("Go to the hospital now.")
else:
    ask1 = float(input("What are the value of your biological?"))
    if 134 <= ask1 <= 167:
        print("You're okay")
    else:
        print("Go to the hospital now.")

#4
i = int(input("Enter year"))
if i % 4 == 0 and (i % 100 == 0 and i % 400 == 0):
    print("This year is a leap year")
else:
    print("This year is not a leap year")



