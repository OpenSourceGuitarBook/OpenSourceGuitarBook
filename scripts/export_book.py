#! /usr/bin/python3
# MuseScore batch file conversion
# GNU GENERAL PUBLIC LICENSE GPLv3

import os
import platform
import subprocess
from glob import glob

def quoteString(s):
  return '\'' + s + '\''

def exportFile(files, destExt, srcExt = ".mscz"):
  for filename in files:
    if filename.endswith(srcExt):
        newfile, dummy = os.path.splitext(filename)
        filename = quoteString(filename)
        newfile = quoteString(newfile + destExt)
        command = museApp + " " + filename + " -o " + newfile
        print (command)
        result = os.system(command)

mydir = "../book/"
extensions = [".xml", ".pdf", ".mp3", ".svg"] 

os.chdir(mydir)

if(platform.system() == "Darwin"):
  find = subprocess.Popen(("find", "/Applications", "-maxdepth", "1"), stdout=subprocess.PIPE)
  museApp = subprocess.check_output(("grep", "Muse"), stdin=find.stdout)
  
  museApp = museApp[:-1] + "/Contents/MacOS/mscore"
  museApp = quoteString(museApp)

  result = [y for x in os.walk(".") for y in glob(os.path.join(x[0], "*" + ".mscz"))]

  for ext in extensions:
    exportFile(result, ext)
