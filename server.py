import socket, select
from board import *

board = 0
last = ()
lastType = ' '

def convert(num):
    return (int(num) - 1) * 2

def broadcast_data (sock, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                socket.close()
                CONNECTION_LIST.remove(socket)
 
if __name__ == "__main__":
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 5009
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)
 
    CONNECTION_LIST.append(server_socket)
 
    print "Tic Tac Toe server started on port " + str(PORT)
 
    while 1:
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                #broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        s = data
                        if (sock.getpeername() != last):
                            if lastType == 'x':
                                lastType = 'o'
                            elif lastType == 'o':
                                lastType = 'x'
                            elif lastType == ' ' and last == ():
                                lastType = 'x'
                            elif last != ():
                                lastType = 'o'
                            print str(sock.getpeername()) + ' played ' + lastType + ' on ' + s
                            if lastType == 'x':
                                board = board | (1 << (convert(s)))
                            elif lastType == 'o':
                                board = board | (1 << (convert(s) + 1))
                            if (winner(board) != ' '):
                                board = 0
                                drawBoard(board)
                            broadcast_data(sock, "\r" + str(board))
                            drawBoard(board)
                            last = sock.getpeername()
                            read_sockets[0].send(str(board))
                        else:
                            print 'Not their turn'

                except:
                    #broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
     
    server_socket.close()
