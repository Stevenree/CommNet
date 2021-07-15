import os
import subprocess

os.system ("tshark -2 -R \" ssl.handshake.type == 1\" -r num4.pcap -w out4.pcap -e ip.src -e ip.dst -T fields -e tls.handshake.extensions_server_name > ServerNames.txt")

output = open("ans.txt",  "w")

temp = set()

with open("ServerNames.txt", "r") as f:
    for line in f:
        split = line.split()
        num1 = len(temp)
        temp.add(split[1])
        num2 = len(temp)
        if (split[1] == '51.222.39.185'):
            break
        elif num1 != num2:
            print(split[1])
            #x = subprocess.check_output(f'whois {split[1]}', shell = True)
            x = subprocess.check_output(f"whois {split[1]}|grep Organization:", shell = True)
            x = x.decode("utf-8")
            x = x.split("\n")
            x = x[0] #took the first organization
            x = x[13:] # take out organization:
            output.write(line[:-1] + " " + x + "\n")
output.close()