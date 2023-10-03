user=int(input("enter the volume in gallons: "))
def gallon():
    value_gallon=3.785411784
    return value_gallon

while user>0:
    liter=user*gallon()
    print(f"Converting {user} gallon into liters is {liter}")
    user = int(input("enter the volume in gallons: "))
if user<0:
    print("nhap sai r ma")