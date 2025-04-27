import telebot
from telebot import types

# token
TOKEN = ''

bot = telebot.TeleBot(TOKEN)

# /mute
@bot.message_handler(commands=['mute'])
def mute_user(message):
    if not message.reply_to_message:
        bot.reply_to(message, "باید روی پیام یه نفر ریپلای کنی تا میوت بشه!")
        return

    try:
        bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=types.ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_polls=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False
            )
        )
        bot.reply_to(message, f"کاربر {message.reply_to_message.from_user.first_name} میوت شد! 🔇")
    except Exception as e:
        bot.reply_to(message, f"خطا در میوت کردن: {e}")

# /unmute
@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    if not message.reply_to_message:
        bot.reply_to(message, "باید روی پیام یه نفر ریپلای کنی تا آن‌میوت بشه!")
        return

    try:
        bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=types.ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_polls=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=False
            )
        )
        bot.reply_to(message, f"کاربر {message.reply_to_message.from_user.first_name} آن‌میوت شد! 🔊")
    except Exception as e:
        bot.reply_to(message, f"خطا در آن‌میوت کردن: {e}")

bot.infinity_polling()
