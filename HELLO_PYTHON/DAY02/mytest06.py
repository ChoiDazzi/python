# 1 ~ 9 까지 수 중에서 중복 없이 섞어서 3개의 수를 출력 하세요 
from random import random
from anaconda_project.internal.conda_api import remove
arr = [1,2,3,4,5,6,7,8,9]

for i in range(99):
    r = int(random() * 9)
    a = arr[0]
    arr[0] = arr[r]
    arr[r] = a
print(arr[0],arr[1],arr[2])

# temp = int(random() * 9);
#
# for i in arr:
#     b = temp 
#     arr.insert(i, b)
#     arr.remove(i)
#     arr.insert(b,i)
#     arr.remove(b)
#
# a = str(arr.pop(1))
# b = str(arr.pop(2))
# c = str(arr.pop(3))
#
# print(a+", "+b+", "+c)
