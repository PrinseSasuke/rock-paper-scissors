async def on_startup(dp):
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)
    from utils.db_api.db_gino import on_startup
    from loader import db
    print("Подключение к Postgressql")
    await on_startup(dp)
    print("Создание таблиц")
    await db.gino.create_all()
    print("Готово")
    print('Бот запущен')
if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup = on_startup)