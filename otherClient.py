import socket, select, string, sys
from board import *

board = 0
pi = False
matrix = None

def prompt() :
    sys.stdout.write('> ')
    sys.stdout.flush()
 
if __name__ == "__main__":
     
    if(len(sys.argv) < 4) :
        print 'Usage : python client.py (pi|reg) hostname port'
        sys.exit()
     
    if sys.argv[1] == 'pi':
        pi = True
        from rgbmatrix import Adafruit_RGBmatrix
        matrix = Adafruit_RGBmatrix(32, 1)

    host = sys.argv[2]
    port = int(sys.argv[3])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((host, port))
    except:
        while 1:
            try :
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((host, port))
                break
            except :
                print 'Unable to connect'
     
    print 'Connected to remote host. Start sending messages'
    prompt()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
        for sock in read_sockets:
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    try:
                        board = int(data.strip())
                        print ""
                        if pi:
                            ledBoard(matrix, board)
                        drawBoard(board)
                    except ValueError:
                        pass
                    prompt()
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()
                
