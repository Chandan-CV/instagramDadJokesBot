import csv
import json
# from instabot import Bot
# from dadJokeBot import clear

f = open("followerList.csv","r+")
writeobj = csv.writer(f)
readobj = csv.reader(f)
# clear()

# bot = Bot()
# bot.login(username="awhh_look_who_it_isnt", password="Development16")
# a = bot.followers
# writeobj.writerow(a)
print(list(readobj)[0])

