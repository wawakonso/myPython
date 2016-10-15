

import urllib.request
#!/usr/bin/env python

import sys

myFile=sys.argv[1];

def CheckUrl(link):
    #code = urllib.request.urlopen(link).code;
    try:
        urllib.request.urlopen(link)
        return True;
    except:
        return False;
    


def getMyFile(myFile):
    file = open(myFile, 'r');
    for line in file:
        print (line);


index=0;
filename="C:/Users/Konso/Pictures/scripts/im";


file = open(myFile, 'r');
for line in file:
    index=index+1;
    print(line);
    if(CheckUrl(line)==True):
        
        urllib.request.urlretrieve(line, filename+str(index)+".jpg");
    else :
        print ("Could not save");
        




