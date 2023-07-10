import requests
import urllib
import json
import time
import os

print("         (   (      (                   )    ") 
print("         )\ ))\ )   )\ )  (    (     ( /(    ") 
print("      ( (()/(()/(  (()/(  )\   )\    )\())   ") 
print("      )\ /(_))(_))  /(_)|((_|(((_)( ((_)\    ") 
print("   _ ((_|_))(_))   (_)) )\___)\ _ )\ _((_)   ") 
print("  | | | | _ \ |    / __((/ __(_)_\(_) \| |   ") 
print("  | |_| |   / |__  \__ \| (__ / _ \ | .` |   ") 
print("   \___/|_|_\____| |___/ \___/_/ \_\|_|\_|   ")  
print("                                             ")
print("            beta 1.0  by Chrxstxqn           ")                                           
print("                                             ")

os.system("toilet T-MUS")
url = input("Insert URL to scan: ")
encoded_url = urllib.parse.quote(url, safe='')
api_url = "https://ipqualityscore.com/api/json/url/6iP3Ci09b83suqDijoQ4pHSD9uayadBp/"
data = requests.get(api_url + encoded_url)
print(json.dumps(data.json(), indent=4))
print("")
print("")
print("Tanks for using! <3")
print("Support me on Instagram : '_chrxstxqn_' " )

