import csv
import time
from tqdm import tqdm
import shutil
from instabot import Bot
import os
from PIL import Image  
import requests
f = open("followerList.csv","r+")
writeobj = csv.writer(f)
readobj = csv.reader(f)
while True:
    r = requests.get("https://icanhazdadjoke.com/slack")
    r =r.json()
    dadJoke =r["attachments"][0]["text"]
    print(dadJoke)
    if(input("Y/N")=="Y"):
        break
print(dadJoke)
def clear():
    if(os.path.exists("config")):
        shutil.rmtree("config")
    else:
        print("config already deleted")

username="" #enter your username
password ="" # enter your password
clear()
bot = Bot()
bot.login(username=username, password=password)

bot.send_messages(dadJoke,list(readobj)[0])
