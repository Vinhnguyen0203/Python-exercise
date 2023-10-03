season=("Spring","Summer","Autumn","Winter")
def main():
    for x in season:
        user = int(input("a number of a month( December is a first month of winter)"))
        if 3<=user<=5:
            print(season[0])
            break
        elif 6<=user<=8:
            print(season[1])
            break
        elif  9<=user<=11:
            print(season[2])
            break
        else:
            print(season[3])
            break
main()