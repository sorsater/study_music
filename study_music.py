import random
import os
import json
import time
from pprint import pprint
import signal

# google_chrome folder
folder = "study_music"

# path to bookmarks file
user = "michael"
path = '/home/' + user + '/.config/google-chrome/Default/Bookmarks'

# point to icon in the git folder
icon = "/home/michael/Documents/gitworks/study_music/icon.png"

def notify(title, message, icon):
    os.system('notify-send -i ' + icon + ' "' + title + '" "' + message + '"')

with open(path, 'r') as bm:
    data = json.load(bm)

# print formatted json
#pprint(data)

# adds all the links to res
res = []
for i in data["roots"]["bookmark_bar"]["children"]:
    if(i["name"] == folder):
        for c in i["children"]:
            res.append([c["name"],c["url"]])

idx = random.randrange(len(res))

title = "Opening link"
message = res[idx][0]

notify(title, message, icon)

os.system('google-chrome ' + res[idx][1])
time.sleep(2)
os.kill(os.getppid(), signal.SIGHUP)
