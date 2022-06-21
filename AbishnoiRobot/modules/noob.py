import asyncio
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,                             InlineKeyboardMarkup, InputMediaPhoto, Message)


from AbishnoiRobot import pbot as bot
      
ABISHNOI = "https://telegra.ph/file/348fd99cf32b44153f5c1.jpg"  

@bot.on_message(filters.command(["noob", "owner"]))
async def repo(client, message):   
       await message.reply_photo(      
            photo=ABISHNOI,      
            caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 Aʟɪsʜᴀ 𒆜 ʀᴏʙᴏᴛ 」](t.me/QueenAlishaRobot)**
""",        
            reply_markup=InlineKeyboardMarkup(   
                  [          
                        [          
                              InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/VeNoM_HAi_HuM"),        
                              
                        ]     
                  ]      
            ),     
      )
      
       
        
         

              
                
                      
                      
                        
                          
             

                                       
                                        
__mod_name__ = "Oᴡɴᴇʀ" 

