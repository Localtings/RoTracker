from urllib.request import urlopen
import json
import sys
print("██████╗░░█████╗░████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░")
print("██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
print("██████╔╝██║░░██║░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝")
print("██╔══██╗██║░░██║░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
print("██║░░██║╚█████╔╝░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║")
print("╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
print("Roblox: @localtbowm")
print("[TRACKING]"+" "+"Intiailizing...")
print("[TRACKING]"+" "+"Loading...")
url = "https://api.roblox.com/users/"+ sys.argv[1] +"/onlinestatus/"
response = urlopen(url)
data_json = json.loads(response.read())
print("Online Status:" + data_json["IsOnline"])
print("Last Location:" + data_json["LastLocation"])
print("Last Online Time:" + data_json["LastOnline"])
