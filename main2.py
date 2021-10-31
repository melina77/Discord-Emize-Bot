import discord
import os
import sys
import requests
import json
import random
import datetime
import time
from replit import db
from keep_alive import keep_alive
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix= '.')

client = discord.Client()

bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$give coins'):
        await message.channel.send('Click this link to get coins: https://streamable.com/e/shil2')



def dadjokes():
  response = requests.get
  ("https://icanhazdadjoke.com")
  jokee = GET ("https://icanhazdadjoke.com/")
  return(jokee)


dadjoke = ["I'm afraid for the calendar. Its days are numbered.",
"My wife said I should do lunges to stay in shape. That would be a big step forward.",
"Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!",
"Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
"What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.",
"What do you call a fish wearing a bowtie?" "Sofishticated.",
"How do you follow Will Smith in the snow?" "You follow the fresh prints.",
"If April showers bring May flowers, what do May flowers bring?" "Pilgrims.",
"I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along.","What do you call a factory that makes okay products?" "A satisfactory.",
"Dear Math, grow up and solve your own problems.",
"What did the janitor say when he jumped out of the closet?" "Supplies!",
"Have you heard about the chocolate record player? It sounds pretty sweet.",
"What did the ocean say to the beach?" "Nothing, it just waved.",
"Why do seagulls fly over the ocean?" "Because if they flew over the bay, we'd call them bagels.",
"I only know 25 letters of the alphabet. I don't know y.",
"How does the moon cut his hair?" "Eclipse it.",
"What did one wall say to the other?" "I'll meet you at the corner.",
"What did the zero say to the eight?" "That belt looks good on you.",
"A skeleton walks into a bar and says, 'Hey, bartender. I'll have one beer and a mop.'",
"Where do fruits go on vacation?" "Pear-is!",
"I asked my dog what's two minus two. He said nothing.",
"What did Baby Corn say to Mama Corn?" "Where's Pop Corn?",
"What's the best thing about Switzerland?" "I don't know, but the flag is a big plus.",
"What does a sprinter eat before a race?" "Nothing, they fast!",
"Where do you learn to make a banana split?" "Sundae school.",
"What has more letters than the alphabet?" "The post office!",
"Dad, did you get a haircut?" "No, I got them all cut!",
"What do you call a poor Santa Claus?" "St. Nickel-less.",
"I got carded at a liquor store, and my Blockbuster card accidentally fell out. The cashier said never mind.",
"Where do boats go when they're sick?" "To the boat doc.",
"I don't trust those trees. They seem kind of shady.",
"My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!",
"How do you get a squirrel to like you? Act like a nut.",
"Why don't eggs tell jokes? They'd crack each other up.",
"I don't trust stairs. They're always up to something.",
"What do you call someone with no body and no nose? Nobody knows.",
"Did you hear the rumor about butter? Well, I'm not going to spread it!",
"Why couldn't the bicycle stand up by itself? It was two tired.",
"What did one hat say to the other?" "Stay here! I'm going on ahead.",
"Why did Billy get fired from the banana factory? He kept throwing away the bent ones."]
 

emizebot = ["@emizebot","emizebot","Emizebot","EMIZEBOT","emize bot"]

