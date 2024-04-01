# Anti-virus-Rasp-Zero-w


@Mr_LuzSec10010


This is a Python script for scanning a Windows system for infected files. It calculates the MD5 hash of each EXE and DLL file in the C: drive and checks it against a list of virus hashes stored in a text file called "VirusLIST.txt". If a match is found, the file is marked as infected and added to a list of infected files. At the end of the scan, the script prints the number of infected files and their names. If no infected files are found, it prints a message indicating that the system is clean.




main.py its main file. the work of the main.py is scan the hole pc and after completed then colledt the all hash value and save it VirusLIST.txt


in the Plug and Play project i decided to make a antivirus payload that can be run on raspberry pi zero w. raspberry pi zero w its IOT device that work for automation task, 

in the raspberry zero w i use a os its a kali linuc thats use for offensive security, or penetration testing by the security engineer, 

in the project i use P4wnp1 toolkit, its alos know as A.L.O.A (A Little Offensive Appliance), in the toolkit alos be used for IOT-related tasks, such as exploiting vulnerabilities reconnaissance,scanning,exploiting

Plug&Play Features :-  •	Penetration testing and ethical hacking and Bug Bounty
                  •	Post-exploitation and privilege escalation
                 •	Data exfiltration and reconnaissance
                •	Red teaming and blue teaming
                
Uses :- •	Penetration testing and ethical hacking and Bug Bounty
       •	Post-exploitation and privilege escalation
       •	Data exfiltration and reconnaissance
       •	Red teaming and blue teaming

      

How to Boot raspberry pi zero w ?
•	Flash a compatible Kali Linux OS image onto a MicroSD card.
•	Download the   P4wnP1 A.L.O.A firmware and configuration files.
•	Modify the configuration file to suit your needs.
•	Flash the firmware onto the Raspberry Pi Zero W using the USB OTG port.( Card Reader)

The easiest way to access a raspberrypi zero w (P4wnP1 A.L.O.A.)  installation is to use the web client via the spawned WiFi (the PSK is MaMe82-P4wnP1, the URL http://172.24.0.1:8000) or SSH (default username root  password toor)

   (P4wnP1 A.L.O.A.)functions:
                                 USB Ethernet (RNDIS and CDC ECM)
                                 USB Serial
                                 USB Mass Storage (Flashdrive or CD-Rom)
                                 HID Keyboard
                                 HID Mouse


How to scan pc and detect the Virus ?


first you need to boot raspberry pi zero w (P4wnp1 A.L.O.A) wait for 10  or 20 sec to need to boot 
then connect through wifi,and also use browser to communicate with the (P4wnP1 A.L.O.A.) via a ip.



