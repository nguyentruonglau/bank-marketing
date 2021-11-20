from tkinter import *
from User_Input import UserInput
from File_Input import FileInput
from About_Us import AboutUs

class Application(object):
    def __init__(self, master):
        self.master=master
        
        #frames
        self.top=Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        
        self.bottom=Frame(master, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)
        
        #top frame design
        self.top_image=PhotoImage(file='Icons/bank.png')
        self.top_image_label=Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120,y=10)
        self.heading=Label(self.top, text='Bank Data Processing', font='arial 20 bold', bg='white', fg='#ebb434' )
        self.heading.place(x=220, y=60)
        
        #button1 - user input
        self.userButton=Button(self.bottom, text='User Input', fg='#1c1b1b', bg='#e6a749', width=50, height=2, command=self.user_input)
        self.userButton.place(x=150, y=90)         
        
        #button2 - file input
        self.fileButton=Button(self.bottom, text='File Input', fg='#1c1b1b', bg='#e6a749', width=50, height=2, command=self.file_input)
        self.fileButton.place(x=150, y=170)   
        
        #button3 - about us
        self.aboutButton=Button(self.bottom, text='About Us', fg='#1c1b1b', bg='#e6a749', width=50, height=2, command=self.aboutus)
        self.aboutButton.place(x=150, y=250) 
        
    def user_input(self):
        input1=UserInput();
        
    def file_input(self):
        input2=FileInput();
        
    def aboutus(self):
        input3=AboutUs();

def main():
    root=Tk()
    app=Application(root)
    root.title('Ground One')
    root.geometry('650x550+350+200')
    root.resizable(False, False)
    root.iconbitmap('Icons/icon3.ico')
    root.mainloop()


if __name__=='__main__':
    main();