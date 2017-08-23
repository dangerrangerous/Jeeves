# Brian Keppinger
# note: file name format must be file.number.extension
# ex: tacocat.0001.png

from shutil import copyfile

# note: the entire filepath must be entered 
src = input("Please enter the filepath of the file to be copied. \n")

num_copies = input("Please enter the number of copies you would like to make. \n")
int_num_copies = int(num_copies)

split_name = src.split('.')
core_file_name = split_name[0]
int_file_number = int(split_name[1])
file_extension = split_name[2]

# copy and reassemble file path
for i in range(int_num_copies):
    int_file_number += 1
    str_file_number = str(int_file_number).zfill(4)
    dst = core_file_name + "." + str_file_number + "." + file_extension 
    copyfile(src, dst)
    
    print("File copied to: " , dst)

