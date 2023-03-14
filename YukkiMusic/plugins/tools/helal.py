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
        photo=f"https://telegra.ph/file/b56b90ec8ae744c01048e.jpg",
        caption=f"""✧ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑺𝒐𝒖𝒓𝒄𝒆 𝒍𝒊𝒏𝒅𝒂 ♪\n\n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [𝖫𝗂𝗇𝖪 𝖥𝗅𝖺𝗆𝖾𝖭𝖼𝗈 .¹](t.me/FH_KN) \n• ᴅᴇᴠᴇʟᴏᴘᴇʀ » [𝖫𝗂𝗇𝖪 𝖥𝗅𝖺𝗆𝖾𝖭𝖼𝗈 .](t.me/llL_67o) \n• ᴄʜᴀɴɴᴇʟ 𝙻𝙸𝙽𝙳𝙰 » [ᴄʜᴀɴɴᴇʟ](t.me/FH_KP)\n\n**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات فلامنكو", url=f"https://t.me/o_xox")
                ]
            ]
        ),
    )     
@app.on_message(
    filters.command(["اوامرفلامنكو","الاوامر"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/15ab2ecef4cc16d95be30.jpg",
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
                InlineKeyboardButton("تحديثات فلامنكو ♪", url=f"https://t.me/o_xox")
                ]
            ]
        ),
    )  
@app.on_message(
    filters.command(["بوت الحذف"],""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7bc5810a111c94694e66a.jpg",
        caption=f"""فڪـر قبـل لا تحذف 🥺..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("بـوت الحـذف", url=f"https://t.me/DTeLebot"),
                ],[
                InlineKeyboardButton(
                        "تحديثات فلامنكو", url=f"https://t.me/o_xox"),
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["بوت"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""اي يقلبـي 🤍😻""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات فلامنكو ♪", url=f"https://t.me/o_xox")
                ]
            ]
        ),
    ) 
@app.on_message(
    filters.command(["مين انا"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""انت قلبي ❤😻""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات فلامنكو ♪", url=f"https://t.me/o_xox")
                ]
            ]
        ),
    )       
@app.on_message(
    filters.command(["انا مين"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""ـ• ﺂٰنـُـٰٰت ﺂٰلـُُـٰ؏ـٖمـࢪَٰٰي َ،🤭♥️ ֆ ۦٰ،""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات فلامنكو ♪", url=f"https://t.me/o_xox")
                ]
            ]
        ),
    )           
@app.on_message(
    filters.command(["فلامنكو"],""))
def reply_to_timo(Client, message):
    message.reply_text(
        f"""اي يقلبي 🤍😻""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("تحديثات فلامنكو ♪", url=f"https://t.me/o_xox")
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(["ميديا", "/tm", "tgm"],""))
async def get_link_group(client, message):

    try:

        text = await message.reply("Processing...")

        async def progress(current, total):

            await text.edit_text(f"🕷 يتم رفع الوسائط ... {current * 100 / total:.1f}%")

        try:

            location = f"./media/group/"

            local_path = await message.reply_to_message.download(location, progress=progress)

            await text.edit_text("🕷 يتم جلب الرابط ... 🕸")

            upload_path = upload_file(local_path) 

            await text.edit_text(f"**🕸 | 𝘵𝘦𝘭𝘦 𝘭𝘪𝘯𝘬 **:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     

            os.remove(local_path) 

        except Exception as e:

            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")

            os.remove(local_path) 

            return         

    except Exception:

        pass          


@app.on_message(
    filters.command(["الرابط"],""))
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("قم برفعي مسؤول في المجموعة أولا ؟")
    await message.reply_text(f"**تم إنشاء رابط الدعوة بنجاح :**\n {invitelink}")
    
