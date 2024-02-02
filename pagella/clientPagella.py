import socket,json
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 22224
BUFFER_SIZE = 1024


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("connesso a: ", ((SERVER_ADDRESS, SERVER_PORT)))
while True:
    comando = input("Inserisci il comando: ")
    messaggio = {
        "comando":comando
    }
    messaggio = json.dumps(messaggio)
    sock.sendall(messaggio.encode("UTF-8"))
    data = sock.recv(BUFFER_SIZE)
    print("Risultato:", data.decode())
    risp=input("se non vuoi fare altre operazioni digita 'n'==no ")
    if(risp=='n'):
        print("chiusura della connessione col server")
        break