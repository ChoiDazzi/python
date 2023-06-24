def showDan(dan):
    for i in range(1, 9+1):
        res = dan * i
        print("{} * {} = {}".format(dan,i,res))

showDan(7)