from tkinter import*  # 윈도우 위젯을 지원하는 라이브러리

window = Tk()
window.title("윈도우 창 연습------")
window.geometry("500x300")
label1 = Label(window, text="window python")
label2 = Label(window, text="hello", font=("궁서체", 30), fg="blue")

label1.pack()
label2.pack()



window.mainloop()

