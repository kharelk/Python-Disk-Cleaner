import os, shutil, configparser

#CONFIG FILE DATA
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
totalSpace, usedSpace, freeSpace = shutil.disk_usage("/") 
totalSpace = totalSpace // (2**30)
usedSpace = usedSpace // (2**30)
freeSpace = freeSpace // (2**30)

print("Total:",totalSpace,"GiB")
print("Used:",usedSpace,"GiB")
print("Free:",freeSpace,"GiB")

#CLEAN
if (usedSpace >= totalSpace * 0.85): # Check disk usage more then 50%
    print("disk has more then 85% usage, 85% = ",totalSpace * 0.85,"GiB")
    for files in os.listdir(TempDir):
        path = os.path.join(TempDir, files) # Path for every file in Temp Dir
        try:
            shutil.rmtree(path) # Delete directory
            print(path, " Directory has been deleted")
        except OSError:
            os.remove(path) # Delete File
            print(path, " File has been deleted")
else: # No need to delete fies
    print("disk has less then 85% usage")


