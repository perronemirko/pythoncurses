import socket as s

host = s.gethostname()
port = 9337

sk= s.socket(s.AF_INET, s.SOCK_STREAM)
sk.bind((host,port))
sk.listen(1)

conn,addr = sk.accept()

print(f"Connection estabilished with: {str(addr)}")

msg = f"Thank you for connecting {str(addr)}"
conn.send(msg.encode("ascii"))
conn.close()