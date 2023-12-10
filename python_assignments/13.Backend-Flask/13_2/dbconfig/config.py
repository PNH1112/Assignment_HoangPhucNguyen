import mysql.connector


connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3300,
    database = "flight_game",
    user = "root",
    password = "",
    autocommit = True
)