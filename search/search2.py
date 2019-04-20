
import os


class sear2:
 def check2(self, file_path):
  
  f = open(file_path)
# use readline() to read the first line 
  line = f.readline()

  while line:
    line = f.readline()
    
    if "Guess 1. Speak!" in line:
    # use realine() to read next line
     line = f.readline()
     #line = f.readline()
     return line;
    # print(line)
  f.close()
