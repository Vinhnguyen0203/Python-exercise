import random
def main():
    a=0
    random_number=random.randint(1,6)
while True:
        result=random_number
        print(f"the time{a} is {result}")
        a=a+1
        if result==6:
            break
main()