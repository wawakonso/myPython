# Using python 2.7

import urllib.request
#!/usr/bin/env python

import sys

myFile=sys.argv[1];

def CheckUrl(link):
    # validate url; a way to check if it is a correct url format
    try:
        urllib.request.urlopen(link)
        return True;
    except:
        return False;



index=0;
filename="C:/Users/Konso/Pictures/scripts/im"; # directory where the images will be stored, can be changed by the user to suit its need


file = open(myFile, 'r');
for line in file:
    index=index+1;
    print(line);
    if(CheckUrl(line)==True):
        
        urllib.request.urlretrieve(line, filename+str(index)+".jpg"); # images are stored using name : im+index;
    else :
        print ("Could not save");
        





        




