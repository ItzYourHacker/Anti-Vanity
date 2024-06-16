import os as hacker
hacker.system("pip install git+https://github.com/dolfies/discord.py-self")
import discord
from discord.ext import commands
client = commands.Bot(command_prefix='', self_bot=True)
token = ""
guild_id = ["1149228142314139648"]
@client.event
async def on_guild_update(before, after):
    async for entry in after.audit_logs(
                limit=1):
      if entry.user.id == after.owner_id or entry.user.id == client.user.id or after.id not in guild_id:return 
      if before.vanity_url_code!= after.vanity_url_code: 
       try:await after.edit(vanity_code=before.vanity_url_code)        
       except Exception as e:print(e)
      else:return
        
@client.event
async def on_ready():
    print("Loaded & Online!")
    print(f"Logged in as: {client.user}")
    print(f"Connected to: {len(client.guilds)} guilds")
    print(f"Connected to: {len(client.users)} users")
client.run(token)
