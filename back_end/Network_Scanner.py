import scapy.all as scapy
import argparse


#Network Scanner in Python : 
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Sepcify target ip or ip range")
    options = parser.parse_args()
    if not options.target:
        #Code to handle if interface is not specified
        parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list

def print_result(scan_list):
    print("IP\t\t\tMAC\n----------------------------------------")
    for client in scan_list:
        print(client["ip"] + "\t\t" + client["mac"])


ssc = scan('192.168.1.1/24')
print_result(ssc)