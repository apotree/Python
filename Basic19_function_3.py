def func1():
    a = 10  # func1 에서만 적용되는 지역변수(Local variable)
    print('func1() a = ', a)
    a = 10 + 20
    print('func01 a = ', a)

def func2():
    print('func2() a = ', a)

a = 100  # 전역변수

func1()
func2()
