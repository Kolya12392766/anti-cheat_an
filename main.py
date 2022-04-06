#####################
## anti cheat "an" ##
#####################

import os #import "os"
import time #import "time"
import filecmp #import "filecmp"

app = "explorer.exe" #set  programm "file"
timeout = 3 #set  timeout
f1 = "start.log" #set  start "log" file
f2 = "list.log" #set  programm "log" file
os.system("listdlls.exe " + app + " >start.log") #save start "log" file

while app == app:
    os.system("listdlls.exe " + app + " >list.log") #save programm "log" file
    time.sleep(timeout)     #timeout
    result = filecmp.cmp(f1,f2)   #save result
    if result == 0: #if
        os.system("taskkill /f /im " + app) #kill process
        pass
