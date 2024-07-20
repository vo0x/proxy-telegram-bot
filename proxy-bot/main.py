import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, CallbackQuery
import random
import asyncio
# setup the bot
api_id = int('api id')
api_hash = 'api_hashf'
bot_token = 'bot_token'
app = Client(
    'proxy-bot',
    api_id= api_id,
    api_hash= api_hash,
    bot_token=bottoken
)
#register users
def register_user(user_id):
    # user_id = message.from_user.id
    try:
        with open("users.txt", "r+") as file:
            existing_ids = file.readlines()
            if str(user_id) + "\n" not in existing_ids:
                file.write(str(user_id) + "\n")
                
           
    except FileNotFoundError:
        with open("users.txt", "w") as file:
            file.write(str(user_id) + "\n")
           
    except Exception as e:
        print(f"Error registering user: {e}")
# markup
markup = {
    'main_button' : InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('✅الحصول على بروكسي', callback_data='get_proxy')],
            [InlineKeyboardButton('🧑‍💻المطور', url='https://t.me/v_o0x')]
        ]
    ) ,
    
    'get_another': InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('🔃الحصول على بروكسي اخر', callback_data='get_another')],
            [InlineKeyboardButton('- رجوع -', callback_data = 'back')]
        ]
    ),

    
}
proxys = ['write your proxys here']
# commands 
@app.on_message(filters.command('start')&filters.private)
async def start(_, message: Message):
    user_id = message.from_user.id
    register_user(user_id)
    start_message = '''مرحبا بك في بوت بروكسي @NS8_b✅
     
      هنا يمكنك على بروكسيات التليجرام بطريقة سهلة ومجانية '''
    await message.reply(start_message, reply_markup=markup['main_button'])
@app.on_message(filters.command('help')&filters.private)
async def help(_, message : Message):
    help_message = '''
مرحبا بك في قسم المساعدة:

- للحصول على بوكسي اضغط على زر الحصول على بروكسي

- اذا كانت حالة البروكسي (unavailable) اضغط على زر الحصول على بروكسي اخر

- للمزيد من المعلومات والبوتات نرجو منك زيارة قناتنا
'''
    help_markup = InlineKeyboardMarkup([[InlineKeyboardButton('قناتنا', url='https://t.me/NS1_8')]])
    await message.reply(help_message, reply_markup = help_markup)

# buttons handler 
@app.on_callback_query()
async def call(_, call : CallbackQuery):
    proxy = random.choice(proxys)
    if call.data == 'get_proxy':
        await call.message.edit_text(f'اليك البروكسي :\n \n{proxy}', reply_markup=markup['get_another'])
    elif call.data == 'get_another':
        await call.message.edit_text(f'اليك البروكسي :\n \n{proxy}', reply_markup=markup['get_another'])
    elif call.data == 'back':
        start_message = '''مرحبا بك في بوت بروكسي @NS8_b✅
     
      هنا يمكنك على بروكسيات التليجرام بطريقة سهلة ومجانية '''
        await call.message.edit_text(start_message, reply_markup=markup['main_button'])

app.run()

