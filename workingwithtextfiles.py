"""
python comes with a default python fn open() that accepts two parameters ,the file name and the mode-thats how you
want to access the fil(read ,write read or write
if the fiole exists it will just open the file and if not it proceeds and creates you one
"""
#creating/opening a file
file_text=open("test_file.txt","w+")#opens test_file in read and write mode
file_text.write("this is a test file")
#any time you open a text file you must close
file_text.close()
file_text=open("test_file.txt","r")#read only mode
data_read=file_text.read()
print(file_text.read())#this as no effect in the program
file_text.close()
print(data_read)

#WRITING TO CSV FILES
#works with data by separating them with commas
import csv
with open("test_file.csv",mode="w",newline="") as file_csv:#open the csv file in write mode as file_csv-newline is empty
    writer=csv.writer(file_csv,delimiter=",")#gives us the freedomto write into the variable
    writer.writerow(["NAME","CITY"])
    writer.writerow(["chelsea football club","west london"])#file closes automatically

#READING TO CSV FILES
with open("test_file.csv",mode="r") as file_csv:
    reader=csv.reader(file_csv,delimiter=",")
    for row_csv in reader:
        print(row_csv)