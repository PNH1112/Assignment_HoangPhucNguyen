
#1
season = ("Srping","Summer","Autumn","Winter")
month = int(input("Enter your number of a month: "))
def season_in_year():
    for number in season:
        if month == 12 or 1<= month <=2:
            return season[3]
        elif 3 <= month <= 5:
            return season[0]
        elif 6 <= month <= 8:
            return season[1]
        elif 9 <= month <= 11:
            return season[2]
        else:
            print("Invalid number")
season1 = season_in_year()
print(f"Month {month} is {season1}")

#2
set1 = set()
def list_of_name():
    while True:
        name = input("Enter your name: ")
        if name == "":
            break
        if name in set1:
            print("Existing name")
        else:
            print("New name")
        if name != "":
            set1.add(name)

    print(set1)
print1 = list_of_name()

#3
airport = {
    "EFAA": "Aavahelukka",
    "EFAH": "Ahmosuo Airport",
    "EFAL": "Alavus Airfield",
    "EFEJ": "Jorvin Hospital Heliport"
}
def choose(airport):
    while True:
        user_input = input("Choose new, fetch, or quit: ").lower()
        if user_input == "quit":
            print("Thank you & Goodbye")
            break
        elif user_input == "new":
            ICAO = input("Enter ICAO of the airport: ")
            name = input("Enter name of the airport: ")
            airport[ICAO] = name
        elif user_input == "fetch":
            ask_user = input("Enter the ICAO here: ")
            if ask_user in airport:
                print(f"{ask_user}: {airport[ask_user]}")
            else:
                print("ICAO not found.")
        else:
            print("Invalid input")
choose(airport)
