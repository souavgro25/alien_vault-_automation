import os
import pandas as pd
import shutil
cwd =os.getcwd()

directory = 'C:/Users/Sourabh.Grover/Desktop/Daily report/Daily_rpt_30_4_2023'
my_dict = {}
merged =""
# Create a dictionary with keys derived from the first names of the values
def excel(dir):
    excel_p=f"{dir}\excel files"
    os.makedirs(excel_p, exist_ok=True)
    merged_p=f"{excel_p}\merged_files"
    merged =merged_p
    os.makedirs(merged_p, exist_ok=True)
    for filename in os.listdir(dir):
        ext =os.path.splitext(filename)[1]
        if ext == ".csv":
            df = pd.read_csv(os.path.join(dir, filename),  sep=';' , encoding="utf-8")
            new_filename=f"{filename}.xlsx"
            df=df.to_excel(f'{filename}.xlsx',index=False)
            try:
                src_path=os.path.join(cwd,new_filename)
                shutil.move(src_path, excel_p)
            except:
                continue
        else:
            continue
    for val in os.listdir(excel_p):
        ext =os.path.splitext(val)[1]
        key = val.split('_')[0]   # Extract the first four characters as the key
        if key == val.split('_')[0] and ext== '.xlsx':
            if key == val.split('_')[0] and ext== '.xlsx':   # Check if the key is similar to the value
                df =pd.read_excel(os.path.join(excel_p, val),sheet_name='Sheet1',engine='openpyxl')
                if key in my_dict:
                    my_dict[key].append(df)
                else:
                    my_dict[key] = [df]


    for key in my_dict:             
        master = pd.concat(my_dict[key],axis=0)
        new_filename=f'merged_{key}.xlsx'
        master.to_excel(f'merged_{key}.xlsx',index=False)  
        try:
            src_path=os.path.join(cwd,new_filename)
            shutil.move(src_path, merged)
        except:
            continue     
# Display the contents of the dictionary
