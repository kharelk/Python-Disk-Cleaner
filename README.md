# Python-Disk-Cleaner

Python script that clean a certain folder given from a config file that located at the same directory after 85% usage of Disk.


The user need to specify the scheduler time to run (in hours)


Work only on Windows os.


The script needs to run from cmd as administrator.


Config file needs to contain:<br/>
Section name in my case: [Paths].<br/>
and Key name in my case: "TempPath".<br/>


example for config file:
```` 

[Paths]
TempPath = C:\Windows\TempTest

````
