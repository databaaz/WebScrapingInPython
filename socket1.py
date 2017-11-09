import socket
socket1=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(('www.textfiles.com',80))
socket1.send('GET http://www.textfiles.com/stories/aminegg.txt HTTP/1.0\n\n')
while True:
    data = socket1.recv(512)
    if(len(data) < 1):
        break
    print data

socket1.close()

