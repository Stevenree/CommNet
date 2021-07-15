import os
import subprocess
import signal
import time
from socket import getservbyport

website = input("what website would you like to check : ")
portlist = input("what port would you like to check ")

portlist = portlist.split(",")

tcpdump = subprocess.Popen(['sudo', 'tcpdump', 'tcp', '-w', 'output5.pcap'])

time.sleep(1)

for port in portlist:
    command = "nc -w 1 " + website + " " + port
    os.system(command)

time.sleep(1)

tcpdump.terminate()
#os.killpg(os.getpgid(tcpdump.pid), signal.SIGTERM)

time.sleep(1)
open("output5.txt",  "w")

os.system("sudo tshark -r output5.pcap > output5.txt")

output = open("ans5.txt",  "w")

temp = set()

opentemp = set()

with open("output5.txt", "r") as f:
    for line in f:
        split = line.split()
        length = len(temp)
        if split[5] == 'TCP':
            if split[10] == '[SYN,' and split[11] == 'ACK]':
                port_num = split[7]
                if port_num not in opentemp:
                    opentemp.add(port_num)
                    state = 'opened'
                    service = getservbyport(int(port_num))
                    output.write(port_num + '/tcp \t' + state + '\t' + service + '\n')
            
with open("output5.txt", "r") as f:
    for line in f:
        split = line.split()
        length = len(temp)
        if split[5] == 'TCP':
            if split[10] == '[SYN]':
                port_num = split[9]
                if port_num not in opentemp:
                    opentemp.add(port_num)
                    state = "filtered"
                    service = getservbyport(int(port_num))
                    output.write(port_num + '/tcp \t' + state + '\t' + service + '\n') 
output.close()