# km <-> miles

km = int(1)
miles = float(0.621371)

abc = float(input("킬로미터 단위 거리 입력 : "))

c = abc * miles

print("입력값 :", abc, "km")
print("변환값 :", c, "miles")


###################################

# 키에 적당한 몸무게

you = float(input("키가 몇 cm 입니까? > "))

a = (you - 100) * 0.9
b = a * 1.2
c = a * 0.8

print("당신의 신장 : %.2f" % you , "cm")
print("적정 몸무게 : %.2f" % (a) , "kg")
print("과체중 위험 기준 : %.2f" % (b) , "kg")
print("저체중 위험 기준 : %.2f" % (c) , "kg")
