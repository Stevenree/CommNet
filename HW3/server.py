from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import cgi
import sqlite3
import json

log = sqlite3.connect('messages.db')
cur = log.cursor()
cur.execute("create table if not exists log (sender,receiver,message)")
#def insert_value(a,b,c,tab):
#    tab.execute("insert into [Table] values (?, ?, ?)" (a,b,c))
#    table.commit()

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'GET'}
        )
        dict_user = parse_qs(self.path[2:])
        if 'user' in dict_user.keys():
            current_user = dict_user['user'][0]
            print(dict_user)
            output = []
            for row in cur.execute('SELECT * FROM log WHERE receiver=?', (current_user,)):
                send = row[0]
                msg = row[2]
                person = {'sender': send, 'message': msg}
                output.append(person)
            
        output_dic = {'username': dict_user['user'][0], 'all_messages': output}
        person_json = json.dumps(output_dic) 
        self.wfile.write(person_json.encode())

        #self.wfile.write(b"<html><body><h1>Get Request Received!</h1></body></html>")
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        #print(form.getvalue("sender"))
        #print(form.getvalue("receiver"))
        #print(form.getvalue("message"))
        sender = str(form.getvalue("sender"))
        receiver = form.getvalue("receiver")
        message = form.getvalue("message")
        cur.execute("INSERT INTO log (sender, receiver, message) VALUES(?,?,?)", (sender, receiver, message))
        log.commit()

        self.wfile.write(b"<html><body><h1>POST Request Received!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Server running at localhost:8088...')
    httpd.serve_forever()

run()