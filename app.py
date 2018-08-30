# Kenna 21.07.2018
# Github: https://github.com/kennethrisa/discord-rustserverstatus-python
# Version 0.0.2
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
            if apiSite == '1':
                url = apiUrl
                resp = requests.get(url=url)
                if resp.status_code != 200:
                        raise print("Expected status code 200, but got {}")
                else:    
                    data = resp.json()
                    players = data['players']
                    maxPlayers = data['players_max']
                    game = discord.Game(type=0, name=players + " / " + maxPlayers)
                    await client.change_presence(game=game)
            if apiSite == '2':
                url = apiUrl
                resp = requests.get(url=url)
                if resp.status_code != 200:
                        raise print("Expected status code 200, but got {}")
                else:    
                    data = resp.json()
                    players = data['players']
                    maxPlayers = data['maxplayers']
                    game = discord.Game(type=0, name=players + " / " + maxPlayers)
                    await client.change_presence(game=game)
            await asyncio.sleep(updateInterval)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print('------')

        # Create task to update status
        client.loop.create_task(updateStatusPresence())
        
except Exception as e:
    print(e)

# Start bot
client.run(token)