city=[]
user=input("please enter five cities")
while user!="":
    city.append(user)
    user = input("please enter five cities")
for index,i in enumerate(city,start=1):
    print(index,i)