import socket
import  cv2
import  pickle
import struct
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 2134
s_add  = ('192.168.90.134',port)
s.bind(s_add)
s.listen(5)

while True:
    client,addr = s.accept()
    if client:
        cap = cv2.VideoCapture(0)
        while(cap.isOpened()):
            ret,photo = cap.read()
            p = pickle.dumps(photo)
            mess = struct.pack("Q",len(p))+p
            client.sendall(mess)
            cv2.imshow('Live Video',photo)
            if cv2.waitKey(10) == 13:
                client.close()
cv2.destroyAllWindows()
