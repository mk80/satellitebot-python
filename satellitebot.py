
import os
import sys
import discord
import re
from skyfieldModule import getSatelliteVisable

# get present working dir
pwd = os.getcwd()

# define file that has the token and store in token var
token_file = 'token.txt'
token = ''

with open(token_file,'r') as data:
  token = data.read().replace('\n','')

# define log file to use
log_file = pwd + '/' + 'message.log'

# start discord client
client = discord.Client()

# regex definitions
bot_name = (r'.*satellitebot.*')

# satellite info
sat_file =  pwd + '/' + 'ISS.info'

# extra header info
extra_header_file = pwd + '/' + 'extra.header'

#** max message is 2000 chars; 16 x 125 is the largest message; 16 lines

@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
  # logging for later use
  with open(log_file,'a') as log:
    log.write(f'We have logged in as {client.user}\n')  # notification of login

@client.event
async def on_message(message):  # event that happens per any message.
  # test dm
  with open(sat_file, 'r') as f:
    data = f.read()

  with open(extra_header_file, 'r') as h:
    extra_info = h.read()

  # test visibility printout with ISS
  satName = 'ISS'
  satPrintout = getSatelliteVisable(satName)

  if (message.content.startswith("!test")):
    # sending as code snippet for proper formatting of text
    await message.author.send('```' + data + '```')
    await message.author.send('```' + str(satPrintout) + '```')
    await message.author.send('```' + extra_info + '```')

  found_match = re.match(bot_name,message.content.lower())
  #if found_match and str(message.author) != "satellitebot#8915":

client.run(token)
