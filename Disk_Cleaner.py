import os, shutil, configparser
from apscheduler.schedulers.blocking import BlockingScheduler

#SCHEDUAL TIME 
scheduler = BlockingScheduler()
hoursToRun = int(input("Enter how often the script will run (in hours:): "))

#CONFIG_FILE DATA
config = configparser.ConfigParser()
file = str(input("Enter config file name: "))
section = str(input("Enter [section] name in config file: ")) # Get section name, in my case "Paths"
pathValue = str(input("Enter key name: ")) # Get key name, in my case "TempPath" 

try:
    config.read_file(open(file,'r')) # Read config.txt file
    TempDir = config.get(section, pathValue) # Get path from file
    print("temp folder path:", TempDir)
except OSError:
    print(OSError)

# DISK USAGE DATA

#CLEAN
@scheduler.scheduled_job('interval', hours = hoursToRun)
def timed_job():
    print("'This job is run every",hoursToRun,"hours.")
    totalSpace, usedSpace, freeSpace = shutil.disk_usage("/") 
    totalSpace = totalSpace // (2**30)
    usedSpace = usedSpace // (2**30)
    freeSpace = freeSpace // (2**30)
    print("Total:",totalSpace,"GiB")
    print("Used:",usedSpace,"GiB")
    print("Free:",freeSpace,"GiB")

    if (usedSpace >= totalSpace * 0.50): # Check disk usage more then 50%
        print("disk has more then 50% usage, 50% = ",totalSpace * 0.50,"GiB")
        if len(os.listdir(TempDir)) == 0:
            print("Directory is empty")
        else:    
            for files in os.listdir(TempDir):
                path = os.path.join(TempDir, files) # Path for every file in Temp Dir
                try:
                    shutil.rmtree(path) # Delete directory
                    print(path, " Directory has been deleted")
                except OSError:
                    os.remove(path) # Delete File
                    print(path, " File has been deleted")
    else: # No need to delete fies
        print("disk has less then 50% usage")



scheduler.configure()
scheduler.start()

