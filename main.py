import asyncio
from settings import bot, dp
import user
import postback


async def main():
    _token = '6681667923:AAHNd2vwObvWwgFqF2-hgM2W1lxcuZdDD5E'
    dp.include_routers(user.router, postback.router)
    await dp.start_polling(bot)


asyncio.run(main())
