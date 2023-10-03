mylist=[1,3,5,6,42,55,64,63,62,93,41]
def biggame(first):
    for i in first:
        print("the first version is",first)
        return
def giantgame():
    for a in mylist:
        if a%2!=0:
            print(a,end=' ')

biggame(mylist)
giantgame()