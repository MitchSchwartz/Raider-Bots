import requests
from discord.ext import commands
from discord_slash import SlashCommand
import json
import os
from get_server_id import getServerId




def runNewBot():
  
  print("Starting NewBot")

  newBot = commands.Bot(command_prefix='-')
  slash = SlashCommand(newBot, sync_commands=True)


  @slash.slash(name="buy_raider", description="How can I buy $Raider tokens?")
  async def buy_raider(ctx):
    await ctx.send("To buy $RAIDER tokens from SushiSwap, click here:\nhttps://app.sushi.com/swap?inputCurrency=ETH&outputCurrency=0xcd7361ac3307D1C5a46b63086a90742Ff44c63B3")

  @slash.slash(name="buy_aurum", description="How can I buy $Aurum tokens?")
  async def buy_aurum(ctx):
    await ctx.send("To buy $AURUM tokens from SushiSwap, click here:\n https://app.sushi.com/swap?inputCurrency=ETH&outputCurrency=0x34d4ab47Bee066F361fA52d792e69AC7bD05ee23")

  @slash.slash(name="stake_raider", description="A quick intro to staking raider")
  async def stake_raider(ctx):
    await ctx.send("**PLEASE REMEMBER THAT THIS IS A FUNCTIONAL GUIDE, IT IS  DEFINITELY NOT FINANCIAL ADVICE.** \n\nYou can earn $AURUM by solo staking $RAIDER tokens. \n\nStaking for: \n - 3 months will earn the base APR \n - 6 months will earn 2x \n - 9 months will earn 3x, and \n - 12 months will earn 4x \n\n Stakers have also received several air drops.\n\n By staking, **your tokens will be locked up, and you won't be able to retrieve them for the full staking duration.** \n\nOnce you've chosen a staking period, you won't be able to increase or decrease it, but you will be able to add more tokens.\n\nWhen your staking period is over, you will be able to retrieve your tokens at any time; you'll also be able to leave them and continue to earn aurum at the same rate \n\n You can claim your $AURUM rewards at any time. \n\nYou can stake $RAIDER here: https://econ.cryptoraiders.xyz/staking.")

  @slash.slash(name="how_do_i_start_playing", description="How do I start playing Crypto Raiders?")
  async def how_do_i_start_playing(ctx):
    await ctx.send("Crypto Raiders can be played on mobile and desktop here: https://play.cryptoraiders.xyz. \n\nTo get started, you'll need to acquire a Raider, which you can do from https://opensea.io/collection/crypto-raiders-characters. \n\nRaiders live on Polygon, so you can pay in WETH and skip the ETH gas fees.\n\nIf you only have ETH, you can bridge it to the Polygon network using their bridge: https://wallet.polygon.technology/bridge. \nMany of our members prefer the much cheaper Umbria bridge found here: https://bridge.umbria.network/bridge. \n\nTo do all of this, you'll need to use MetaMask wallet which can be installed here: https://metamask.io/download.")
    
  #await slash.register_global_slash_command(sc)
      # Discord API uploads GLOBAL commands for more than 1 hour
      # That's why I highly recommend .register_guild_slash_command for testing:
  # server = getServerId("test")
  # await slash.register_guild_slash_command(test_guild_id, sc)

  newBotToken = os.environ.get("newBot")
  newBot.run(newBotToken)



def registerGuildSlashCommand(_name, _description, _type):
  server = getServerId("test")
  appId = 935550057409814578

  url = f"https://discord.com/api/v8/applications/{appId}/guilds/{server}/commands"
  print(url)

  # This is an example CHAT_INPUT or Slash Command, with a type of 1
  json =  {
      "name" : f"{_name}", 
      "description" : f"{_description}",
      "type": f"{_type}"
    }


  newBotToken = os.environ.get("newBot")

  # For authorization, you can use either your bot token
  headers = {
      "Authorization": f"Bot {newBotToken}"
  }

  try:
    r = requests.post(url, headers=headers, json=json)
    print((r.json()))
  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n {e.content} \n")



def getCommands(_server):

  guild = ""
  

  if _server:
    server = getServerId("test")
    guild = f"/guilds/{server}"
    

  appId = 935550057409814578 


  url = f"https://discord.com/api/v8/applications/{appId}{guild}/commands"
  print(url)
  newBotToken = os.environ.get("newBot")

  # For authorization, you can use either your bot token
  headers = {
      "Authorization": f"Bot {newBotToken}",
      "Content-Type": "application/json"
  }


  try:
    r = requests.get(url, headers=headers)
    print(json.dumps(r.json(), indent=4))
  except requests.exceptions.RequestException as e:
    print(f"\n {e} \n {e.content} \n")

