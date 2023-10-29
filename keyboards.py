from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

start = InlineKeyboardBuilder()
start.row(
    InlineKeyboardButton(text='✅90.000₽ (вечный доступ)', url='http://24time2pay.ru/pay-id90.html'),
    InlineKeyboardButton(text='✅30.000₽ (доступ на месяц)', url='http://24time2pay.ru/pay-id90.html'),
    InlineKeyboardButton(text='🚀3 дня БЕСПЛАТНО', callback_data='free'),
    width=1,
)

join_group = InlineKeyboardBuilder()
join_group.add(InlineKeyboardButton(text='💸ВСТУПИТЬ В ГРУППУ💸', callback_data='join_group'))

final = InlineKeyboardBuilder()
final.row(
    InlineKeyboardButton(text='✅ВСТУПИТЬ В ГРУППУ', url='https://t.me/+98Fga5lE8Z42NjYy'),
    InlineKeyboardButton(text='👨‍💻ПОМОЩЬ', url='https://t.me/+aN4a4KZDKsM5MWRi'),
    width=1
)


def get_reg_keyboard(user_id):
    registration = InlineKeyboardBuilder()
    registration.row(
        InlineKeyboardButton(
            text='📲РЕГИСТРАЦИЯ',
            url=f'https://1wddjd.top/casino/list?open=register&sub1={user_id}'
        ),
        InlineKeyboardButton(text='🔎ПРОВЕРИТЬ РЕГИСТРАЦИЮ', callback_data='check_reg'),
        InlineKeyboardButton(text='👨‍💻ПОМОЩЬ', url='https://t.me/+aN4a4KZDKsM5MWRi'),
        width=1
    )
    return registration
