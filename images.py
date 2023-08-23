import csv
from datetime import datetime
import os
from pathlib import Path
import shutil

def bytes_to_Kilobytes(size_in_bytes):
    return round(size_in_bytes / (1024),1)

def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

root=(r"C:\Users\ALKODS\Desktop\P1\dairies")

target=(r"C:\Users\ALKODS\Desktop\P1\images dataset")

csv_file_path = (r"C:\Users\ALKODS\Desktop\P1\image_report.csv")


for r, _, files in os.walk(root):
    
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            source_path = os.path.join(r, file)
            dest_path = os.path.join(target)
            shutil.copy(source_path, dest_path)


files = os.listdir(target)
x=0
for filename in files:
    new_filename = filename.replace(filename, "image"+str(x)+".jpg")
    old_file_path = os.path.join(target, filename)
    new_file_path = os.path.join(target, new_filename)
    os.rename(old_file_path, new_file_path)
    x+=1
            
            
files = os.listdir(target)

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Image Name", "Image Size (Kbytes)", "Last Modified"])

    for filename in files:
        image_name = filename
        image_size = os.path.getsize(target+"\\"+filename)
        image_last_modified = os.path.getmtime(target+"\\"+filename)

        size = bytes_to_Kilobytes(image_size)
        size = str(size)+" KB"
        last_modified = format_timestamp(image_last_modified)
        csv_writer.writerow([image_name, size, last_modified])



            
