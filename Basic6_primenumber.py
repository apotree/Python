# 소수를 구하는 방법

n = int(input("어떤 수를 판별할까요? >> "))
success = True
print(type(success))

t = 2
while t < n:
    if n % t == 0:
        success = False
        break
    t += 1  # = t = t+1

if success == True:
    print("%d는 소수 입니다" % n)
else:
    print("%d는 소수가 아닙니다." % n)
    
###########################################3

n = int(input("어떤 수를 판별할까요? >> "))

for t in range(2, n, 1):
    if n % t == 0:
        print("%d은 %d로도 나누어지므로 소수가 아니다" % (n, t))
        break
    else:
        print("%d는 소수입니다." % n)
        print("1과 자기자신 %d로만 나누어집니다.")
