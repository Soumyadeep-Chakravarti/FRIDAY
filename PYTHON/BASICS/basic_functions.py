def make_folders_files():
    
    #imports
    import sys
    import os
    
    #directories
    os.mkdir(os.path.join(os.path.expanduser("~"),"Documents","FRIDAY_AI"))
    os.mkdir(os.path.join(os.path.expanduser("~"),"Documents","FRIDAY_AI","BACKUP"))
    os.mkdir(os.path.join(os.path.expanduser("~"),"Documents","FRIDAY_AI","PERIPHARALS"))
    os.mkdir(os.path.join(os.path.expanduser("~"),"Documents","FRIDAY_AI","USERS"))
    os.mkdir(os.path.join(os.path.expanduser("~"),"Documents","FRIDAY_AI","LOGS"))

    #files
    make_file(0,'users_list',os.path.join(os.path.expanduser("~"),"Documents","FRIDAY_AI"))
    
    user_data = read_file(0,'user_list',os.path.join(os.path.expanduser("~"),"Documents","FRIDAY_AI"))
    
    if len(user_data)>3:
        for i in range(3,len(user_data)):
            make_file(1,'logs',os.path.join(os.path.expanduser("~"),"Documents","FRIDAY_AI","LOGS",user_data[i]))
    
def date_for_file():
    import time
    date = time.strftime('%d%b%Y', time.localtime()).upper()
    return date

def make_file(file_type:int,file_name:str,path:str):
    import pickle
    import datetime
    import csv


    lines = [f"START OF FILE {file_name}",f"FILE TYPE: {file_type}",f"CREATED ON: {f'{date_for_file()}'.capitalize}"]
    if file_type == 0:
        with open(f"{file_name}.bat",'wb') as file:
            for line in lines:
                pickle.dump(line,file)
            
    elif file_type == 1:
        with open(f"{file_name}.txt",'w') as file:
            for line in lines:
                file.writelines(line)
    
    elif file_type == 2:
        with open(f"{file_name}.csv",'w') as file:
            csv_writer = csv.writer(file)
            for line in lines:
                csv_writer.writerow(line)
                
def read_file(file_type:int,file_name:str,path:str):
    import datetime
    import pickle
    import csv
    import os
    data = []
    lines = [f"START OF FILE {file_name}",f"FILE TYPE: {file_type}",f"CREATED ON: {f'{date_for_file()}'.capitalize}"]
    if file_type == 0:
        with open(os.path.join(path,file_name),'wr') as file:
            data = pickle.load(file)
    
    elif file_type == 1:
        with open(os.path.join(path,file_name),'r') as file:
            data = file.readlines()
    
    elif file_type == 2:
        with open(os.path.join(path,file_name),'r') as file:
            csv_reader = csv.reader(file)
            data = []
            for row in csv_reader:
                data.append(row)
    
    return data

def write_file(file_type:int,file_name:str,path:str,data:list):
    import pickle
    import datetime
    import csv

    if file_type == 0:
        with open(f"{file_name}.bat",'ab') as file:
            for line in data:
                pickle.dump(line,file)
            
    elif file_type == 1:
        with open(f"{file_name}.txt",'a') as file:
            for line in data:
                file.writelines(line)
    
    elif file_type == 2:
        with open(f"{file_name}.csv",'a') as file:
            csv_writer = csv.writer(file)
            for line in data:
                csv_writer.writerow(line)