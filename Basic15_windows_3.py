from tkinter import*  # 윈도우 위젯을 지원하는 라이브러리

window = Tk()
window.title("이미지 지원")
window.geometry("500x300")

photo = PhotoImage(file="image.png")
label = Label(window, image=photo)

label.pack()

window.mainloop()

