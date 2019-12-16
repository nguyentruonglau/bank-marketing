# -*- coding: utf-8 -*-

from tkinter import *

class AboutUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x550+350+200')
        self.title('Ground One')
        self.resizable(False, False)
        self.iconbitmap('Icons/icon3.ico')
        
        self.top=Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        
        self.bottom=Frame(self, height=500, bg='#0ecc41')
        self.bottom.pack(fill=X)
        
        #top frame design
        self.top_image=PhotoImage(file='Icons/about_us.png')
        self.top_image_label=Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120,y=10)
        self.heading=Label(self.top, text='About Us', font='arial 20 bold', bg='white', fg='#ebb434' )
        self.heading.place(x=260, y=60)
        
        self.text=Label(self.bottom, text='DEMO ĐỒ ÁN MÔN HỌC:'
                        '\n KHAI THÁC DỮ LIỆU VÀ ỨNG DỤNG'
                        '\n GVGD: NGUYỄN THỊ ANH THƯ'
                        '\n\n\n NHÓM I'
                        '\n Nguyễn Trường Lâu - 17520676'
                        '\n Trần Công Minh - 17520763'
                        '\n Bùi Đức Cường - 17520301', font='arial 20 bold', fg='black', bg='#0ecc41')
        self.text.place(x=65, y=50)