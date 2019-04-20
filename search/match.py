from search1 import sear1
from search2 import sear2
import os


if __name__ == '__main__':
  

    st1= sear1()
    st2=sear2()
    str1="/home/mahima/game/file.txt"
    str2="/home/mahima/game/files.txt"
    #res = t.classify('./boxing.jpg')
    #print(res)
    s1=st1.check1(str1);
    s2=st2.check2(str2);
  
    if(s1.lower()==s2.lower()):
     
     os.system("espeak 'You are correct'")
     print("You are correct");
    else:
     os.system("espeak 'You are wrong'")
     os.system("espeak ' Correct answer is '")
     os.system("espeak ' on the screen'")
     print("Correct answer is",s1)
     print("You are wrong");
