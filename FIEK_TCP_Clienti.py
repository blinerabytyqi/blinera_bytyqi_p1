import socket
 
host = "127.0.0.1"
port = 12000
BUFFER_SIZE = 2000

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
    tcpClient.connect((host, port))
    while True:
        MESSAGE = input("Mesazhi: ")
        tcpClient.send(MESSAGE.encode("ASCII"))     
        data = tcpClient.recv(BUFFER_SIZE).decode("ASCII")
        
        print("Serveri: "+data)
        
        
except ConnectionRefusedError:
    print("Serveri nuk eshte i startuar!")

except ConnectionResetError:
    print("Serveri ka ndaluar!")

except ConnectionAbortedError:
    print("Lidhja eshte shkeputur!")
tcpClient.close()
