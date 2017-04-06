#!usr/bin/python

import shutil
import os

allnames = []
allnamePaths = []

count = 0


fileExt = ".jpg"
inputDir = "NAVARRE_1920"
destination = "NAVARRE_1920_test"

for root, dirs, files in os.walk(inputDir):
    for name in files:
            
        if name.endswith(fileExt):

            allnames.append(name)           #list of filenames - basename only
            allnamePaths.append(os.path.join(root,name))    #list of all names with directory paths appended

            count = count + 1


for name in allnamePaths:
	shutil.copy(name, destination)