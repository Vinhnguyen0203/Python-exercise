user=int(input("enter the value"))
number=0
for i in range(1,user):
    if user%i==0:
        number+=1
    else:
        number=number
if number==1:
    print("this is prime number")
else:
    print("not prime number")