import socket
import threading
import ipaddress
import time
import platform
import os
import requests
import whois
import dns.resolver
from colorama import Fore, Style, init

init(autoreset=True)


ascii_art = f"""
{Fore.RED}╭╮╭╮╭┳━━━┳━━━┳━━━┳━━━╮
{Fore.GREEN}┃┃┃┃┃┃╭━╮┃╭━╮┣╮╭╮┃╭━━╯
{Fore.RED}┃┃┃┃┃┃┃╱┃┃┃╱┃┃┃┃┃┃╰━━╮
{Fore.GREEN}┃╰╯╰╯┃┃╱┃┃┃╱┃┃┃┃┃┃╭━━╯
{Fore.RED}╰╮╭╮╭┫╰━╯┃╰━╯┣╯╰╯┃╰━━╮
{Fore.GREEN}╱╰╯╰╯╰━━━┻━━━┻━━━┻━━━╯
{Fore.BLUE}       ATTEMPT TO INFILTRATE NETWORKS
{Fore.YELLOW}       ===============================
{Fore.BLUE}       TOOLS BY </> WOODE
{Fore.RED}      TELE </> @c249c
{Fore.YELLOW}       =======================
"""
print(ascii_art)



if __name__ == "__main__":
    while True:
        print(f"{Fore.GREEN} MENU -»")
        print(f"{Fore.BLUE}=======================")    
        print(f"{Fore.CYAN}1.{Fore.WHITE} SCAN SINGLE PORT IN CIDR")
        print(f"{Fore.CYAN}2.{Fore.WHITE} PING AN IP")
        print(f"{Fore.CYAN}3.{Fore.WHITE} WHOIS LOOKUP")
        print(f"{Fore.CYAN}4.{Fore.WHITE} DNS LOOKUP")
        print(f"{Fore.CYAN}5.{Fore.WHITE} HTTP HEADER FETCH")
        print(f"{Fore.CYAN}6.{Fore.WHITE} PORT RANGE SCAN")
        print(f"{Fore.CYAN}7.{Fore.WHITE} REVERSE DNS LOOKUP")
        print(f"{Fore.CYAN}8.{Fore.WHITE} EXIT")
        print(f"{Fore.BLUE}=======================")

        choice = input(f"{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}")

        if choice == '1':
            cidr = input(f"{Fore.YELLOW}Enter IP CIDR blocks (e.g., 192.168.0.0/24): {Style.RESET_ALL}")
            port = int(input(f"{Fore.YELLOW}Enter port to scan: {Style.RESET_ALL}"))
            scan_network(cidr, port)
        elif choice == '2':
            ip = input(f"{Fore.YELLOW}Enter IP address to ping: {Style.RESET_ALL}")
            ping_target(ip)
        elif choice == '3':
            domain = input(f"{Fore.YELLOW}Enter domain for WHOIS lookup: {Style.RESET_ALL}")
            get_whois_info(domain)
        elif choice == '4':
            domain = input(f"{Fore.YELLOW}Enter domain for DNS lookup: {Style.RESET_ALL}")
            dns_lookup(domain)
        elif choice == '5':
            url = input(f"{Fore.YELLOW}Enter URL to fetch HTTP headers: {Style.RESET_ALL}")
            fetch_http_headers(url)
        elif choice == '6':
            ip = input(f"{Fore.YELLOW}Enter IP address for port range scan: {Style.RESET_ALL}")
            start_port = int(input(f"{Fore.YELLOW}Enter start port: {Style.RESET_ALL}"))
            end_port = int(input(f"{Fore.YELLOW}Enter end port: {Style.RESET_ALL}"))
            port_scan_range(ip, start_port, end_port)
        elif choice == '7':
            ip = input(f"{Fore.YELLOW}Enter IP address for reverse DNS lookup: {Style.RESET_ALL}")
            reverse_dns_lookup(ip)
        elif choice == '8':
            print(f"{Fore.RED}Exiting... Goodbye!")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.")