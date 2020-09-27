from flask import Flask, render_template
import json
import urllib
from urllib.request import urlopen

host = "0.0.0.0" #do not change this!
channelid = 
key = 
subs = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channelid}&fields=items/statistics/subscriberCount&key={key}'
output = json.load(urlopen(subs))

def updatecount():
    with open("data.json", "w") as f:
        json.dump(output, f, indent=4)

updatecount() # updates every 1 sec (reload page to see)

app = Flask(__name__)
port = 7642

@app.route('/')
def home():
    with open('data.json') as f:
        subs = json.load(f)
    subscribers = subs["items"][0]["statistics"]["subscriberCount"] #this shows the numbers of the subs!

    return f'<center><h1 style="position: fixed; top: 40%; left: 50%; transform: translate(-50%, -50%); font-family: Arial, Helvetica, sans-serif;">ThonkySl Sub Count:<br><br>{subscribers}</h1></center>'

if __name__ == '__main__':
    app.run(port=port host=host)
