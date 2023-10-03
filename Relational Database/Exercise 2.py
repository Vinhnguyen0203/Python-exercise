import mysql.connector
connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)
def airport(iso_country):
    sql="select name from airport"
    sql=sql+ " Where iso_country='"+ iso_country +" '"+"order by type "
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"the name of airport {row[0]}")
    return

user=input("enter area code:")
airport(user)
