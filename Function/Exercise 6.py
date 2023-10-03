def first_pizza(first_diameter,first_price):
    radius=(first_diameter/2)*0.01
    Area=3.14*(radius**2)
    result=first_price/Area
    return result
diameter = float(input("enter the first diameter"))
price = float(input("enter the first price"))
print(f"the unit price of first pizza is {first_pizza(diameter,price)}")

diameter_2=float(input("enter the second diameter"))
price_2 = float(input("enter the second price"))
print(f"the unit price of second pizza is {first_pizza(diameter_2,price_2)}")

if first_pizza(diameter,price) > first_pizza(diameter_2,price_2):
    print("you should buy second pizza")
elif first_pizza(diameter,price)<first_pizza(diameter_2,price_2):
    print("you should buy first pizza")
else:
    print("equal")