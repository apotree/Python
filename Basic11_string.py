# 문자열 변경 -> replace()

ss = " 열심히 파이썬 공부 중@@ "

res = ss.replace('파이썬', "Python")

print(res)


# 문자열 분리 및 결합 , split(), splitles(), join()

ss = "하나 둘 셋"
res = ss.split()
print(res)

ss = "하나\n둘\n셋"
res = ss.splitlines()
print(res)

ss = "%"
res = ss.join("파이썬")
print(res)
