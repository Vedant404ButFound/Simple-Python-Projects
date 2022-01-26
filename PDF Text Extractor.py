import PyPDF2
from tkinter.filedialog import askopenfilename,askdirectory
import tkinter.messagebox as tmsg
from tkinter import *
import os
root = Tk()
root.geometry('1x1+0+0')
pdf = PyPDF2.PdfFileReader(askopenfilename(filetypes=[('PDF Files','*.pdf'),('Text Files','*.txt')],initialdir=os.getcwd()))
root.destroy()
root.mainloop()
try:
    startPage = int(input('Enter Starting Page : \n'))
    endPage = int(input('Enter Ending Page : \n'))
    txtFile = input('Text File Name : \n')
except:
    print('Error!')
a = ''
root2 = Tk()
root2.geometry('0x0+0+0')
path = askdirectory(initialdir=os.getcwd())
root2.destroy()
root2.mainloop()
for i in range(startPage,endPage+1):
    a = a + f'\nPage No.{i}\n'+ pdf.getPage(i).extractText()
with open(f'{path}/{txtFile}.txt',mode='a',encoding='utf-8') as f:
    f.write(a)