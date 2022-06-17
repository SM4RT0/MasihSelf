import re, os, importlib
from pyrogram import Client
from pyrogram.client import Client
from pyrogram.types.messages_and_media.message import Message
from pyrogram import filters

client = Client('user', config_file='config.ini')

VERSION = 2.0






@client.on_message(filters.regex('^version$', re.I) & filters.me)
async def version(client: Client, message: Message):
    await message.edit("Version {}".format(VERSION))

@client.on_message(filters.regex('^help$', re.I) & filters.me)
async def help(client: Client, message: Message):
    help = """
    version: Return current version
    help: Return this help message
    
    Source: (MasihSelf)[https://github.com/Masihgh/MasihSelf]
    """
    i = 0
    
    for file in os.listdir('plugins'):
        
        if file[-3:] != '.py': continue
        i = i+1
        help += f"\n **[{i}]** {file.replace('.py','')}" + importlib.import_module('plugins.' + file[:-3]).help + "\n"
    i = 0
    await message.edit("HELP : \n{}\n version:{}".format(help, VERSION))

client.run()
