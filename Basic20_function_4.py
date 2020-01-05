def func3(num):
    # 매개변수로 선언된 것도 지역변수 적용됨.
    print('func3() num = ', num)

def func4(n1, n2, n3):
    print('func04() n1, n2, n3 = ', n1, n2, n3)

num = 10
func3(num)
print(num)
