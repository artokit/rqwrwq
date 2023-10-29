from aiogram import Router, F
from aiogram.methods import SendVideo
from aiogram.types import Message, FSInputFile
import db_api
import os

import keyboards
from settings import bot, IMAGE_PATH

router = Router()
CHANNEL_POSTBACK = -1001503014145


@router.channel_post(F.chat.id == CHANNEL_POSTBACK)
async def get_postback(message: Message):
    data = message.text.split(':')

    if message.text.endswith('reg'):
        site_id, user_id, _ = data
        db_api.add_reg_user(int(site_id))
        db_api.update_user_site_id(int(user_id), int(site_id))

        # send пополнение.mp4.

        await bot(SendVideo(
            chat_id=int(user_id),
            video='BAACAgIAAxkBAAMzZT659DIom9x9fzxBAAFrWyeze2LpAAJnQAAC3QHxSUPVh4sSXfr6MAQ',
            caption='✅РЕГИСТРАЦИЯ УСПЕШНА!\n\n'
                    '‼️Для того, чтобы получить доступ в закрытую группу с сигналами, необходимо на любую сумму'
                    ' пополнить баланс аккаунта, который вы только что зарегистрировали.\n'
                    'На эти деньги вы будете делать ставки по сигналам.\n\n'
                    '✅После успешного пополнения бот АВТОМАТИЧЕСКИ выдаст вам ссылку на вступление в группу'
        ))

    if len(data) == 2:
        user = db_api.get_user_by_site_id(int(data[0]))
        db_api.update_deposit(int(data[0]), int(data[1]))

        await bot.send_photo(
            chat_id=user[0],
            photo=FSInputFile(os.path.join(IMAGE_PATH, 'access.png')),
            caption='Пополнение зачислено✅\n'
                    '😇Поздравляю, ты можешь вступить в закрытую группу и получить доступ к ПРИВАТНЫМ СИГНАЛАМ!',
            reply_markup=keyboards.final.as_markup()
        )
