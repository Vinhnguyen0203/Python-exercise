import random
guess_number=0
final=random.randint(1,100)
while guess_number!=final:
    guess_number=int(input("please guess the number:"))
    if guess_number>final:
        print("too big")
    elif guess_number<final:
        print("too small")
    else:
        print("correct")
