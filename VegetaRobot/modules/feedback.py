from LuffyRobot import pgram as bot, SUPPORT_CHAT
from pyrogram import filters
import random
from datetime import datetime
from pyrogram.types import *

#made by t.me/nandhaxd

vegeta_img = [ "https://telegra.ph/file/62f89dd5806510b054635.jpg", 
"https://telegra.ph/file/255aeb793773c74398a13.jpg",
"https://telegra.ph/file/21ae855857ea1259d5895.jpg",
"https://telegra.ph/file/6e3caf3d3a199ae15dabc.jpg"]

@bot.on_message(filters.group & filters.command(["feedback","bug"]))
async def feedback(_, m):
         if len(m.command) < 2:
               await m.reply_text("**Gime a Feedback!**")
               return 
         text = m.text.split(None, 1)[1]
         user = m.from_user
         chat = m.chat
         datetimes_fmt = "%d-%m-%Y"
         datetimes = datetime.utcnow().strftime(datetimes_fmt)
         feedback = f""" **#NewFeedBack**
FromChat: @{chat.username}
user_id: {user.id}
mention: {user.mention}
msg_date: {datetimes}
Feedback: **{text}**
"""      
         msg = await bot.send_photo(f"@{SUPPORT_CHAT}",random.choice(vegeta_img),caption=feedback,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "➡ View Report", url=f"{m.link}"),
                            InlineKeyboardButton(
                                "❌ Close", callback_data="close")
                        ]
                    ]
                )
            )
    

         await m.reply_text("Your feedback Successfully Reported On SupportChat!",
                    reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "➡ View Report", url=f"{msg.link}")]]))
         
__help__ = """ •
• /feedback: found any bugs or commands not working and
What's your experience In this bot everything you can use this module.😁

Example:
• /feedback: bot spamming!

Thanks for your feedbacks!
"""
__mod_name__ = "feedback"
