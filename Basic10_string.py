# 문자열과 리스트 비교

aa = "Hello world"
# bb = ["H", "e", "l", "o", ]
# [H, e, l, l, o,  , w, o, r, l, d]
#  0  1  2  3  4  5  6  7  8  9  10

print(aa)  # Hello world
print(aa[6])  # w
print(aa[0:5])  # Hello
print(aa[4:])  # 5번쨰 글자 뒤로 다 입력  >  o world

stR = input("문자열을 자유롭게 입력해보세요 > ")
s = int(input("출력할 시작 범위 > "))
e = int(input("출력할 끝 범위 입력 > "))

print(stR[s:e])
