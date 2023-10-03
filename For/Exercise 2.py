numbers=[]
users=input("enter your value :")
while users!="":
    users=float(users)
    numbers.append(users)
    users = input("enter your value :")
print(sorted(numbers,reverse=True))