import graphlib
from instapy import InstaPy

myUsername = "awhh_look_who_it_isnt"
myPass = "Development16"
session =InstaPy(username = myUsername, password = myPass)

followers= session.grab_followers(username= myUsername, amount=50)
print(followers)