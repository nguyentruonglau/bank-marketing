# -*- coding: utf-8 -*-

from tkinter import *
from Normalize import *
from keras.models import load_model
import numpy as np

class UserInput(Toplevel):
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
        self.top_image=PhotoImage(file='Icons/user.png')
        self.top_image_label=Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120,y=10)
        self.heading=Label(self.top, text='User Input', font='arial 20 bold', bg='white', fg='#ebb434' )
        self.heading.place(x=260, y=60)
        
        #Age
        self.lbAge=Label(self.bottom, text='Age', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbAge.place(x=40, y=40)
        
        self.tbAge=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbAge.place(x=40, y=70)
        
        #Job
        self.lbJob=Label(self.bottom, text='Job', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbJob.place(x=40, y=120)
        
        self.tbJob=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbJob.place(x=40, y=150)
        
         #Marital
        self.lbMarital=Label(self.bottom, text='Marital', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbMarital.place(x=40, y=200)
        
        self.tbMarital=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbMarital.place(x=40, y=230)
        
         #Education
        self.lbEducation=Label(self.bottom, text='Education', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbEducation.place(x=40, y=280)
        
        self.tbEducation=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbEducation.place(x=40, y=310)
        
        #Default
        self.lbDefault=Label(self.bottom, text='Default', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbDefault.place(x=180, y=40)
        
        self.tbDefault=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbDefault.place(x=180, y=70)
        
        #Balance
        self.lbBalance=Label(self.bottom, text='Balance', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbBalance.place(x=180, y=120)
        
        self.tbBalance=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbBalance.place(x=180, y=150)
        
        #Housing
        self.lbHousing=Label(self.bottom, text='Housing', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbHousing.place(x=180, y=200)
        
        self.tbHousing=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbHousing.place(x=180, y=230)
        
        #Loan
        self.lbLoan=Label(self.bottom, text='Loan', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbLoan.place(x=180, y=280)
        
        self.tbLoan=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbLoan.place(x=180, y=310)
        
        #Contact
        self.lbContact=Label(self.bottom, text='Contact', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbContact.place(x=320, y=40)
        
        self.tbContact=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbContact.place(x=320, y=70)
        
        #Day
        self.lbDay=Label(self.bottom, text='Day', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbDay.place(x=320, y=120)
        
        self.tbDay=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbDay.place(x=320, y=150)
        
        #Month
        self.lbMonth=Label(self.bottom, text='Month', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbMonth.place(x=320, y=200)
        
        self.tbMonth=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbMonth.place(x=320, y=230)
        
        #Duration
        self.lbDuration=Label(self.bottom, text='Duration', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbDuration.place(x=320, y=280)
        
        self.tbDuration=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbDuration.place(x=320, y=310)
        
        #Campaign
        self.lbCampaign=Label(self.bottom, text='Campaign', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbCampaign.place(x=460, y=40)
        
        self.tbCampaign=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbCampaign.place(x=460, y=70)
        
        #Pdays
        self.lbPdays=Label(self.bottom, text='Pdays', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbPdays.place(x=460, y=120)
        
        self.tbPdays=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbPdays.place(x=460, y=150)
        
         #Previous
        self.lbPrevious=Label(self.bottom, text='Previous', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbPrevious.place(x=460, y=200)
        
        self.tbPrevious=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbPrevious.place(x=460, y=230)
        
         #Poutcome
        self.lbPoutcome=Label(self.bottom, text='Poutcome', font='arial 8 bold', bg='#34baeb', fg='black')
        self.lbPoutcome.place(x=460, y=280)
        
        self.tbPoutcome=Entry(self.bottom, fg='black', bg='#e6a749', width=20)
        self.tbPoutcome.place(x=460, y=310)
        
        #Result
        self.btnResult=Button(self.bottom, text='Predict', fg='black', bg='#34baeb', width=17, height=2, command=self.btnPredict_Click)
        self.btnResult.place(x=150, y=350)
        
        #Exit
        self.btnExit=Button(self.bottom, text='Exit', fg='black', bg='#34baeb', width=17, height=2, command=self.destroy)
        self.btnExit.place(x=350, y=350)
    
        
    def btnPredict_Click(self):
        '''
        + Nhận dữ liệu từ UI
        + Chuẩn hóa theo dữ liệu train
        '''
        self.tbJob=switch_job(self.tbJob.get())
        self.tbMarital=switch_marital(self.tbMarital.get())
        self.tbEducation=switch_education(self.tbEducation.get())
        self.tbDefault=switch_default(self.tbDefault.get())
        self.tbHousing=switch_housing(self.tbHousing.get())
        self.tbLoan=switch_loan(self.tbLoan.get())
        self.tbMonth=switch_month(self.tbMonth.get())
        self.tbContact=switch_contact(self.tbContact.get())
        self.tbPoutcome=switch_poutcome(self.tbPoutcome.get())
        self.tbAge=int(self.tbAge.get())
        self.tbDuration=round((int(self.tbDuration.get()))/60.0,2);
        self.tbBalance=int(self.tbBalance.get())
        self.tbCampaign=int(self.tbCampaign.get())
        self.tbDay=int(self.tbDay.get())
        self.tbPdays=int(self.tbPdays.get())
        self.tbPrevious=int(self.tbPrevious.get())
        a=np.zeros(15)
        a[0]=self.tbAge;         a[1]=self.tbJob;
        a[2]=self.tbMarital;     a[3]=self.tbEducation;
        a[4]=self.tbDefault;     a[5]=self.tbBalance;
        a[6]=self.tbHousing;     a[7]=self.tbLoan;
        a[8]=self.tbDay;         a[9]=self.tbMonth;
        a[10]=self.tbDuration;   a[11]=self.tbCampaign;
        a[12]=self.tbPdays;      a[13]=self.tbPrevious;   a[14]=self.tbPoutcome;
        a=a.reshape(1,15)
        model = load_model('trained_model.h100')
        result = model.predict(a)
        pre=np.argmax(result)
        messagebox.showinfo('Predict', switch_y(pre))
    
    
    
    
        