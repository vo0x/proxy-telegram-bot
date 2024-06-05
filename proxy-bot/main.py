import asyncio
from pyrogram import Client, filters, idle
from proxys import proxys
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

# Start command
@app.on_message(filters.command('start'))
async def start(_, message):
    await message.reply("Welcome to the proxy bot")

# Get proxy command
@app.on_message(filters.command('getproxy'))
async def proxy(_, message):
    proxy = random.choice(proxys)
    # If you paste ready links, just skip the proxy info and replace {proxy_info} with {proxy}
    proxy_info = f'server: {proxy["server"]}\nport: {proxy["port"]}\nSecret: {proxy["secret"]}'
    await message.reply(f'Here is your proxy:\n\n{proxy_info}')

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
