import socket
import json
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 22224
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((SERVER_ADDRESS, SERVER_PORT))

dizionario = { 'Antonio Barbera': [   ['Matematica', 8, 1],
                           ['Italiano', 6, 1],
                           ['Inglese', 9.5, 0],
                           ['Storia', 8, 2],
                           ['Geografia', 8, 1]],
    'Giuseppe Gullo': [   ['Matematica', 9, 0],
                          ['Italiano', 7, 3],
                          ['Inglese', 7.5, 4],
                          ['Storia', 7.5, 4],
                          ['Geografia', 5, 7]],
    'Nicola Spina': [   ['Matematica', 7.5, 2],
                        ['Italiano', 6, 2],
                        ['Inglese', 4, 3],
                        ['Storia', 8.5, 2],
                        ['Geografia', 8, 2]]}

print("server in attesa di messaggi..")
while True:
    data=sock.recv(1024)
    if not data:
        break
    data=data.decode()
    data = json.loads(data)

    comando = data['comando']
    parametri = data['parametri']

    print("comando: ", comando)
    print("parametri: ", parametri)