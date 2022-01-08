import pandas as pd
import csv
from random import randint
import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "moistdata/moist.csv"
abs_file_path = os.path.join(script_dir, rel_path)
df = pd.read_csv(abs_file_path)

protomoist=df[df.columns[0]]
protohole=df[df.columns[1]]
protopole=df[df.columns[2]]
prototouch=df[df.columns[3]]

moist=[x for x in protomoist if str(x)!="nan"]
hole=[x for x in protohole if str(x)!="nan"]
pole=[x for x in protopole if str(x)!="nan"]
touch=[x for x in prototouch if str(x)!="nan"]

def generatemoist():
    randommoistnumber=randint(0,(len(moist)-1))
    return(str(moist[randommoistnumber]))

def generatehole():
    randomholenumber=randint(0,(len(hole)-1))
    return(str(hole[randomholenumber]))

def generatepole():
    randompolenumber=randint(0,(len(pole)-1))
    return(str(pole[randompolenumber]))

def generatetouch():
    randompolenumber=randint(0,(len(touch)-1))
    return(str(touch[randompolenumber]))

import discord
import os
with open(os.path.join(script_dir, 'token.txt')) as f:
    TOKEN = f.readline()
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    words=["moist","hole","pole","touch","sorcerer"]
    response_message = message.content
    booly=False
    for word in words:
        if word in message.content.lower():
            booly=True
        better_words=[]
    if booly:
        stringmessage=message.content.lower()
        current=stringmessage
        current=current.replace("hole",generatehole())
        current=current.replace("pole",generatepole())
        current=current.replace("moist",generatemoist())
        current=current.replace("touch",generatetouch())
        current=current.replace("sorcerer","shitty wizard")
        response_message=current
        await message.channel.send(response_message)  # send this one after the replacement loop

        await client.process_commands(message)

client.run(TOKEN)