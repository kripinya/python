# #Reading From Files
# f = open("file.txt", "r")
# content = f.read()         # Read entire file
# lines = f.readlines()      # Read as list of lines
# line = f.readline()        # Read just one line
# f.close()

# #writing to files
# f = open("file.txt", "w")   # Overwrites file if exists
# f.write("Hello Ananya!\n")
# f.writelines(["Line1\n", "Line2\n"])
# f.close()

# #Appending to Files
# f = open("file.txt", "a")
# f.write("New data added\n")
# f.close()

# #Example 1: Write student info to a file
# with open("file.txt", "w")as f:
#     f.write("name: Ananya\n")

#     #read student info:
# with open("file.txt", "r") as f:
#     for line in f:
#         print(line.strip())

#checking if file exists
import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")