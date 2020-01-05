from tkinter import*  # 윈도우 위젯을 지원하는 라이브러리

window = Tk()
window.title("hello")
window.geometry("500x300")


button = Button(window, text="창 닫기", fg="red", command=quit)

button.pack()

window.mainloop()

