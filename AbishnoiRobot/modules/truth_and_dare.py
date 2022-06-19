import html
import random
import AbishnoiRobot.modules.truth_and_dare_string as truth_and_dare_string
from AbishnoiRobot import dispatcher
from telegram import ParseMode, Update, Bot
from AbishnoiRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__help__ = """
*Tʀᴜᴛʜ & Dᴀʀᴇ*

 ❍ /truth *:* Sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ
 ❍ /dare *:* Sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ
"""
__mod_name__ = "Tʀᴜᴛʜ-Dᴀʀᴇ"
