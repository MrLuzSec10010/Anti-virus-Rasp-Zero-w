import os
import hashlib
import sys
import time
from keyboard import layout

# Set the keyboard layout to US
layout('us')

file_list = []

rootdir = "C:/"

print("Program starting!")
print("[+]Collecting virus definitions and allocating memory[+]")

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".exe") or filepath.endswith(".dll"):
            file_list.append(filepath)
            #print(filepath)

print("[+]Virus definition and memory allocation complete...[+]")
print("[+]Starting scan...[+]")

def countdown():
    for x in range(4):
        print(x+1)
        time.sleep(1)

countdown()

def Scan():
    infected_list = []
    for f in file_list:
        virus_defs = open("VirusLIST.txt", "r")
        file_not_read = False
        print("\nScanning: {}".format(f))
        hasher = hashlib.md5()
        try:
            with open(f, "rb") as file:
                while chunk := file.read(4096):
                    hasher.update(chunk)
                    file_hash = hasher.hexdigest()
                    virus_defs.seek(0)
                    for line in virus_defs:
                        if line.strip() == file_hash:
                            print(f"\n\n[+]Virus detected: {f}.\n")
                            infected_list.append(f)
                            file_not_read = True
                            break
                    if file_not_read:
                        break
        except FileNotFoundError:
            print("\n[+]Virus definition file not found. Skipping...\n")

    if infected_list:
        print("\n[+]Infected files:\n")
        for file in infected_list:
            print(file)
    else:
        print("\n[+]No viruses detected.\n")

Scan()
