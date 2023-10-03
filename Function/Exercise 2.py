import random
a=0
user=int(input("roll the dice"))
def random_number():
    random_number1=random.randint(1,user)
    return random_number1
while True:
    a=a+1
    result=random_number()
    print(f"roll {a} is {result}")
    if result==user:
        break


