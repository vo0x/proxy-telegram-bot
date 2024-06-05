import asyncio.staggered
from pyrogram import Client, filters, idle
from proxys import proxys
import asyncio
import random
# setup the bot
api_id = int('your api_id')
api_hash = 'your api_hash'
bot_token = 'your bot_token'
app = Client(
    'proxy bot',
    api_id = api_id,
    api_hash = api_hash,
    bot_token = bot_token
)
# start 
@app.on_message(filters.command('start'))
async def start(_, message):
    await app.send_message(message.chat.id, 'welcome to the proxy bot')
# command
@app.on_message(filters.command('getproxy'))
async def proxy(_, message):
    proxy = random.choice(proxys)
    #if you paste a ready links just skip the proxy info and replace {proxy_info}with {proxy}
    proxy_info = f'server:{proxy['server']}\nport:{proxy['port']}\nSecret:{proxy['secret']}'
    await app.send_message(message.chat.id, f'here is you proxy:\n\n{proxy_info}')

async def main():
    await app.start()
    await idle()
    await app.stop()

if __name__ == '__name__':
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop=loop)        
    loop.run_until_complete()
