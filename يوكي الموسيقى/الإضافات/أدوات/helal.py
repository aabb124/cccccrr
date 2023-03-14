import sys
import asyncio
import requests
import re
import string
from pyrogram.types import Message
from aiohttp import ClientSession
from pyrogram import filters, Client
from strings import get_command
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

#########
#الاوامر    
@app.on_message(
    filters.command(["سورس","السورس"],""))
async def sourc(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/a054bc6d56a5bebcb092d.jpg",
        caption=f"""Welcome To Source""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("السورس", url=f"https://t.me/o_xox")
                ]
            ]
        ),
    )     
@app.on_message(
    filters.command(["الاوامر"))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/235b5af8b3f68f7b1a57e.jpg",
        caption=f"""𝑤𝑒𝑙𝑐𝑜𝑚𝑒 {message.from_user.mention}
        
« اليك قائـمة الاوامــر »
          

»**لتشغيل اغنيه اكتب : تشغيل او شغل**
»**لأنهاء الاغنيه اكتب : ايقاف او انهاء**
»**لايقاف الاغنيه مؤقت اكتب : قفي**
»**لتكملة الاغنيه من الايقاف المؤقت اكتب : كمل او استمر**
»**لتخطي الاغنيه اكتب : تخطي او التالي**
»**لكتم البوت في المحادثه اكتب : اسڪتي**
»**لألغاء كتم البوت في المحادثه اكتب : اتكلم او تكلمي**
»**لتحميـل الاغانـي اڪتب : بحث او تحميل**
»**لاعادة تشغيل البوت اكتب** : /restart.""",
      reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("السورس", url=f"https://t.me/o_xox")
                ]
            ]
        ),
