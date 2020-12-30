#!/usr/local/bin/python3

import requests

targetURL = "192.168.1.16"
dictionnary = open("common.txt", "r")

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass 

print("Starting ... \n")

for line in dictionnary:
    word = line.strip()
    fullUrl = targetURL + "/whatever/" + word
    response = request(fullUrl)
    if response:
        print("[+] Discovery At : " + fullUrl)

print("\nDone")

# Output :

# [+] Discovery At : 192.168.1.16/
# [+] Discovery At : 192.168.1.16/admin
# [+] Discovery At : 192.168.1.16/favicon.ico
# [+] Discovery At : 192.168.1.16/index.php
# [+] Discovery At : 192.168.1.16/robots.txt
# [+] Discovery At : 192.168.1.16/whatever