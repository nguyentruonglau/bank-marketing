from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
from Normalize import normal, switch_y
from sklearn.model_selection import train_test_split
from keras.models import load_model
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import xlsxwriter

class FileInput(Toplevel):
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
        self.top_image=PhotoImage(file='Icons/user4.png')
        self.top_image_label=Label(self.top, image=self.top_image)
        self.top_image_label.place(x=120,y=10)
        self.heading=Label(self.top, text='File Input', font='arial 20 bold', bg='white', fg='#ebb434' )
        self.heading.place(x=260, y=60)
        
        #Open File
        self.btnOpenFile=Button(self.bottom, text='Open File', fg='black', bg='#34baeb', width=17, height=2, command=self.readFile)
        self.btnOpenFile.place(x=100, y=350)
        
        #Result
        self.btnResult=Button(self.bottom, text='Predict', fg='black', bg='#34baeb', width=17, height=2, command=self.predictData)
        self.btnResult.place(x=250, y=350)
        
        #Exit
        self.btnExit=Button(self.bottom, text='Exit', fg='black', bg='#34baeb', width=17, height=2, command=self.destroy)
        self.btnExit.place(x=400, y=350)
        
    def readFile(self):
        '''
        + Mở file để đọc và hiển thị lên UI
        + Chuẩn hóa dữ liệu
        '''
        self.name = askopenfilename(filetypes=[('TruongLau', '*.csv'), ('CongMinh', '*.xlsx'), ('DucCuong', '*.xlsx')])
        self.data=pd.read_csv(self.name, delimiter=",")
        self.lbText=Label(self.bottom, text=str(self.data[0:16]), font='arial 10 bold', fg='black', bg='#0ecc41')
        self.lbText.place(x=90, y=20)
        
        self.data=normal(self.data)
        
        
        
        
    
    def predictData(self):
        '''
        + Hiển thị kết quả dự đoán của mô hình
        + Ghi và định dạng file xlsx
        '''
        Data_X=self.data[['age','job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome']]
        Data_X=Data_X.drop('contact',axis=1)
        Data_y=self.data['y']
        
        Normal_Data=pd.read_csv('Trained_Data_Plus.csv', delimiter=',')
        Normal_Data_X=Normal_Data[['age','job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome']]
        Normal_Data_y=Normal_Data['y']
        

        logreg = LogisticRegression()
        logreg.fit(Normal_Data_X, Normal_Data_y)
        y_pred = logreg.predict(Data_X)
        
        #----
        workbook = xlsxwriter.Workbook('Result.xlsx')
        worksheet = workbook.add_worksheet()

        label_format = workbook.add_format({'bold': True,
                            'bg_color': 'greeen'
                            })
        
        error = workbook.add_format({
                            'bg_color': 'red'
                            })

        worksheet.write('A1', 'Y', label_format)
        worksheet.write('B1', 'Y PREDICT', label_format)


        row = 1
        col = 0
        
        temp=-1;
        # Iterate over the data and write it out row by row.
        for item in (Data_y):
            temp=item;
            worksheet.write(row, col, switch_y(item))
            row += 1
            
        row=1
        for item in (y_pred):
            worksheet.write(row, col+1, switch_y(item))
            row += 1
            
        
        Re=Data_y+y_pred
        for i in (range(len(Re))):
            if(Re[i]==1):
                worksheet.set_row(i+1, 15, error)
        worksheet.set_column('A:B', 100)
        
        workbook.close()

        messagebox.showinfo('Result', str(round( logreg.score(Data_X, Data_y),2)*100)+'%');
        
      
        