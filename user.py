from aiogram import Router, F
from aiogram.filters import Command
from aiogram.methods import SendVideo
from aiogram.types import Message, CallbackQuery
from settings import IMAGE_PATH, bot
import os
import db_api
from aiogram.types import FSInputFile
import keyboards

router = Router()


@router.message(Command('start'))
async def start(message: Message):
    db_api.add_user(message.chat.id, message.chat.username)

    await message.reply_photo(
        FSInputFile(os.path.join(IMAGE_PATH, 'start.png')),
        caption='Выбери тариф 👇',
        reply_markup=keyboards.start.as_markup()
    )


@router.callback_query(F.data == 'free')
async def get_free(call: CallbackQuery):
    # send привет.mp4
    await bot(SendVideo(
        chat_id=call.message.chat.id,
        video='BAACAgIAAxkBAAM0ZT66Xb67qMTlahsFP4l1e5g-sVoAAmxAAALdAfFJHOTNwTBrocAwBA',
        caption='Салют👋🏻\n\n'
                'Если ты здесь, то вероятно хочешь получить бесплатный доступ на 3 дня в мою ЗАКРЫТУЮ ГРУППУ'
                ' С СИГНАЛАМИ из проги LuckyJet Hack v4.0\n\n'
                'За это время ты успеешь заработать на месячный тариф и уже сможешь приобрести доступ✊🏻\n\n'
                '❗ Итак, нужно выполнить ряд простых действий, чтобы получить доступ и начать зарабатывать\n\n'
                '✅Это полностью БЕСПЛАТНО\n\n'
                '⛔️Без этих действий ты не будешь добавлен в группу\n\n'
                'Нажми «ВСТУПИТЬ В ГРУППУ» для продолжения👇🏻',
        reply_markup=keyboards.join_group.as_markup()
    ))


@router.callback_query(F.data == 'check_reg')
async def check_reg(call: CallbackQuery):
    user = db_api.get_user(call.message.chat.id)
    if user[2]:
        deposit = db_api.get_postback_by_site_id(user[2])[1]

        if deposit:
            return await bot.send_photo(
                chat_id=call.message.chat.id,
                photo=FSInputFile(os.path.join(IMAGE_PATH, 'access.png')),
                caption='Пополнение зачислено✅\n'
                        '😇Поздравляю, ты можешь вступить в закрытую группу и получить доступ к ПРИВАТНЫМ СИГНАЛАМ!',
                reply_markup=keyboards.final.as_markup()
            )

        await bot(SendVideo(
            chat_id=call.message.chat.id,
            video='BAACAgIAAxkBAAMzZT659DIom9x9fzxBAAFrWyeze2LpAAJnQAAC3QHxSUPVh4sSXfr6MAQ',
            caption='✅РЕГИСТРАЦИЯ УСПЕШНА!\n\n'
                    '‼️Для того, чтобы получить доступ в закрытую группу с сигналами, необходимо на любую сумму'
                    ' пополнить баланс аккаунта, который вы только что зарегистрировали.\n'
                    'На эти деньги вы будете делать ставки по сигналам.\n\n'
                    '✅После успешного пополнения бот АВТОМАТИЧЕСКИ выдаст вам ссылку на вступление в группу'
        ))


@router.callback_query(F.data == 'join_group')
async def join_group(call: CallbackQuery):
    # send code.mov
    await bot(SendVideo(
        chat_id=call.message.chat.id,
        video='BAACAgIAAxkBAAMyZT65dntbPh037mFlLTKDxA-ANy8AAmVAAALdAfFJ15TbZbfe-fQwBA',
        caption='📲Для начала необходимо провести регистрацию на 1win (провайдер игры LuckyJet). Чтобы бот успешно '
                'проверил регистрацию, нужно соблюсти важные условия:\n\n'
                '1️⃣Аккаунт обязательно должен быть НОВЫМ! Если у вас уже есть аккаунт и при нажатии на кнопку'
                ' «РЕГИСТРАЦИЯ» '
                'вы попадаете на старый, необходимо выйти с него и заново нажать на кнопку «РЕГИСТРАЦИЯ»,'
                ' после чего по новой зарегистрироваться!\n\n'
                '2️⃣Чтобы бот смог проверить вашу регистрацию, обязательно нужно ввести промокод MAYOT555 '
                'при регистрации!\n\n'
                '⚠️Как ввести промокод можно узнать здесь: https://t.me/+aN4a4KZDKsM5MWRi\n\n'
                'После РЕГИСТРАЦИИ бот автоматически переведёт вас к следующему шагу✅\n\n',
        reply_markup=keyboards.get_reg_keyboard(call.message.chat.id).as_markup()
    ))
