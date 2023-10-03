import mysql.connector
connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)
def nameandlocation(ident):
 #  select name,municipality from airport where ident="18LS"
# nameandlocation()
    sql = "select name,municipality from airport"
    sql = sql + " where ident='"+ ident + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"the name is {row[0]} and the location is {row[1]}")
    return
user=input("enter ICAO: ")
nameandlocation(user)