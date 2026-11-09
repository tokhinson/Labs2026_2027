import tkinter as tk
from generate_key import generate_key
from tkinter import messagebox

def get_key():
    decnum = num_entry.get()
    key = generate_key(decnum)
    if key == '':
        messagebox.showinfo('Ошибка', 'Введите корректное 3-значное десятичное число')
    else:
        messagebox.showinfo('Сгенерированный ключ', f'Ваш ключ: {key}')

window = tk.Tk()
window.title('Fallout keygen')
window.geometry('720x405')
window.resizable(0, 0)
bg_img = tk.PhotoImage(file='photo.png')

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

text_label = tk.Label(window, text='Введите 3-значное десятичное число:', font=('Roboto',25), bg='#000000', fg='#FFFFFF')
text_label.grid(row=0, column=0, padx=1, pady=1)

num_entry = tk.Entry(window, width=10, font=('Roboto', 20), bg='#000000', fg='#FFFFFF')
num_entry.grid(row=0, column=1, padx=1, pady=1)

button1 = tk.Button(window, text='<', font=('Roboto', 20), command=get_key)
button1.grid(row=0, column=2, padx=1, pady=1)

window.mainloop()