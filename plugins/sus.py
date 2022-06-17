from base64 import b64decode
import re
from pyrogram.client import Client
from pyrogram.types import MessageEntity
from pyrogram.types.messages_and_media.message import Message
from pyrogram import filters
help = """
Super Ultra Sexy Tools

/ss resone
Reply Any User
Save On Save Message
"""


@Client.on_message(filters.command('ss') & filters.me)
async def save(client: Client, message: Message):
    resone = message.text[4:]
    
    await message.delete()
    from_id = message.reply_to_message['from_user']['id']
    from_name = message.reply_to_message['from_user']['first_name']
    
    await client.send_message('me', f"👤 [{from_name}](tg://user?id={from_id}) \n ⁉️ {resone}")


