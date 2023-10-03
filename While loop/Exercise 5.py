username=input("username:")
password=input("password:")
python=0
while python<5 :
    python=python + 1
    if username=="python" and password=="rules":
        print("welcome")
        break
    elif username!="python" or password!="rules":
        print("nhap lai di ma")
        username = input("username:")
        password = input("password:")
if python==5 :
    print("dined")

