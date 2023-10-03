import random
user=int(input("how many dice to roll"))
amount=[]
amount.append(user)
n=1
sum = 0
b = []
total=0
while n<=user:
    randomnumber=random.randint(1,6)
 #b = [3,4,5]
    print ("dice:", randomnumber)
    n=n+1
    b.append(randomnumber)
print(b)
for index in b:
    total=total+index
print(f"newtotal:{total}")



