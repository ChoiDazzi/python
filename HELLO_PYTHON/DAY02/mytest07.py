# 홀/짝 을 선택하세요. 홀
# 나: 홀
# 컴: 홀 
# 결과: 승리 
from random import random

a = input("홀/짝 을 선택하세요.")
rnd = random()

if(rnd > 0.5) :
    com = "홀"
else  :
    com = "짝"

if(a == com): 
    res = "승리"
else: 
    res = "패배"
     
print("나:" + a)
print("컴:" + com)
print("결과:" + res)
