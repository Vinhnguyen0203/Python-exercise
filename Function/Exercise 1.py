import random
a=0
user=int(input("type the number roll to dice"))
def random_number():
    number_random=random.randint(1,user)
    return number_random
while True:
    a=a+1
    result=random_number()
    print(f"roll {a} is {result}")
    if result==user:
        break