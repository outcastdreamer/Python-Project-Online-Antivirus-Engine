from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
import os
import urllib2 as u
import hashlib
import time

#CHECKING INTERNET CONNECTION
urltotest="http://www.lsdx.eu"
nboftrials=0
answer='NO'
flag=0
while answer=='NO' and nboftrials<2:
    try:
        u.urlopen(urltotest)
        answer='YES'
    except:
        essai='NO'
        nboftrials+=1
        print "NET NOT CONNECTED!!"
        time.sleep(3)
        flag=-1


if flag==-1:
    print " Quiting!!"
    quit()

print "CONNECTION ESTABLISHED!!"

print "\n\tChoose what you want to do - \n\t1) Scan a file\n\t2)Scan an URL or website Link"
choice=input("\n ENTER CHOICE 1 OR 2 - ")
flag=0
if choice==1:
    print "\n\t\tPLEASE SELECT A FILE!\n"
    flag=1
    try:
        Tk().withdraw()
        filename=askopenfilename()
        f=str(filename)
        h=str(hashlib.md5(open(f,'rb').read()).hexdigest())
    except IOError:
        print "NO FILE SELECTED!"
        print " QUITTING!!"
        quit()
elif choice==2:
    u=str(raw_input("Enter website URL in correct format - "))
    flag=2
    try:
        h=str(hashlib.md5(u).hexdigest())
        print "HASH CODE - ",h
    except IOError:
        print "INVALID URL INPUTTED!\n QUITING!"
        time.sleep(4)
        quit()
else:
    print "Invalid Choice! Quiting!"
    time.sleep(4)
    quit()

#os.chdir("C:\Users\Saket\Documents\HackFest17")
import requests
params = {'apikey': '6ac868dd8c2218f9009c4ce051aaaa48d2b192251ff3922387ea153962fe6e00', 'resource': h}
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
          }
response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
  params=params, headers=headers)
d = response.json()
print d

print "Number of viruses found - ",d['positives']

def check():
    if d['positives']==0:
        if flag==1:
            tkMessageBox.showinfo("NOTICE!!","%d Viruses or Malwares found among total of %d searches among various Antivirus and AntiMalware Engines.\nTHE FOLLOWING INPUTTED FILE HAS NO VIRUS OR MALWARES!\nYOU CAN GO AHEAD AND USE IT!"%(d['positives'],d['total']))
        else:
            tkMessageBox.showinfo("NOTICE!!",
                                  "%d Viruses or Malwares found among total of %d searches among various Antivirus and AntiMalware Engines.\nTHE FOLLOWING URL HAS NO VIRUS OR MALWARES!\nYOU CAN GO AHEAD AND USE IT!" % (
                                  d['positives'], d['total']))
    else:
        if flag==1:
            tkMessageBox.showinfo("NOTICE!!","%d Viruses or Malwares found among total of %d searches among various Antivirus and AntiMalware Engines.\nPLEASE DON'T USE THIS APPLICATION AND REMOVE IT"%(d['positives'],d['total']))
            d1=d['scans']
            l=[]
            for i in d1:
                l+=[i,]
            f=open("Output.txt",'w')
            temp=[]
            for i in range(len(l)):
                temp+=[d1[l[i]],]
            sp=" "
            f.writelines("  ---S.No.---"+"\t"*3+"   ---ANTIVIRUS SEARCH ENGINE NAME---"+"\t"*3+"  ---VIRUS FOUND---")
            f.write("\n"*3)
            for i in range(len(temp)):
                t=str(l[i])
                while len(t)!=25:
                    t+=sp
                f.writelines(str(i+1)+".)"+"\t"*3+t+"\t"*4+str(temp[i]['result']))
                f.write("\n")
            f.close()
            os.startfile("Output.txt")
        else:
            tkMessageBox.showinfo("NOTICE!!",
                                  "%d Viruses or Malwares found among total of %d searches among various Antivirus and AntiMalware Engines.\nPLEASE DON'T USE THIS URL AND IT'S HARMFUL!" % (
                                  d['positives'], d['total']))
            d1 = d['scans']
            l = []
            for i in d1:
                l += [i, ]
            f = open("Output.txt", 'w')
            temp = []
            for i in range(len(l)):
                temp += [d1[l[i]], ]
            sp = " "
            f.writelines(
                "  ---S.No.---" + "\t" * 3 + "   ---ANTIVIRUS SEARCH ENGINE NAME---" + "\t" * 3 + "  ---VIRUS FOUND---")
            f.write("\n" * 3)
            for i in range(len(temp)):
                t = str(l[i])
                while len(t) != 25:
                    t += sp
                f.writelines(str(i + 1) + ".)" + "\t" * 3 + t + "\t" * 4 + str(temp[i]['result']))
                f.write("\n")
            f.close()
            os.startfile("Output.txt")
check()
