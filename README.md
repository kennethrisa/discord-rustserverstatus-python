# Python Rust discord bot that displayes online players

![Discord-bot](https://i.gyazo.com/23a3f95b758a146efa7d4a3dfd5f3999.png)

Updates activity status on discord bot and displays how many players are connect to your rust server from rest api

Written in Python and requires version 3.4 or 3.6 else you will get errors.

* Support rust-servers.info
* Support rust-servers.net
* Bot update status every 6 minutes

# Configuration
config.ini
```
[BOT]
# Bot token and not client secret.
token = <your token here>

# 1 = rust-servers.info
# 2 = rust-servers.net
apiSite = 2

# example:
# rust-servers.info: https://api.rust-servers.info/status/106
# rust-servers.net:  https://rust-servers.net/api/?object=servers&element=detail&key={ServerKey}
apiUrl = https://rust-servers.net/api/?object=servers&element=detail&key=
```
* token = Your bot token from discord.
* apiSite: To use rust-servers.info, set apiSite = 1, rust-servers.net, set apiSite = 2 in config.
* apiUrl: Use full url, for rust-servers.info: example: https://api.rust-servers.info/status/<your id> and rust-servers.net: https://rust-servers.net/api/?object=servers&element=detail&key={ServerKey}
* Client secret is used to invite the bot to your server. Token is used for the bot to connect to discord.

# Installation:
```
Download it as zip or use:
git clone https://github.com/kennethrisa/discord-rustserverstatus-python.git
run command to install dependencies:
pip install discord.py asyncio requests configparser
```

edit config.ini file with correct parameters

Before you start the bot, I assumes that you know have to created a discord bot and invited it to your server.

Start the bot:

```
python app.py or python3 app.py
```