#!/usr/local/bin/python3


# USAGE : set the correct IP address before running that script

import requests
from html.parser import HTMLParser

global tmpURLs
tmpURLs = []
global readmeURLs
readmeURLs = []
global rootURL
rootURL = "http://192.168.1.25/.hidden/"
global merge
merge = []

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value != "../" and value != "README":
                        tmpURLs.append(value)
                # elif name == "href" and value == "README":
                #     readmeURLs.append(value)

parser = MyHTMLParser()
global errorGet
errorGet = 0

def sendGetRequest(u):
    
    global errorGet
    
    try:
        return requests.get(u)
    except requests.exceptions.ConnectionError:
        errorGet += 1
    
def readmeURLBuilder(tab):
    
    for href in tab:
        tmp =  rootURL + href
        res = sendGetRequest(tmp)
        if res:
            body = str(res.content)
            parser.reset()
            parser.feed(body)
            

def mergeDeep1AND2(dup1, dup2):
    global merge
    
    for indexA, a in enumerate(dup1):
        for indexB, b in enumerate(dup2):
            if indexB // 26 == indexA:
                merge.append(a + b)
        readmeURLs.append(a)

def mergeDeep2AND3(merge, dup3):
    
    output = []
    for indexA, a in enumerate(merge):
        for indexB, b in enumerate(dup3):
            if indexB // 26 == indexA:
                output.append(a + b)
        readmeURLs.append(a)
    return output
    
def returnContent(output):
    filter = []
    for u in output:
        res = sendGetRequest(rootURL + u + "README")
        if res:
            filter.append(str(res.content))
    return set(filter) 

def init():
    
    global tmpURLs
    global merge
    
    print("1.1 Building every URLs possible ...")
    res = sendGetRequest(rootURL)
    body = str(res.content)
    parser.feed(body)
    
    # Nested 1
    dup1 = tmpURLs
    tmpURLs = []
    readmeURLBuilder(dup1) # deep1 = ["azgh/", "dfgshsgdf/", ...]
    dup2 = tmpURLs
    tmpURLs = []
    mergeDeep1AND2(dup1, dup2) # Feed "merge" object
    # Nested 2
    tmpURLs = []
    readmeURLBuilder(merge) # deep2 = ["azgh/dsfghjdh/", "dfgshsgdf/fhfgd/", ...]
    dup3 = tmpURLs
    output = mergeDeep2AND3(merge, dup3)
    print("1.2 Done. Got " + str(len(output)) + " URLs. In theory, 17 576 values are possible. For middle readme, got " + str(len(readmeURLs)) + ". In theory, 702 endpoints.")
   
    print("2.1 GET REQUEST To Every README Endpoint")
    filterUniqueness = returnContent(output)
    print("2.2 GEGET REQUEST To Every README (Middle Endpoint)")
    filterUniquenessMiddleReadMe = returnContent(readmeURLs)
    
    print("3. Printing Uniq README ")
    for x in filterUniqueness:
        print(x)
    for x in filterUniquenessMiddleReadMe:
        print(x)
    print("Errors GET : " + str(errorGet))
    
init()

# print(str(len(output)))
# print(str(len(readmeURLs)))
# print(readmeURLs)
# print(str(len(readmeURLs)))

# output = set(output)
# print("After UNIQ : " + str(len(output)))
# output = set(readmeURLs)
# print("After UNIQ : " + str(len(output)))
