import config
import logging

from aiogram import Bot, Dispatcher, executor, types

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализация бота

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)
# эхо

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.txt)
# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)