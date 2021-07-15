import os
import subprocess

website = input("what website would you like to check : ")
portlist = input("what port would you like to check ")
portlist = portlist.split(",")

tcpdump = subprocess.Popen(["sudo", "tcpdump" "-w", "output5.pcap"])

for port in portlist:
    command = "nc -w 1" + website + " " + port
    os.system(command)

time.sleep(2)
tcpdump.terminate()
time.sleep(1)

os.system(sudo shark -r output5.pcap > output5.txt)