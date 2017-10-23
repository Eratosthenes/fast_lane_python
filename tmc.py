import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = int(sys.argv[1])
s.connect((host,port))

s.send(sys.argv[2])

i = 0
while(1):
  data = s.recv(1000000)
  i += 1
  if i<5:
    print(data)
  if not data:
    break
  print('received ',str(len(data)),' bytes')

s.close()




