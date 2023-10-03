
#1
import random
import mysql.connector
from geopy.distance import geodesic
connection = mysql.connector.connect(
        host='127.0.0.1',
        port = 3306,
        user = 'root',
        password='Giakhang2018@',
        database='flight_game',
)
cursor = connection.cursor()

player_1 = input("Hi player1, enter your nickname: ")
player_2 = input("Hi player2, enter your nickname: ")
ICAO = {0:"LPPT",
1:"LEMD",
2:"LFML",
3:"LIMC",
4:"LOWW",
5:"LZKZ",
6:"UKBB",
7:"UMMS",
8:"EVRA",
9:"EETN",
10:"ULLI",
11:"EFHK"}

map1 = ["PORTUGAL","SPAIN","FRANCE","ITALIA","AUSTRIA","SLOVAKIA","UKRAINE","BELARUS","LATVIA","ESTONIA","RUSSIA","FINLAND"]
map2 = ["PORTUGAL","SPAIN","FRANCE","ITALIA","AUSTRIA","SLOVAKIA","UKRAINE","BELARUS","LATVIA","ESTONIA","RUSSIA","FINLAND"]


print("Let the race begin! Starting from Portugal, the first to reach Finland will claim victory.")



move1 = 0
move2 = 0
def game_road1():
    sql = f'select latitude_deg, longitude_deg,name from airport where ident = %s'
    cursor.execute(sql,(ICAO[move1],))
    row = cursor.fetchall()

    sql2 = f'select latitude_deg, longitude_deg,name from airport where ident = %s'
    cursor.execute(sql2, (ICAO[move1 + 1],))
    row2 = cursor.fetchall()


    for la1, lo1,i1 in row:
        location1 = (la1,lo1)
    for la2, lo2,i2 in row2:
        location2 = (la2,lo2)
    distance1 = geodesic(location1, location2).kilometers
    print(f"{distance1:.0f} km from +++{i1}+++ to +++{i2}+++")
    return distance1

def game_road2():
    sql = f'select latitude_deg, longitude_deg, name from airport where ident = %s'
    cursor.execute(sql,(ICAO[move2],))
    row = cursor.fetchall()

    sql2 = f'select latitude_deg, longitude_deg, name from airport where ident = %s'
    cursor.execute(sql2, (ICAO[move2 + 1],))
    row2 = cursor.fetchall()

    if len(row) == 0 or len(row2) == 0:
        print("There are no results for this ")
    else:
        for la1, lo1,i1 in row:
            location1 = (la1,lo1)
        for la2, lo2,i2 in row2:
            location2 = (la2,lo2)
        distance2 = geodesic(location1, location2).kilometers
        print(f"{distance2:.0f} km from +++{i1}+++ to +++{i2}+++")
    return distance2

p1_co2_budget = []
p2_co2_budget = []
while True:
    if move1 == 11 or move2 == 11:
        break

    ask1 = input(f"+++{player_1}, enter to roll.")
    if ask1 == "":
        player1_dice = random.randint(1, 6)
        print(f"Dice: {player1_dice}")
        p1_co2_unit = player1_dice * 100
        p1_co2_budget.append(p1_co2_unit)
        co2_budget_1 = sum(p1_co2_budget)
        print(f"Total fuel that {player_1} have: {p1_co2_unit} CO2 Unit")
        co2_left_1 = co2_budget_1 - game_road1()
        if co2_budget_1 - game_road1() > 0:
            move1 += 1
            print(f"{player_1} flight to next airport: {map1[move1]} ")
            print("")
            p1_co2_budget.remove(co2_budget_1)
            p1_co2_budget.append(co2_left_1)
            print(f"{player_1}'s CO2 UNIT left: {co2_left_1:.0f}")
        else:
            print(f"{player_1} doesn't have enough fuel, standstill for one turn and add {p1_co2_unit} co2 Unit")
            p1_co2_budget.append(p1_co2_unit)
            print("")
    else:
        print(f"Wrong input! {player_1} lost 1 turn!")
    print(f"{player_1}'s CO2 UNIT left: {co2_budget_1:.0f}")

    ask2 = input(f"+++{player_2}, enter to roll.")
    if ask2 == "":
        player2_dice = random.randint(1, 6)
        print(f"Dice: {player2_dice}")
        p2_co2_unit = player2_dice * 100
        p2_co2_budget.append(p2_co2_unit)
        co2_budget_2 = sum(p2_co2_budget)
        print(f"Total fuel that {player_2} have: {p2_co2_unit} CO2 Unit")
        if co2_budget_2 - game_road2() > 0:
            move2 += 1
            print(f"{player_2} flight to next airport: {map2[move2]} ")
            print("")
            co2_left_2 = f"{co2_budget_2 - game_road2()}.0f"
            p2_co2_budget.remove(co2_budget_2)
            p2_co2_budget.append(co2_left_2)
            print(f"{player_2}'s CO2 UNIT left: {co2_left_2:.0f}")
        else:
            print(f"{player_2} doesn't have enough fuel, standstill for one turn and add {p2_co2_unit} co2 Unit")
            p2_co2_budget.append(p2_co2_unit)
            print("")
    else:
        print(f"Wrong input! {player_1} lost 1 turn!")
    print(f"{player_2}'s CO2 UNIT left: {co2_budget_2}")

if move1 == 11:
    print(f"Congratulation {player_1}, you are the WINNER!")
elif move2 == 11:
    print(f"Congratulation {player_2}, you are the WINNER!")
elif move1 == move2:
    print(f"Both {player_1} and {player_2} are the WINNER!")

