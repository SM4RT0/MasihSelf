from base64 import b64decode
import re
from pyrogram.client import Client
from pyrogram.types import MessageEntity
from pyrogram.types.messages_and_media.message import Message
from pyrogram import filters
import asyncio

help = """
Animation Text Edit
[1] love
[2] love2
[3] love3
[4] dick
[5] dickf (faster)
[6] dance
[7] yalda
[8] bomb
[9] pros
[10] post
[11] hack
[12] gun
[13] shash
[14] shashr (shashidam too in refaghat)
[15] jaq1 (đ)
[16] jaq2 (đĽş)
[17] lovehack (vip command)
"""



@Client.on_message(filters.regex('^bomb$', re.I) & filters.me)
async def bomb(client: Client, message: Message):
    bomb_animation = [
	"**[10]**",
	"**[9]**",
	"**[8]**",
	"**[7]**",
	"**[6]**",
	"**[5]**",
	"**[4]**",
	"**[3]**",
	"**[2]**",
	"**[1]**",
	"**đ§¨Ř¨ŮŘ¨ Ř§ŮŘ§Ů ŮŮŮŘŹŘąŮ ŮŰŘ´Ů**",
	"ŮžŮŮ",
	"ŮžŮŮŮŮŮ",
	"ŮžŮŮŮŮŮŘŽ",
	"ŮžŮŮŮŮŮŘŽŰ đ",
	"đ",



	]

    run_animation = 1

    for i in range(run_animation):
         for asset in bomb_animation:
                await asyncio.sleep(0.8)
                await message.edit(asset)


@Client.on_message(filters.regex('^love$', re.I) & filters.me)
async def love(client: Client, message: Message):
    love_animation = ["đ¤đ¤đ¤đ¤đ¤",
    "â¤ď¸đ¤đ¤đ¤đ¤",
    "đ¤â¤ď¸đ¤đ¤đ¤",
    "đ¤đ¤â¤ď¸đ¤đ¤",
    "đ¤đ¤đ¤â¤ď¸đ¤",
    "đ¤đ¤đ¤đ¤â¤ď¸",
     "đ¤đ¤đ¤â¤ď¸đ¤",
    "đ¤đ¤â¤ď¸đ¤đ¤",
    "đ¤â¤ď¸đ¤đ¤đ¤",
    "â¤ď¸đ¤đ¤đ¤đ¤"]

    run_animation = 4

    for i in range(run_animation):
         for asset in love_animation:
                #await asyncio.sleep(5)
                await message.edit(asset)

@Client.on_message(filters.regex('^dick$', re.I) & filters.me)
async def dick(client: Client, message: Message):
    dick_animation = ['B==D',
    'B===D',
    'B====D',
    'B=====D',
    'B====D',
    'B===D',
    'B==D',
    'B=D']

    run_animation = 16

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.6)
                await message.edit(asset)
    await message.edit('**The End!**')


@Client.on_message(filters.regex('^dickf$', re.I) & filters.me)
async def dickf(client: Client, message: Message):
    dick_animation = ['B==D',
    'B===D',
    'B====D',
    'B=====D',
    'B====D',
    'B===D',
    'B==D',
    'B=D']

    run_animation = 20

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.1)
                await message.edit(asset)
    await message.edit('**The End!**')




@Client.on_message(filters.regex('^pros$', re.I) & filters.me)
async def pros(client: Client, message: Message):
    pros_animation = ["â˘ż", "âŁť", "âŁ˝", "âŁž", "âŁˇ", "âŁŻ", "âŁ", "âĄż"]
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.1)
                await message.edit(asset)
    await message.edit('**The End!**')

@Client.on_message(filters.regex('^love2$', re.I) & filters.me)
async def love2(client: Client, message: Message):
    pros_animation = ['â¤ď¸','đ','đ','đ','đ¤','đ§Ą','đ¤','đ','đ¤']
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(f'**I Love You{asset} :)**')
    await message.edit('**The End!**')

