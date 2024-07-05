import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
import random

# Join us on Telegram: https://t.me/NS8_b

# Setup the bot
api_id = int('your api_id')
api_hash = 'your api_hash'
bot_token = 'your bot_token'

app = Client(
    'proxy_bot',
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)
#keyboard
keyboard = [
    [KeyboardButton("proxy 1")],
    [KeyboardButton("proxy 2")],
    [KeyboardButton("proxy 3")],
    [KeyboardButton("proxy 4")],
    [KeyboardButton("proxy 5")],
]
# put the your proxy in this list
proxys = []
# Start command
@app.on_message(filters.command('start')& filters.private)
async def start(_, message):
    reply_markp = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await message.reply("""
    **Welcome to the proxy bot**

    here you can get free tgproxys 

    dev : @NS8_b
    """,reply_markup = reply_markup)
# proxy handler
@app.on_message(filters.text& filters.private)
async def proxy_handler(_, message):
    chat_id = message.chat.id
    proxy = random.choice(proxys)
    if message.text == 'proxy 1':
        await app.send_message(chat_id, proxy)
    if message.text == 'proxy 2':
        await app.send_message(chat_id, proxy)
    if message.text == 'proxy 3':
        await app.send_message(chat_id, proxy)
    if message.text == 'proxy 4':
        await app.send_message(chat_id, proxy)
    if message.text == 'proxy 5':
        await app.send_message(chat_id, proxy)
    


# Main function to run the bot
async def main():
    await app.start()
    await idle()
    await app.stop()

# Ensure the script is run directly
if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
