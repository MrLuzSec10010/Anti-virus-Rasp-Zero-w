# Anti-virus-Rasp-Zero-w


@Mr_LuzSec10010


This is a Python script for scanning a Windows system for infected files. It calculates the MD5 hash of each EXE and DLL file in the C: drive and checks it against a list of virus hashes stored in a text file called "VirusLIST.txt". If a match is found, the file is marked as infected and added to a list of infected files. At the end of the scan, the script prints the number of infected files and their names. If no infected files are found, it prints a message indicating that the system is clean.


