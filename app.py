# Kenna 21.07.2018
# Github: https://github.com/kennethrisa/discord-rustserverstatus-python
import discord
import asyncio
import requests
import configparser

# Config:
config = configparser.ConfigParser()
config.read('config.ini')

BOT = config['BOT']
token = BOT['token']
apiSite = BOT['apiSite']
apiUrl = BOT['apiUrl']

# updateInSec
updateInterval = 360

client = discord.Client()

# Print the starting text
print('---------------')
print('Discord Bot updates activity status every 6 min')
print('---------------')
print('Starting Bot...')

try:
    async def updateStatusPresence():
        await client.wait_until_ready()
        counter = 0
        while not client.is_closed:
            counter += 1
            print('ready')
            if apiSite == '1':
                print('Api site 1')
                print('updated')
                url = apiUrl
                resp = requests.get(url=url)
                try:
                    if resp.status_code != 200:
                            raise print("Expected status code 200, but got {}")
                    else:    
                        data = resp.json()
                        name = data['name']
                        players = data['players']
                        maxPlayers = data['players_max']
                        game = discord.Game(type=0, name=players + " / " + maxPlayers)
                        await client.change_presence(game=game)
                except Exception as e:
                    print(e)
            if apiSite == '2':
                print('Api site 2')
                print('updated')
                url = apiUrl
                resp = requests.get(url=url)
                try:
                    if resp.status_code != 200:
                            raise print("Expected status code 200, but got {}")
                    else:    
                        data = resp.json()
                        name = data['name']
                        players = data['players']
                        maxPlayers = data['maxplayers']
                        game = discord.Game(type=0, name=players + " / " + maxPlayers)
                        await client.change_presence(game=game)
                except Exception as e:
                    print(e)
            await asyncio.sleep(updateInterval)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print('------')

        client.loop.create_task(updateStatusPresence())

except Exception as e:
    print(e)
try:
    client.run(token)
    
except Exception as e:
    print(e)