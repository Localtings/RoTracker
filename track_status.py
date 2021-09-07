from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime
import sys
import validators
import time

url = "https://www.roblox.com/users/"+ sys.argv[1] +"/profile"
check = validators.url(url)
if check == False:
    print("[URL] Invalid user ID.")
else:   
    client = uReq(url)
    page = client.read()
    client.close()
    page_soup = soup(page, "html.parser")
    html_tags = page_soup.find("div",{"class":"profile-display-name font-caption-body text text-overflow"})
    print("██████╗░░█████╗░████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░")
    print("██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
    print("██████╔╝██║░░██║░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝")
    print("██╔══██╗██║░░██║░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
    print("██║░░██║╚█████╔╝░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║")
    print("╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
    print("Roblox: @localtbowm")
    print("[TRACKING]"+" "+"Intiailizing...")
    print("[TRACKING]"+" "+"Tracking...")
    status2 = ""
    while True:
        client = uReq(url)
        page = client.read()
        client.close()
        page_soup_main = soup(page, "lxml")
        status = ""
        if page_soup_main.find('span', {"class":'avatar-status online profile-avatar-status icon-online'}):
            status = "online"
        elif page_soup_main.find('span', {"class":'avatar-status game icon-game profile-avatar-status'}):
            status = "pg"
        elif page_soup_main.find('span', {"class":'avatar-status studio profile-avatar-status icon-studio'}):
            status = "mg"
        else:
            status = "offline"
        now = datetime.now()
        current_time = now.strftime("[%H:%M:%S] - ")
        if status != status2:
            if status == "online":
                print(current_time+"Online.")
            elif status == "pg":
                print(current_time+"Playing a game.")
            elif status == "mg":
                print(current_time+"Making a game.")
            elif status == "offline":
                print(current_time+"Offline.")
        status2 = status


        
        



