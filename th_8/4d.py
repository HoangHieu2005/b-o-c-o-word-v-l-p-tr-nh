print("Nguyễn Bá Hoàng Hiếu")
print("235752021610036")

import tkinter as tk

def thay_doi_mau():
    button.config(bg="green", fg="white")

window = tk.Tk()
window.title("Thay đổi màu nút")

button = tk.Button(window, text="Nhấn vào đây", command=thay_doi_mau)
button.pack()

window.mainloop()