@Client.on_message(filters.regex('^post$', re.I) & filters.me)
async def post(client: Client, message: Message):
    posts_animation = ['đŞ','đŤ','đŹ','đ­']
    run_animation = 10

    for i in range(run_animation):
         for asset in posts_animation:
                await asyncio.sleep(0.3)
                await message.edit(f'**{asset}Posting . . .**')
    await message.edit('**The End!**')



@Client.on_message(filters.regex('^dance$', re.I) & filters.me)
async def dance(client: Client, message: Message):
    dick_animation = ['âŞâ ( ď˝Ľoď˝Ľ) ââŞ','âŞâ(ăťoď˝Ľ)ââŞ']
    run_animation = 50

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.1)
                await message.edit(asset)
    await message.edit('**đľđľ!**')
    

#yalda 1400
@Client.on_message(filters.regex('^yalda$', re.I) & filters.me)
async def yalda(client: Client, message: Message):
    dick_animation = ['â ( ď˝Ľđď˝Ľ) â','â(ăťđď˝Ľ)â']
    run_animation = 20

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.8)
                await message.edit(asset)
    await message.edit('**đŘ´Ř¨ ŰŮŘŻŘ§ŘŞŮŮ ŮŘ¨Ř§ŘąÚŠ!đ**')




@Client.on_message(filters.regex('^love3$', re.I) & filters.me)
async def love3(client: Client, message: Message):
    pros_animation = ['â¤ď¸','đ','đ','đ','đ¤','đ§Ą','đ¤','đ','đ¤']
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.8)
                await message.edit(f'{asset}')


                
@Client.on_message(filters.regex('^hack$', re.I) & filters.me)
async def hack(client: Client, message: Message):
    pros_animation = ["Hacking...\n0 1 0 1 0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1 0 1 0 1",
    "Hacking...\n1 0 1 0 1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0 1 0 1 0"]
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(asset)
    await message.edit('**target HACKED!**')
    
@Client.on_message(filters.regex('^lovehack$', re.I) & filters.me)
async def lovehack(client: Client, message: Message):
    pros_animation = ["Hacking HEART...\n0 1 0 1 0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1 0 1 0 1",
    "Hacking HEART...\nđ â¤ď¸ đ â¤ď¸ đ â¤ď¸ đ\nâ¤ď¸ đ â¤ď¸ đ â¤ď¸ đ â¤ď¸\nđ â¤ď¸ đ â¤ď¸ đ â¤ď¸ đ",
    "Hacking HEART...\n1 0 1 0 1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0 1 0 1 0",
    "Hacking HEART...\nâ¤ď¸ đ â¤ď¸ đ â¤ď¸ đ â¤ď¸\nđ â¤ď¸ đ â¤ď¸ đ â¤ď¸ đ\nâ¤ď¸ đ â¤ď¸ đ â¤ď¸ đ â¤ď¸"]
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(asset)
    await message.edit('**Target heart HACKED! now SHE is with YOU! đŠââ¤ď¸âđ¨đđťâ¤ď¸âđĽđşđť **')
    
@Client.on_message(filters.regex('^shashr$', re.I) & filters.me)
async def shashr(client: Client, message: Message):
    dick_animation = ["Ř´Ř§Ř´ŰŘŻŮ ŘŞŮ Ř§ŰŮ ŘąŮŘ§ŮŘŞ!!!!!\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "Ř´Ř§Ř´ŰŘŻŮ ŘŞŮ Ř§ŰŮ ŘąŮŘ§ŮŘŞ!!!!!\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "Ř´Ř§Ř´ŰŘŻŮ ŘŞŮ Ř§ŰŮ ŘąŮŘ§ŮŘŞ!!!!!\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "Ř´Ř§Ř´ŰŘŻŮ ŘŞŮ Ř§ŰŮ ŘąŮŘ§ŮŘŞ!!!!!\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "Ř´Ř§Ř´ŰŘŻŮ ŘŞŮ Ř§ŰŮ ŘąŮŘ§ŮŘŞ!!!!!\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "Ř´Ř§Ř´ŰŘŻŮ ŘŞŮ Ř§ŰŮ ŘąŮŘ§ŮŘŞ!!!!!\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "Ř´Ř§Ř´ŰŘŻŮ ŘŞŮ Ř§ŰŮ ŘąŮŘ§ŮŘŞ!!!!!\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "Ř´Ř§Ř´ŰŘŻŮ ŘŞŮ Ř§ŰŮ ŘąŮŘ§ŮŘŞ!!!!!\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n"]
    run_animation = 3

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.5)
                await message.edit(asset)
    await message.edit('** **')
    
