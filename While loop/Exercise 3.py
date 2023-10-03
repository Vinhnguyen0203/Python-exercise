users=input("please enter your value")
largest=float(users)
smallest=float(users)
while users!="":
    users=float(users)
    if users>largest:
        largest=users
    if users<smallest:
        smallest=users
    users = input("please enter your value")
print(largest)
print(smallest)





