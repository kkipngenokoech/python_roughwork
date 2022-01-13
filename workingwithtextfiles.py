"""
python comes with a default python fn open() that accepts two parameters ,the file name and the mode-thats how you
want to access the fil(read ,write read or write
if the fiole exists it will just open the file and if not it proceeds and creates you one
"""
# creating/opening a file
file_text = open("test_file.txt", "w+")  # opens test_file in read and write mode
file_text.write("this is a test file")
# any time you open a text file you must close
file_text.close()
file_text = open("test_file.txt", "r")  # read only mode
data_read = file_text.read()
print(file_text.read())  # this as no effect in the program
file_text.close()
print(data_read)

# WRITING TO CSV FILES
# works with data by separating them with commas
import csv

with open("test_file.csv", mode="w",
          newline="") as file_csv:  # open the csv file in write mode as file_csv-newline is empty
    writer = csv.writer(file_csv, delimiter=",")  # gives us the freedomto write into the variable
    writer.writerow(["NAME", "CITY"])
    writer.writerow(["chelsea football club", "west london"])  # file closes automatically

# READING TO CSV FILES
with open("test_file.csv", mode="r") as file_csv:
    reader = csv.reader(file_csv, delimiter=",")
    for row_csv in reader:
        print(row_csv)

#################
with open('pi_digits.txt') as file_object:
    file_contents = file_object.read()
print(file_contents.rstrip())  # removes an extra blank space normally left by the end of the open() function
# when your file is an absolute diffrent place from the current directory you uplpoad the absolute path
file_path = "C:\\Users\\kip\\Documents\\pi_digits.txt"
with open(file_path) as maguke_harm:
    lines = maguke_harm.readlines()  # this allows you to access the lines outside this function
    for line in maguke_harm:  # reading line by line
        print(line.rstrip())#removes whitespace in many spaces
for line in lines:
    print(line)
#manipulating the files
pi_string=''
for line in lines:
    pi_string+=line.strip()#strip removes whitespace in a single line
#pi_string=int(pi_string)-converting to integer
print(pi_string,len(pi_string),type(pi_string))

#WRITING TO A TEXT FILE
file_name="programming.txt"
with open(file_name,'w') as write_file:
    write_file.write("i love programming ,python mostly")
with open(file_name,'r') as read_file:
    reader=read_file.read()
print(reader)

#APPENDING TO A FILE
#it justs adds the content on top ,it doesnt erase
with open(file_name,'a') as append_file:
    appender=append_file.write("\ni also love anlyzing databases")
with open(file_name) as reader_file:
    reader_append=reader_file.read()
print(reader_append)
#using split function-splits the lines into single strings using space as guide and stores them in a list
words=reader_append.split()
print(words)
