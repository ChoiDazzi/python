# 1 ~ 45 까지 수 중에서 로또 만드세요.
# range 함수로 바꾸세요.

from random import random
# arr = [] 
# for i in range(1, 45+1):
#     arr.append(i)

# 왜냐햐면 range는 함수
arr = list(range(1,45+1))

for i in range(1000):
    r = int(random() * 45)
    a = arr[0]
    arr[0] = arr[r]
    arr[r] = a

print(arr[0:6])