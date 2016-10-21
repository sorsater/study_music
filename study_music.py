import random
import os
import json
import time
from pprint import pprint
import signal

# -1 if no closing down
sleeptime = 8
folder = "study_music"
user = "michael"
path = '/home/' + user + '/.config/google-chrome/Default/Bookmarks'

# the links in the folder
res = []

with open(path, 'r') as bm:
    data = json.load(bm)

# print formatted json
#pprint(data)

for i in data["roots"]["bookmark_bar"]["children"]:
    if(i["name"] == folder):
        for c in i["children"]:
            res.append([c["name"],c["url"]])

print(len(res), " links in folder.")

vald = random.randrange(len(res))
print("Opening: ", res[vald][0])
os.system('google-chrome ' + res[vald][1])

if(sleeptime != -1):
    for i in range(sleeptime):
        print("Closing down:", sleeptime-i, "", end="\r")
        time.sleep(1)

    os.kill(os.getppid(), signal.SIGHUP)
