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
protoball = df[df.columns[4]]
protomeat = df[df.columns[5]]
prototest = df[df.columns[6]]
moist=[x for x in protomoist if str(x)!="nan"]
hole=[x for x in protohole if str(x)!="nan"]
pole=[x for x in protopole if str(x)!="nan"]
touch=[x for x in prototouch if str(x)!="nan"]
ball=[x for x in protoball if str(x)!="nan"]
meat=[x for x in protomeat if str(x)!="nan"]
test=["test1","test2","test3"]
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

def generateball():
    randompolenumber=randint(0,(len(ball)-1))
    return(str(ball[randompolenumber]))

def generatemeat():
    randompolenumber=randint(0,(len(meat)-1))
    return(str(meat[randompolenumber]))

def generatetest():
    randompolenumber=randint(0,(len(test)-1))
    return(str(test[randompolenumber]))
import discord
import os
with open(os.path.join(script_dir, 'token.txt')) as f:
    TOKEN = f.readline()
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id == ('Paris#8008'):
        return
    words=["moist","hole","pole","touch","sorcerer","ball","meat"]
    response_message = message.content
    test_response=message.content.lower()
    booly=False
    for word in words:
        if word in message.content.lower():
            booly=True
        better_words=[]
    if "bottest" in message.content.lower():
        final=[]
        wordlist=test_response.split(" ")
        for word in wordlist:
            newword=word.replace("bottest",generatetest())
            final.append(newword)
        my_response=" ".join(final)
        await message.channel.send(my_response)
 #       await message.channel.send(final)
    if booly:
        final=[]
        wordlist=test_response.split(" ")
        for current in wordlist:
            current=current.replace("hole",generatehole())
            current=current.replace("pole",generatepole())
            current=current.replace("moist",generatemoist())
            current=current.replace("touch",generatetouch())
            current=current.replace("ball",generateball())
            current=current.replace("meat",generatemeat())
            current=current.replace("sorcerer","shitty wizard")
            final.append(current)
        response_message=" ".join(final)
        await message.channel.send(response_message)  # send this one after the replacement loop
client.run(TOKEN)