import socket
import time

socket3=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket3.connect(('www.abdulkalam.com',80))
socket3.send('GET http://www.abdulkalam.com/kalam/theme/assets/img/kalamimages/04%20Homepage_img.jpg HTTP/1.0\n\n')

picture=""
while True:
    data = socket3.recv(5120)
    if(len(data) < 1):
        break
    #time.sleep(0.25)
    picture = picture + data

socket3.close()


headend = picture.find('\r\n\r\n')
print 'Header:'
print picture[:headend]
print 'Length:',headend

picture = picture[headend+4:]


handler1 = open('kalam.jpg','wb')
handler1.write(picture)
handler1.close()











