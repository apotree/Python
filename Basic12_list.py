aa = []
for i in range(0, 4):
    aa.append(0)
sum = 0

for i in range(0, 4):
    aa[i] = int(input(str(i + 1) + "번째 숫자 : "))

sum = aa[0] + aa[1] + aa[3]
print("총합 : ", sum)
