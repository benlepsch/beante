from tkinter import *

def getFileValue():
    return text.get('1.0', 'end-1c')

root = Tk()
root.title('bean text editor')

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text = Text(root, wrap=NONE, yscrollcommand=scroll.set)
text.pack(side=LEFT, expand=1, fill='both')

scroll.config(command=text.yview)

root.mainloop()