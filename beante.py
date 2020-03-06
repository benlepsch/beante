from tkinter import *

def getFileValue():
    return text.get('1.0', 'end-1c')

root = Tk()
root.title('bean text editor')

top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

scroll = Scrollbar(root)
scroll.pack(in_=bottom, side=RIGHT, fill=Y)

button = Button(root, text='toggle dark mode', command=getFileValue)
button.pack(in_=top, side=LEFT)
button2 = Button(root, text='or not', command=getFileValue)
button2.pack(in_=top, side=LEFT)

text = Text(root, wrap=NONE, yscrollcommand=scroll.set)
text.pack(in_=bottom,side=LEFT, expand=1, fill='both')

scroll.config(command=text.yview)

root.mainloop()