# 좋아하는 수를 입력하시오: 4
# 또 좋아하는 수를 입력하시오: 5
# 4와 5의 합은 9 입니다.

a = input("좋아하는 수를 입력하시오:")
b = input("또 좋아하는 수를 입력하시오:")
c = int(a) + int(b)

# print(a + "와 " + b + "의 합은" + str(c) + "입니다.")
print("{}와 {}의 합은 {}입니다.".format(a,b,c))

