#!/usr/local/bin/python3

import requests
import hashlib

targetURL = "192.168.1.16"
dictionnary = open("common.txt", "r")
hashobj4 = hashlib.sha256()

def request(url, p):
    try:
        return requests.get("http://" + url, params=p)
    except requests.exceptions.ConnectionError:
        pass 

print("Starting ... \n")

for line in dictionnary:
    word = line.strip()
    fullUrl = targetURL + "/index.php"
    
    # hashobj4.update(word.encode())
    # params = {'page': str(hashobj4.hexdigest())}

    params = {'page': str(word)}
    
    response = request(fullUrl, params)
    if response:
        x = str(response.content).split('</script>')[0]
        pattern = "<script>alert(\\'Wtf ?\\');"
        # print(response.request.url)
        if str(pattern) not in x:
        #     print("[+] Nothing new at : " + response.request.url)
        # else:
             print("[+] Discovery at : " + response.request.url)
  
        
print("\nDone")

# http://192.168.1.16/index.php?page=survey
# http://192.168.1.16/index.php?page=media&src=nsa
# http://192.168.1.16/index.php?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c
# e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c => SHA256 => TAMERE
