from random import random

def getStrike(com,mine):
    ret = 0
    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]

    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]
    
    if c1 == m1:
        ret += 1
    if c2 == m2:
        ret += 1
    if c3 == m3:
        ret += 1
         
    return ret;

def getBall(com,mine):
    ret = 0
    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]

    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]
    
    if c1 == m2 or c1 == m3:
        ret += 1
    if c2 == m1 or c2 == m3:
        ret += 1
    if c3 == m1 or c3 == m2:
        ret += 1
    return ret;

def ranCom():
    arr = ["1","2","3","4","5","6","7","8","9"]
    
    for i in range(100):
        r = int(random() * 9)
        a = arr[0]
        arr[0] = arr[r]
        arr[r] = a
        
    res = arr[0] + arr[1] + arr[2]
    print("com: ",res)
    return res
 
com = ranCom()

while True:
    mine = input("수를 입력하세요.")
    s = getStrike(com,mine)
    b = getBall(com,mine)

    print(mine,"\t","s",s,"b",b);
    
    if s == 3:
        print(mine + "를 맞췄습니다.")
        break