@Client.on_message(filters.regex('^shash$', re.I) & filters.me)
async def shash(client: Client, message: Message):
    dick_animation = ["\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n",
    "\n\nB=======Dâ\n                       â\n                         â\n                           â\n                             â\n                               â\n                                 â\n                                   â\n"]
    run_animation = 3

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.5)
                await message.edit(asset)
    await message.edit('** **')
    

@Client.on_message(filters.regex('^jaq1$', re.I) & filters.me)
async def jaq1(client: Client, message: Message):
    dick_animation = [
    "\nI'm comming\n\n    đ                        \n   / [] \                              \n    (( B====âđťđ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nYesss\n\n    đ                        \n   / [] \                              \n    (( B===âđť=đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nI'm comming\n\n    đ                        \n   / [] \                              \n    (( B==âđť==đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nYESSS\n\n    đ                        \n   / [] \                              \n    (( B=âđť===đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nREADYYYYYY\n\n    đ                        \n   / [] \                              \n    (( B==âđť==đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nHMMMMMM\n\n    đ                        \n   / [] \                              \n    (( B===âđť=đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nOPEN YOUR MOUTHHHH HMMMM\n\n    đ                        \n   / [] \                              \n    (( B====âđťđ        /       /\n    /   \                 đ¨====\n                                  \       \ "
    ]
    
    run_animation = 3

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.2)
                await message.edit(asset)
    await message.edit('**\n YEAH BABE\n    đ                        \n   / [] \                              \n    (( B======đđŚ  /       /\n    /   \                 đśâđŤď¸====\n                                  \       \  **')

@Client.on_message(filters.regex('^jaq2$', re.I) & filters.me)
async def jaq2(client: Client, message: Message):
    dick_animation = [
    "\nI'm comming\n\n    đĽş                        \n   / [] \                              \n    (( B====âđťđ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nYesss\n\n    đĽş                        \n   / [] \                              \n    (( B===âđť=đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nI'm comming\n\n    đĽş                        \n   / [] \                              \n    (( B==âđť==đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nYESSS\n\n    đĽş                        \n   / [] \                              \n    (( B=âđť===đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nREADYYYYYY\n\n    đĽş                        \n   / [] \                              \n    (( B==âđť==đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nHMMMMMM\n\n    đĽş                        \n   / [] \                              \n    (( B===âđť=đ        /       /\n    /   \                 đ¨====\n                                  \       \ ",
    "\nOPEN YOUR MOUTHHHH HMMMM\n\n    đĽş                        \n   / [] \                              \n    (( B====âđťđ        /       /\n    /   \                 đ¨====\n                                  \       \ "
    ]
    
    run_animation = 3

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.2)
                await message.edit(asset)
    await message.edit('**\n YEAH BABE\n\n    đĽş                        \n   / [] \                              \n    (( B======đđŚ  /       /\n    /   \                 đśâđŤď¸====\n                                  \       \  **')

@Client.on_message(filters.regex('^gun$', re.I) & filters.me)
async def gun(client: Client, message: Message):
    pros_animation = ['Ř¨ŮŰŘą \n âď¸ťĚˇâťââä¸ â','Ř¨ŮŰŘą \n âď¸ťĚˇâťââä¸ â â','Ř¨ŮŰŘą \n âď¸ťĚˇâťââä¸ â â â',' Ř¨ŮŰŘą \n âď¸ťĚˇâťââä¸ â â â â','Ř¨ŮŰŘą \n âď¸ťĚˇâťââä¸ â â â â â']
    run_animation = 4

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(f'{asset}')
