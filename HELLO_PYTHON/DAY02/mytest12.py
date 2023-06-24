# 가위바위보 중 하나를 입력하세요. 가위 
# 나: 가위 
# 컴: 보 
# 결과: 승리
from random import random

a = input("가위바위보 중 하나를 입력하세요.")
rnd = random()

if(rnd <  0.33):
    com = "가위"
    if(a == "가위"):
        res = "비김"
    elif(a == "바위"):
        res = "승리"
    else:
        res = "패배"
if(0.33 <= rnd <  0.66):
    com = "바위"
    if(a == "가위"):
        res = "패배"
    elif(a == "바위"):
        res = "비김"
    else:
        res = "승리"
if(0.66 <= rnd <  0.99):
    com = "보"
    if(a == "가위"):
        res = "승리"
    elif(a == "바위"):
        res = "패배"
    else:
        res = "비김"
        
print("나: " + str(a))
print("컴: " + com)
print("결과: "+ res)
