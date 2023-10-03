mylist=[]
user=input("add anything else: ")
def total():
    a=0
    for i in mylist:
        a=a+i
    print(f"the sum of the list is {a}")
    return a
while str(user)!="":
    user=float(user)
    mylist.append(user)
    user = input("add anything else: ")
total()