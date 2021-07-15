from socket import getservbyport

output = open("ans.txt",  "w")

temp = set()
opentemp = set()

with open("feb28_nmap.txt", "r") as f:
    for line in f:
        split = line.split()
        length = len(temp)
        if split[10] == '[SYN,' and split[11] == 'ACK]':
            port_num = split[7]
            if port_num not in opentemp:
                opentemp.add(port_num)
                state = 'opened'
                service = getservbyport(int(port_num))
                output.write(port_num + '/tcp \t' + state + '\t' + service + '\n')
            
with open("feb28_nmap.txt", "r") as f:
    for line in f:
        print("hello")
        split = line.split()
        length = len(temp)
        if split[10] == '[SYN]':
            port_num = split[9]
            if port_num not in opentemp:
                opentemp.add(port_num)
                state = "filtered"
                service = getservbyport(int(port_num))
                output.write(port_num + '/tcp \t' + state + '\t' + service + '\n') 
output.close()
