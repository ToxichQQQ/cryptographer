import hashlib
from tkinter import *

root = Tk()

def createHash():
   text = input.get()

   text_sha1 = hashlib.sha1(text.encode('utf-8'))
   result = text_sha1.hexdigest()

   finalText['text'] = f'{result}'


root['bg'] = '#fff'
root.title('Hash Program')
root.geometry('500x500')

root.resizable(width=False,height=False)

canvas = Canvas(root,height = 500, width = 500)
canvas.pack()

frame = Frame(root)
frame.place(rely=0.15,relwidth = 1.0,relheight = 0.25)

frameBottom = Frame(root)
frameBottom.place(rely=0.55,relwidth = 1.0,relheight = 0.3)

title = Label(frame,text = 'Введите текст',font=32)
title.pack()

input = Entry(frame,bg='white',font=32)
input.pack()

btn = Button(frame, text = 'Создать хеш',bg='#fff',command=createHash)
btn.pack()


title = Label(frameBottom,text = 'Хеш',font=32)
title.pack()

finalText = Label(frameBottom,font=32)
finalText.pack()




root.mainloop()


