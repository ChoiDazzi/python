from random import random
arr = [
    1,2,3,4,5, 6,7,8,9,10,
    11,12,13,14,15, 16,17,18,19,20,
    21,22,23,24,25, 26,27,28,29,30,
    31,32,33,34,35, 36,37,38,39,40,
    41,42,43,44,45
    ]

a = arr.pop(int(random()*len(arr)))
b = arr.pop(int(random()*len(arr)))
c = arr.pop(int(random()*len(arr)))
d = arr.pop(int(random()*len(arr)))
e = arr.pop(int(random()*len(arr)))
f = arr.pop(int(random()*len(arr)))

print("로또번호: ",a,b,c,d,e,f)
print(arr)