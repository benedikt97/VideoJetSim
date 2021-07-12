#!/usr/bin/python3

import socket;
import sys;
import time;
import os;
from datetime import datetime;


HOST = '192.168.10.21'
dummy = True

def ownip():
    connection=socket.socket()
    connection.connect(("google.de",int(80)))
    own = (connection.getsockname()[0])
    connection.close()
    print("Your IP is ", own)
    return own

def clearTerm():
    os.system('clear')

def printVJtext(data):
    print(data.hex())
    print(" ________________________________________________________")
    stri = data.replace(b'\r', b'\x43'b'\x52')                          # CR
    stri = stri.replace(b'\x18', b'\x43'b'\x4C'b'\x52'b'\x20')          # 'CLR' SP
    stri = stri.replace(b'\x00', b'\n'b'\x20'b'\x20'b'\x20'b'\x20')     # CR SP SP SP SP
    stri =stri.decode('UTF-8')
    print(stri)


def printHeader():
    print(" ________________________________________________________")
    print("                VJ Text Received at PORT", PORT, "        ")
    print("               ",datetime.now(),"         ")
    print(" ________________________________________________________")

def printMain():
    print(" ________________________________________________________")
    print("|        VideoJet TCP Printer Simulation / HeuserB       |") 
    print("|________________________________________________________|",)
    print("|            IP Adress:", HOST,":", PORT,"            |")
    print("|________________________________________________________|")
    print("")


def replyVJ(data):
    if data.find(b'\x18'):
        print ("Buffer Cleared")





def main():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
                conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                conn.bind((HOST, PORT))
                conn.listen()
                conn, addr = conn.accept()
                clearTerm()
                printMain()
                print("Not Connected")
                with conn:
                    while True:     
                        data = conn.recv(1024)
                        if not data: 
                            raise ValueError('Connection Closed by Remote Partner')
                        #replyVJ(data)
                        clearTerm()
                        printMain()
                        printHeader()
                        printVJtext(data)
        except Exception as e:
            clearTerm()
            printMain()
            print(" ________________________________________________________")
            print("               ",datetime.now(),"         ")
            print("Error:", e, "        ")
            print(" ________________________________________________________")
            time.sleep(1)
            





if __name__ == "__main__": 
    
    HOST = '172.16.45.100' #ownip()
    PORT = int(sys.argv[1])
    clearTerm()
    printMain()
    main()
            
                        
