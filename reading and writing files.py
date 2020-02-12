# READING AND WRITING FILES ##################################################
# open a file for writing and create it if it doesn't exist: open()
f = open("textfile.txt", "w+")     # w means write, + means create it if it doens't exists

# write some lines of data to the file
for i in range(10):
  f.write("This is line " + str(i) + "\r\n")
  
# close the file when done
f.close()

# open the file and append more text to the end
f = open("textfile.txt", "a")     # a means append to the end of the file, instead of writing over everything

# open the file to read:
f = open("textfile.txt", "r")    #  r means read

# open the file back up and read all of the contents: read()
if f.mode == 'r':
  contents = f.read()     # read() reads the ENTIRE contents
  print(contents)

# open the file and read SOME of the contents: readlines()
if f.mode == 'r':
fl = f.readlines()
for x in fl:
  print(x)
print(contents)

# WORKING WITH OS PATH UTILITIES

import os
from os import path

# print name of OS
print(os.name)

# check for the existence of an item and its type
print("Item exists: " + str(path.exists("textfile.txt")))
print("Item is a file: " + str(path.isfile("textfile.txt")))
print("Item is a directory: " + str(path.isdir("textfile.txt")))

# work with file paths
print("Item path: " + str(path.realpath("textfile.txt")))
print("Item path and name: " + str(path.split(path.realpath("textfile.txt))))


# get the modification time
t = time.ctime(path.getmtime("textfile.txt"))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

# calculate how long ago the item was modified
td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
  path.getmtime("textfile.txt")
)
print("It has been " + str(td) + " since the file was modified")

# USING SHELL UTILITIES ##############################################
import shutil

#make a duplicate of an existing file
if path.exists("textfile.txt"):
  # get the path to the file in the current directory
  src = path.realpath("textfile.txt")
  
  # let's make a backup copy by appending "bak" to the name
  dst = src + ".bak"
  
  # copy over the permissions, modification times, and other info
  shutil.copy(src, dst)
  
  # rename the original file
  os.rename("textfile.txt", "newfile.txt")
  
  # now put things into a ZIP archive
  from shutil import make_archive
  root_dir, tail = path.split(src)
  shutil.make_archvie("archive", "zip", root_dir)
  
  # more fine-grained control over ZIP files
  from zipfile import ZipFile
  with ZipFile("testzip.zip", "w") as newzip:
    newzip.write("textfile.txt")
    newzip.write("textfile.txt.bak")
  

