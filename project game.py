
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
        print(f"{map1[move1]}'s airport is : {i1}")
    for la2, lo2,i2 in row2:
        location2 = (la2,lo2)
        print(f"{map1[move1 +1]}'s airport is : {i2}")
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
            print(f"{map2[move2]}'s airport is : {i1}")
        for la2, lo2,i2 in row2:
            print(f"{map2[move2 +1]}'s airport is : {i2}")
            location2 = (la2,lo2)
        distance2 = geodesic(location1, location2).kilometers
        print(f"{distance2:.0f} km from +++{i1}+++ to +++{i2}+++")
    return distance2


while True:
    if move1 == 11 or move2 == 11:
        break

    ask1 = input(f"+++{player_1}, enter to roll.")
    if ask1 == "":
        player1_dice1 = random.randint(1, 6)
        player1_dice2 = random.randint(1, 6)
        print(f"Dice 1: {player1_dice1}")
        print(f"Dice 2: {player1_dice2}")
        print(f"Sum of 2 dices : {(player1_dice1 + player1_dice2)}")
        km1 = (player1_dice1 + player1_dice2) * 100
        print(f"Total fuel that {player_1} have: {km1} CO2 Unit")
        if game_road1() - km1 < 0:
            move1 += 1
            print(f"{player_1} flight to next airport: {map1[move1]} ")
            print("")
        else:
            print(f"{player_1} doesn't have enough fuel, standstill for one turn")
            print("")
    else:
        print(f"Wrong input! {player_1} lost 1 turn!")

    ask2 = input(f"+++{player_2}, enter to roll: ")
    if ask2 == "":
        player2_dice1 = random.randint(1, 6)
        player2_dice2 = random.randint(1, 6)
        print(f"Dice 1: {player2_dice1}")
        print(f"Dice 2: {player2_dice2}")
        print(f"Sum of 2 dices : {(player2_dice1 + player2_dice2)}")
        km2 = (player2_dice1 + player2_dice2) * 100
        print(f"Total fuel that {player_2} have: {km2} CO2 Unit")
        if game_road2() - km2 < 0:
            move2 += 1
            print(f"{player_2} flight to next airport: {map2[move2]} ")
            print("")
        else:
            print(f"{player_2} doesn't have enough fuel, standstill for one turn")
            print("")
    else:
        print(f"Wrong input! {player_2} lost 1 turn!")

if move1 == 11:
    print(f"Congratulation {player_1}, you are the WINNER!")
elif move2 == 11:
    print(f"Congratulation {player_2}, you are the WINNER!")
elif move1 == move2:
    print(f"Both {player_1} and {player_2} are the WINNER!")

