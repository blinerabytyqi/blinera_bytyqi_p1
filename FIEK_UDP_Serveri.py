from socket import *
from datetime import datetime
import random
from math import sqrt


udp_port = 12000
host = "127.0.0.1"

serverSocket = socket(AF_INET, SOCK_DGRAM)

print("|=======================================|")
print("|           UDP Serveri                 |")
print("|=======================================|")

# Mundeson qe cdo IP-adrese te kete mundesi te lidhet ne server permes portit 12000
serverSocket.bind(('',udp_port))
print("\nServeri shërben në portin %s" %(udp_port))


print("\n\nServeri i gatshem per sherbim...")

while True :
    try:
        data,adresa = serverSocket.recvfrom(128)
        data = data.decode("ASCII")
        data = data.lower()
        print("\nKerkesa e klientit: ", data)

        ipKlientit = adresa[0]
        portiKlientit = adresa[1]
        hosti = gethostname()
               
        pergjigja = "Pershendetje!"

        def IpAddr():
            pergjigja = "IP Addresa e klientit eshte: %s" % (ipKlientit) 
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def portNr():
            pergjigja = "Porti i klientit eshte: %s" % (portiKlientit)
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def bashketingellore():
            nrBashketingelloreve = 0
            bashketingelloret = ['B', 'C', 'ร', 'D', 'Dh', 'F',	'G', 'Gj', 'H', 'J', 'K', 'L', 'LL', 'M', 'N',
                   'Nj', 'P', 'Q',	'R', 'RR', 'S', 'Sh', 'T', 'TH', 'V', 'X', 'XH', 'Z', 'Zh', 'b', 'c', 'รง', 'd', 'dh',
                  'f', 'g', 'gj', 'h', 'j', 'k', 'l', 'll', 'm' , 'n', 'nj', 'p', 'q', 'r', 'rr', 's', 'sh', 't', 'th',
                  'v','x', 'xh', 'z', 'zh']
            try:
                teksti = data[data.index(' '):]
                for i in range(0, len(teksti)):
                    if(teksti[i] in bashketingelloret):
                       nrBashketingelloreve += 1
                pergjigja = "Numri i bashketingelloreve te tektit "+teksti+" permban "+str(nrBashketingelloreve)+" bashketingellore."
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
            except ValueError:
                pergjigja = "Kerkesa juaj nuk permbane tekst(ex. bashketingellore KOMPJUTERIKA)."
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def printimi():
            try:
                teksti = data[data.index(' '):].strip()
                pergjigja = str(teksti)
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
            except ValueError:
                pergjigja = "Kerkesa juaj nuk permbane tekst(ex. printo KOMPJUTERIKA)."
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def host():
            pergjigja = "Hosti eshte: %s" % (hosti)
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def koha():
            pergjigja = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def loja():
            loja1 = []
            for i in range(0,7):
                number = random.randint(1,49)
                loja1.insert(i, number)
            pergjigja = str(loja1)
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        def fibonacci():
            try:
                number = int(data[data.index(' '):])
                def F(n):
                    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
                if number == 0:
                    f = 0
                    pergjigja = str(f)
                    serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
                elif number == 1:
                    f = 1
                    pergjigja = str(f)
                    serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
                else:
                    f = F(number-1)+F(number-2)
                    f = int(f)
                    pergjigja = str(f)
                    serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
            except ValueError:
                pergjigja = "Kerkesa juaj nuk permbane numer(ex. fibonacci 15)."
                serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        
                    
        def instructions():
            pergjigja = "Metodat e serverit\n\nMetoda:\t\tPershkrimi\t\t\t\t\tSintaksa:"\
                        "\n\nIpAddr\t\tKthen IP Adresen e klientit\t\t\tIP (ip)"\
                        "\nPortNr\t\tKthen Portin e klientit\t\t\t\tPORT (port)"\
                        "\nBashketingellore\t\tGjene numrin e bashketingelloreve ne tekst\t\tBashketingellore{hapesire}Teksti (bashketingellore{hapesire}Teksti)"\
                        "\nPrinto\t\tShtyp fjalin e derguar\t\t\t\tPRINTO{hapesire}Teksti (printimi{hapesire}Teksti)"\
                        "\nHost\t\tKthen emrin e hostit\t\t\t\tHOST (host)"\
                        "\nKoha\t\tKthen kohen aktuale ne server\t\t\tTIME (koha)"\
                        "\nLoja\t\tKthen 7 numra te rastesishem nga 1 deri 49\tLOJA (loja)"\
                        "\nFibonacci\tGjene numrin Fibonacci nga numri i dhene\tFIBONACCI{hapesire}numri (fibonacci{hapesire}numri)\n\n"
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)


        if data == 'ip':
            IpAddr()
        elif data == 'port':
            portNr()
        elif data.split(' ')[0] == 'bashketingellore':
            bashketingellore()                    
        elif data.split(' ')[0] == 'printimi':
            printimi()
        elif data == 'host':
            host()
        elif data == 'koha':
            koha()
        elif data == 'loja':
            loja()
        elif data.split(' ')[0] == 'fibonacci':
            fibonacci()
        elif data == 'instructions':
            instructions()
        elif type(data) =="NULL":
            pergjigja = "Sintaksa juaj eshte GABIM! SHENONI INSTRUCTIONS!!"
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
        else:
            pergjigja = "Sintaksa juaj eshte GABIM! SHENONI INSTRUCTIONS!!"
            serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
    except SyntaxError:
        pergjigja = "Serveri nuk ka startuar!"
        serverSocket.sendto(pergjigja.encode("ASCII"),adresa)
