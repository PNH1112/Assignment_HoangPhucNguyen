import os

import sys
from dbconfig import config
# from geopy.distance import geodesic as GD
connection = config.connection


# to import module from different direcotry,
#set the root folder as the source folder
# we need to need add __init__.py in the modules that we want to import from
# as well as in root model, so that python know which module and its directory to travel

def getICAO():
    ICAO = input("Type ICAO code: ").upper()
    return ICAO
def getAirportByICAO(ICAO):
    sql = "SELECT ident, name, municipality FROM airport"
    sql += " WHERE ident ='" +ICAO+ "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(result)
    # if cursor.rowcount > 0:
    #     for index, row in enumerate(result, start=1) :
    #         print (f"{index}.  {row[0]} -- {row[1]} -- {row[2]} -- {")
    # else:
    #     print(f"There is no airport with ICAO: {ICAO}")
    return result

def main():
    while True:
        ICAO = getICAO()
        getAirportByICAO(ICAO)


if __name__ == "__main__":
    main()