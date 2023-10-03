from geopy.distance import geodesic
import mysql.connector
connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)
def distance(ident):
    sql="select latitude_deg,longitude_deg from airport"
    sql=sql+" Where ident='" + ident+ "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    a=result
    if cursor.rowcount > 0:
        for row in result:
            print(f"the latitude is {row[0]} and the longtitude is {row[1]}")
    return a

user_a=input("enter ICAO")
distance(user_a)
def distance_2(ident):
    sql="select latitude_deg,longitude_deg from airport"
    sql=sql+" Where ident='" + ident+ "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    b=result
    if cursor.rowcount > 0:
        for row in result:
            print(f"the latitude is {row[0]} and the longtitude is {row[1]}")
    return b
user_b=input("enter ICAO")
distance_2(user_b)

result_a=distance(user_a)
result_b=distance(user_b)
print(f"total distance is : ",geodesic(result_a,result_b).km)