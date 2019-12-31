name = "test"
classid = "20190930"

print("name : ", name)
print("Class ID : ", classid)

###################################

#number = input("number IN : ")
#number = int(number)

number = int(input("Number IN : "))

if number >= 100:
    print("100 over")
else:
    print("100 under")
    
print("%d * %d = %d" % (9,2,9*2))

####################################

total = 95
grade = 4.5

print("총점 : ", total)
print("평균 : ", grade)
print("총점 : %d 평균 : %f" % (total, grade))
print("총점 : %d 평균 : %.2f" % (total, grade))

