import socket
import datetime


def terminal():
    cmd = input("> ")

    def gethost():
        hostname = socket.gethostname()
        host = socket.gethostbyname(hostname)
        print("Host Name: " + hostname)
        print("Host IP: " + host)

    def echo(text):
        print(text)

    def systeminfo():

        hostname = socket.gethostname()

        print("Host OS: PTSD DOS Revision 3.1.2")
        print("Host Name: " + hostname)

    def ver():
        print("PTSD DOS CMD-PROMPT VER 4! NO REVISION!")

    def printdate():
        print(datetime.date.today())

    if cmd == "echo":
        a = input(">Text To Echo?: ")
        echo(a)
    elif cmd == "system info":
        systeminfo()
    elif cmd == "get host":
        gethost()
    elif cmd == "date":
        printdate()
    elif cmd == "ver":
        ver()
    elif cmd == "dingus":
        printdate()
        gethost()
        ver()
        systeminfo()
        echo("impossible")
        a = float and int or str is False
        print(a)


while True:
    terminal()
