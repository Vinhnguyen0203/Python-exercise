years=int(input("please enter the year"))
if years%4 and years%100 or years%400 :
    print("this year is leap year")
else:
    print("this is not leap year")