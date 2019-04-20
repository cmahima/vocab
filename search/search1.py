import os


class sear1:
  #def __init__(self):

  def check1(self, file_path): 
          
# Open the file with read only permit
   f = open(file_path)
# use readline() to read the first line 
   line = f.readline()

   while line:
    line = f.readline()
    if "(1-image):" in line:
    # use realine() to read next line
     line = f.readline()
     line = f.readline()
     
    # print(line)
     return line;
    # print(line)
   f.close()
