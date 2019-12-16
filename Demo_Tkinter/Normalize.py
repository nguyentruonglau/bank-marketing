'''
+ LabelEncoder: mã hóa các chuỗi theo thứ tự alpha.
+ Các hàm có nhiệm vụ: chuyển hóa dữ liệu người dùng nhập tay và nhập bằng file sao cho đúng chuẩn dữ
  liệu chúng ta thực hiện train.
'''

from sklearn.preprocessing import LabelEncoder
import numpy as np

def switch_job(argument):
    switcher = {
        "admin":0,
        "blue-collar":1,
        "entrepreneur":2,
        "housemaid":3,
        "management":4,
        "retired":5,
        "self-employed":6,
        "services":7,
        "student":8,
        "technician":9,
        "unemployed":10,
        "unknown":11
    }
    return(switcher.get(argument))
    
def switch_marital(argument):
    switcher = {
        "divorced":0,
        "married":1,
        "single":2
    }
    return(switcher.get(argument))
    
def switch_education(argument):
    switcher = {
        "primary":0,
        "secondary":1,
        "tertiary":2,
        "unknown":3
    }
    return(switcher.get(argument))
    
def switch_default(argument):
    switcher = {
        "no":0,
        "yes":1
    }
    return(switcher.get(argument))
    
def switch_housing(argument):
    switcher = {
        "no":0,
        "yes":1
    }
    return(switcher.get(argument))
    
def switch_loan(argument):
    switcher = {
        "no":0,
        "yes":1
    }
    return(switcher.get(argument))
    
def switch_month(argument):
    switcher = {
        "jan":1,
        "feb":2,
        "mar":3,
        "apr":4,
        "may":5,
        "jun":6,
        "jul":7,
        "aug":8,
        "sep":9,
        "oct":10,
        "nov":11,
        "dec":12
    }
    return(switcher.get(argument))
    
def switch_contact(argument):
    switcher = {
        "cellular":0,
        "telephone":1,
        "unknown":2
    }
    return(switcher.get(argument))
    
def switch_poutcome(argument):
    switcher = {
        "failure":0,
        "other":1,
        "success":2,
        "unknown":3
    }
    return(switcher.get(argument))
    
def switch_y(argument):
    switcher = {
        0:"no",
        1:"yes"
    }
    return(switcher.get(argument))
    
def duration(data):
    
    return data

def normal(data):
    labelencoder_X = LabelEncoder()
    data['job']      = labelencoder_X.fit_transform(data['job']) 
    data['marital']  = labelencoder_X.fit_transform(data['marital']) 
    data['education']= labelencoder_X.fit_transform(data['education']) 
    data['default']  = labelencoder_X.fit_transform(data['default']) 
    data['housing']  = labelencoder_X.fit_transform(data['housing']) 
    data['loan']     = labelencoder_X.fit_transform(data['loan']) 
    data['contact']=labelencoder_X.fit_transform(data['contact'])
    
    data['month'].replace(['jan','feb','mar','apr','may','jun','jul','aug','sep','oct' ,'nov','dec'],[1,2,3,4,5,6,7,8,9,10,11,12], inplace=True)
    data['poutcome'].replace(['unknown', 'failure', 'other', 'success'],[1,2,3,4], inplace=True)
    data['y'].replace(['no', 'yes'],[0,1], inplace=True)
    data['duration']=np.array(data['duration']/60.0, dtype=float);
    return data;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    