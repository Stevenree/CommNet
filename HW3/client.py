import requests
import sys
import json

def function(msg_list):
    command = input("New input: ")
    if command == "quit":
        return
    else:
        print('hello')
        if command == 'refresh':
            resp = requests.get(f'http://{server}/?user={user}')
            json_msg = resp.json()
            messages = json_msg['all_messages']
            msg_count = 0

            for msg in messages:
                if msg not in msg_list:
                    msg_list.append(msg)
                    print(msg['sender'] + " " + msg['message'] + '\n')
                    msg_count += 1

            if msg_count == 0:
                print("no new message")

            function(msg_list)
        else:
            temp = command.split(':')
            print(temp)
            if temp[0] == 'send':
                print(temp[2])
                data_dict = {'sender': user, 'receiver': temp[1], 'message': temp[2]}
                requests.post(f'http://{server}', data = data_dict)
                function(msg_list)
            else:
                print('Error, please input valid command: (send, refresh or quit)')
                function(msg_list)
    return


server = sys.argv[1]
print("Server: "+ server)

user = input("Enter the user: ")
resp = requests.get(f'http://{server}/?user={user}')
json_msg = resp.json()
messages = json_msg['all_messages']
message_list =[]
msg_count = 0
print ("length of dict: " + str(len(messages)))


for msg in messages:
    message_list.append(msg)
    print(msg['sender'] + " " + msg['message'] + '\n')
    msg_count += 1

if msg_count == 0:
    print("No messages")
function(message_list)

