def radiusIn():
    radius = float(input("반지름 입력 >> "))
    return radius

def proceCircle(radius, PI):
    circleArea = radius * radius * PI
    return circleArea

def ptrCircle(radius, circleArea):
    print("반지름이 %.5f인 경우는 " % radius)
    print("원의 넓이가 %.50f 이다." % circleArea)

def main():
    PI = 3.14159265
    radius = radiusIn()
    circleArea = proceCircle(radius, PI)
    ptrCircle(radius, circleArea)


main()
