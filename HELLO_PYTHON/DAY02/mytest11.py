# 첫 수를 입력하세요. 7  9
# 끝 수를 입력하세요. 9  7
# 7 은 9보다 2만큼 작다.
# 9 은 7보다 2만큼 크다.
# 같은 숫자입니다.

a = int(input("첫 수를 입력하세요."))
b = int(input("끝 수를 입력하세요."))

if(a > b):
    res = a - b
    print("{}은(는) {}보다 {}만큼 크다".format(a,b,res))
elif (a < b):
    res = b - a
    print("{}은(는) {}보다 {}만큼 작다".format(a,b,res))
else :
    print("같은 숫자입니다.")