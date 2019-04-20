import os


class search1:
  def __init__(self):

  def check():        
# Open the file with read only permit
   f = open('/home/mahima/game/file.txt')
# use readline() to read the first line 
   line = f.readline()

   while line:
    line = f.readline()
    if "(1-image):" in line:
    # use realine() to read next line
     line = f.readline()
     line = f.readline()
     return line;
     #print(line)
   f.close()
