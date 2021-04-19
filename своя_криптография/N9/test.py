from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('test')

nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')

frame = Frame(root)

f1 = Text(frame)
f2 = Text(frame)
f3 = Text(frame)

nb.add(frame, text='page1')
nb.add(f2, text='page2')
nb.add(f3, text='page3')

root.mainloop()