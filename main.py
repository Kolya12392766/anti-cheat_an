#####################
## anti cheat "an" ##
#####################

import os #import "os"
import time #import "time"
app = '"Among Us.exe"' #set  programm "file"
timeout = 2 #set  timeout
os.system("listdlls.exe " + app + " >start.log") #save start "log" file
f1 = open("start.log") #set  start "log" file
f1 = f1.read()
while app == app:
    os.system("listdlls.exe " + app + " >list.log") #save programm "log" file
    os.system("cls")
    f2 = open("list.log") #set  programm "log" file
    f2 = f2.read()
    print(f2)
    time.sleep(timeout)     #timeout
    if not f1 == f2: #if files is different
        os.system("taskkill /f /im " + app) #kill process
        break