rickroll = ["give you up","let you down","never gonna give","Never gonna give you up"]


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.author.bot:
    return

  msg = message.content

  if msg.startswith('$greet'):
    await message.channel.send('Say hello!')

    def check(m):
        return m.content == 'hello' and m.channel == message.channel

    msg = await client.wait_for('message', check=check)
    await message.channel.send('Hello {.author}!'.format(msg))


  if msg.startswith('$hack nasa'):
    await message.channel.send("Start attacking...")
    time.sleep(5)
    await message.channel.send("- -Hacking NASA- -")
    time.sleep(5)
    await message.channel.send("Penetrating into the system")
    time.sleep(5)
    await message.channel.send("Hacking NASA 20%")
    time.sleep(5)
    await message.channel.send("Hacking NASA 40%")
    time.sleep(5)
    await message.channel.send("Hacking NASA 60%")
    time.sleep(5)
    await message.channel.send("Hacking NASA 80%")
    time.sleep(5)
    await message.channel.send("Hacking NASA 100%")
    time.sleep(7)
    await message.channel.send("Hacked NASA Successfully")

  if msg.startswith('$trust'):
    await message.channel.send("Click this link if you trust emizebot: https://matias.ma/nsfw/")


  if msg.startswith('$newquote'):

      DATA_DIR = 'data'
      
      class User: 
          def _user_(self, username, quote, date):
              self.username = message.author
              self.quote = message.content - '$newquote'
              self.date = datetime.date.today()
            
          def save_to_file_(self):
              with open(f"{DATA_DIR}/{self.username}.txt", 'w') as file:
                  txt = open('quotes.txt','w+')
                  txt.writelines([(message.author.mention)+'\n'+(message.content)+'\n'+(datetime.date.today())])
                  
                  file.write(f'{self.username}\n')
                  file.write(f'{self.quote}\n')
                  file.write(f'{self.date}\n')

          def save():
              txt='quotes.txt'
              mention=message.author.mention
              messagee=message.content

              with open(f"{txt}", 'w') as file:
                  file.write(f'{mention}\n')
                  file.write(f'{messagee}\n')
              
                  
          save_to_file_
          save


      await message.channel.send('quote: <' + (message.content[9:10000:]) + '>  \n author:  <' + (message.author.mention) + '>'.format(msg))



  if any(word in msg for word in rickroll):
    await message.channel.send('https://media.discordapp.net/attachments/791216539201830932/885757907147321374/Screenshot_20210910_105444.jpg?width=263&height=563')



  if msg.startswith('$dadjoke'):
    await message.channel.send(random.choice(dadjoke))

  if msg.startswith('$dadjokes'):
    await message.channel.send(jokee)


  if any(word in msg for word in emizebot):
      await message.channel.send('Who has called upon emizebot? Use $help to ask me something.')

  if msg.startswith('$help'):
    await message.channel.send("You can use these commands:\n $hello - to say hi to emizebot,\n  $help - to see this message,\n  $give coins - to get dank memer coins,\n  $dadjoke - to hear a hardcoded dad joke,\n $dadjokes - to hear a dad joke rendered from a web service,\n $newquote - to create a new quote,\n $hack nasa - to hack nasa,\n $save <quote> - to save a quote in emizebot's system,\n $showquotes to view all saved quotes,\n $showquote <number> - to view a specific saved quote,\n $emizebot said <quote> - to make emizebot say a quote you made,\n $trust - to verify that you trust emizebot")


  if msg.startswith("$dadjoke"):
    joke = get_dadjoke()
    await message.channel.send(joke)

  if msg.startswith("$hello"):
    await message.channel.send('Hello! Use $help to see what you can do with emizebot!')



  if msg.startswith("$give coins"):
     await message.channel.send('Click this link to get coins: https://www.youtube.com/embed/dQw4w9WgXcQ')



  if msg.startswith('$save '):
    await message.channel.send(msg[6:])
    tx=open('quotes.txt','a')
    tx.write('*"'+msg[6:]+'"*   ~ By: {'+str(message.author.name)+'} \n')

  elif msg.startswith('$emizebot said '):
    await message.channel.send(msg[15:])

  elif msg.startswith('$showquotes'):
    tx=open('quotes.txt','r')
    ji=tx.readlines()
    tmp=''
    for i in range(len(ji)):
      tmp+=str(i+1)+'. '+ji[i]
    await message.channel.send(tmp)

  if msg.startswith('$showquote '):
      sno=int(msg.split()[1])
      if  sno < 10000 and sno>0:
        tx=open('quotes.txt','r')
        ji=tx.readlines()
        if len(ji)>=sno:
            await message.channel.send(ji[sno-1])
        else:
          await message.channel.send('There arent that many quotes')
      else:
        await message.channel.send('number should be above 0 and below 10000')

   
load_dotenv()

TOKEN = os.getenv('TOKEN')

keep_alive()