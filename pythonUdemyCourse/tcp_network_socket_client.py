import socket as s

host = s.gethostname()
port = 9337

sk = s.socket(s.AF_INET, s.SOCK_STREAM)
sk.connect((host,port))
msg = sk.recv(1024)
sk.close()
print(f"Connection estabilished with: {str(msg.decode('ascii'))}")