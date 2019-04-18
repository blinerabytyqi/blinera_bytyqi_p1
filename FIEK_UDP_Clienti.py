from socket import *

host = "127.0.0.1"
port = 12000


udpClient = socket(family=AF_INET, type=SOCK_DGRAM)
udpClient.settimeout(5)


while True:
    try:
        kerkesa=input("Kerkesa :")
        udpClient.sendto(kerkesa.encode("ASCII"),(host,port))
        pergjigja, addressa = udpClient.recvfrom(2048)
        print("Serveri: "+pergjigja.decode("ASCII"))
    except ConnectionError:
        print("\tNuk u mundesua lidhja me serverin")
    except TimeoutError:
        print("\tKerkesa deshtoi te dergohej brenda 5 sekondave")
connectionSocket.close()

clientSocket = socket(family=AF_INET, type=SOCK_DGRAM)
clientSocket.settimeout(5)
 