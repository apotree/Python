letter = input("입력 : ")
encode = ""

for ch in letter:
    num = ord(ch)
    encode = encode + chr(num + 1)

print("원문 :", letter)
print("암호 :", encode)

encode2 = ""

for ch in encode:
    num = ord(ch)
    encode2 = encode2 + chr(num - 1)

print("원문 :", encode2)

####################################

let1 = "A"
res1 = ord(let1)
res1 = res1 + 32
print(chr(res1))

let2 = "a"
res2 = ord(let2)
res2 = res2 - 32
print(chr(res2))

inChar = input("문자를 입력 : ")
inChar = inChar.upper()
print (inChar)

inChar = input("문자를 입력 : ")
inChar = inChar.lower()
print(inChar)

inChar = input("대문자로 된 단어 입력 : ")
inChar = inChar.lower()
print(inChar)
