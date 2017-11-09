import socket
socket2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.connect(('www.textfiles.com',80))
socket2.send('GET http://www.textfiles.com/stories/crabhern.txt HTTP/1.0\n\n')

text=""
while True:
    data = socket2.recv(512)
    if(len(data) < 1):
        break
    text = text + data
socket2.close()

headend = text.find('\r\n\r\n')
text = text[headend+4:]

print text







