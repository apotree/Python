# 구글 번역기 모듈을 이용한 번역 프로그램
import webbrowser # PC에 기본으로 설정된 브라우저 이용

url = "https://papago.naver.com/"

webbrowser.open(url) # url 링크 열기

############################################

import webbrowser

strText = ""; intext = "";

while True:
    print("> ", end="")
    intext = input() # 번역할 말 적기
    if intext == "끝": # 만약 끝 이라는 말을 적으면 멈추고 다음 코드 실행
        break
    strText = strText + "%0A" + intext

url = "https://papago.naver.com/?sk=ko&tk=fr&hn=0&st=" + strText # 한국어를 프랑스어로 번역하는 파파고 사이트 오픈
webbrowser.open(url)
