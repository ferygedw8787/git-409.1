import logging
from config import TOKEN
from aiogram import BOt,Dispatcher,exector,types
from translate import to_cyrillic,to_latin

6
API_TOKEN=TOKEN


logging.basicConfig(level=logging.INFO)
bot=Bot(API_TOKEN)
dp=Dispatcher

@dp.message_handler(commands=['start'])
async def boshlash(message:types.Message):
    """"Botga/start buyryg`ini yozilganda ishga tushadi"""

    
