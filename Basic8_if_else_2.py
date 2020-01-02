# 문자열 판단 가능

userID = "qwer1234"
userPWD = "1234"
inID = str("사용자 ID 입력 : ")
inPWD = str("사용자 PWD 입력 : ")

if inID == userID and inPWD == userPWD:
    print("아이디 일치", inID)
    print("패스워드 일치", inPWD)
else:
    print("아이디 또는 패스워드 불일치")


if inID == userID:
    if inPWD == userPWD:
        print("ID, PWD 일치")
    else:
        print("PWD 불일치")
else:
    print("ID 불일치")
