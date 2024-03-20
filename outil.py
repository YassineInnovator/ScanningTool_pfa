import nmap # type: ignore
import os
import socket

sc = nmap.PortScanner()


#----------------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '112.13.2.1'
def PortScanner(port):
    if s.connect_ex((host, port)):
        print("open")
    else:
        print("close")   
        
import requests

def check_headers(url):
    response = requests.get(url)
    headers = ['Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options', 'X-Content-Type-Options', 'Referrer-Policy', 'Permissions-Policy']

    for header in headers:
        print(f"{header}: {'Present' if header in response.headers else 'Missing'}")


            
        
def Scanernmap(opt):
    if opt == '1':
        ip = input("\nEnter the IP address you want to scan:")  # Enter the IP address you want to scan
        print("Nmap version: ", sc.nmap_version())
        sc.scan(ip, '1-1024', ' -v -sS')
        print(sc.scaninfo())
        print("Ip Status: ", sc[ip].state())
        print(sc[ip].all_protocols())
        print("Open Ports: ",sc[ip]['tcp'].keys())
    elif opt =='2':
        ip = input("\nEnter the IP address you want to scan:")  # Enter the IP address you want to scan
        print("Nmap version: ", sc.nmap_version())
        sc.scan(ip, '1-1024', ' -v -sU')
        print(sc.scaninfo())
        print("Ip Status: ", sc[ip].state())
        print(sc[ip].all_protocols())
        print("Open Ports: ",sc[ip]['tcp'].keys())
    elif opt =='3':
        ip = input("\nEnter the IP address you want to scan:")  # Enter the IP address you want to scan
        print("Nmap version: ", sc.nmap_version())
        sc.scan(ip, '1-1024', ' -v -sS -sV -sC -A -O')
        print(sc.scaninfo())
        print("Ip Status: ", sc[ip].state())
        print(sc[ip].all_protocols())
        print("Open Ports: ",sc[ip]['tcp'].keys())
          
#-----------------------------------------------
    
def main():
    check_headers('http://www.example.com')
    """ n=input("1- Network scaner\n2- Vulnerabiliter Detection \n3- Exploit\n\nPlease entre a number : ")
    
    if n == '1':
        nmap()
    if n == '2':
        vuln()
    if n == '3':
        os.system('msfconsole')
    else:
        print('ereur!!')     """
        
   
def nmap():
    ip = input("\nEnter the IP address you want to scan:")  # Enter the IP address you want to scan
    sc.scan(ip, '22-443')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())

def vuln():
    ip = input("\nEnter the IP address you want to scan:")  # Enter the IP address you want to scan
    print(os.system('nmap -sV --script=vulscan.nse ' +ip))

if __name__=='__main__':
    #print("""Outil de scan""")
    main()