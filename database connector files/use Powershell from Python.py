"""
connect to a website that requires using Powershell for authentication from inside Python
Requires passing instructions to the website on what to do from a Powershell .ps1 script
For this file, Powershell will then save a selection of data in a folder location that Python then reads.
"""

import subprocess
import os, os.path
import pandas as pd
import glob
import time

DIR = "//PATH/Folder"
for x in glob.glob(DIR + "/*"): os.remove(x)

# invoke Powershell
subprocess.Popen(["powershell.exe,
                    "powershell - Execution Policy ByPass -File '//PATH/TO_PS1_FILE/My_file.ps1'"]
                    , stdout=subprocess.PIPE)
print("downloading sources...")
while 0 == 0:
    if len([name for name in os.listdir(DIR)]) == 7: # our ps1 script obtains 7 files
        print("7 files obtained! writing to disk.")
        size_check=0
        while size_check < 8:
            for f in os.listdir(DIR):
                try:
                    if os.path.getsize(DIR + "/" + f) > 1:
                        size_check += 1
                        print(f, " written to disk")
                    except:
                        print(f, "sleep")
        time.sleep(10)        
        break

os.chdir(DIR)
df = pd.DataFrame()
while True:
    try:
        for f in os.listdir(DIR):
            data = pd.read_excel(f)
            # perform any other data manipulation needed here.
            df = df.append(data) # our downloaded files are read into one appended dataframe
    except:
        print("---->ATTENTION<---- Code error appending data. Adjust sleep var")
        sys.exit(1)
        # todo: something better than that
    break

df = df.reset_index(drop=True)
# perform any other steps to df now.