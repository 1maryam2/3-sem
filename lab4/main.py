from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram import Bot, Dispatcher, Router, F
import asyncio
from datetime import datetime
from get_text_of_horoscope import get_text_of_horoscope


router: Router = Router()
BOT_TOKEN = '7942017814:AAEZmEO0NqGHpaibBp0SwuZURsmK66_e3fI'

zodiac_names = {
    "aries": "Овен ♈",
    "taurus": "Телец ♉",
    "gemini": "Близнецы ♊",
    "cancer": "Рак ♋",
    "leo": "Лев ♌",
    "virgo": "Дева ♍",
    "libra": "Весы ♎",
    "scorpio": "Скорпион ♏",
    "sagittarius": "Стрелец ♐",
    "capricorn": "Козерог ♑",
    "aquarius": "Водолей ♒",
    "pisces": "Рыбы ♓",
}

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Привет! Выбери любую команду:', reply_markup=get_command())

@router.callback_query(F.data == 'zodiac_of_user')
async def send_zodiac_keyboard(call: CallbackQuery):
    await call.message.edit_text(text='Выберите свой знак зодиака:', reply_markup=get_zodiac_keyboard())

@router.callback_query(F.data.in_(['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']))
async def get_horoscope(call: CallbackQuery):
    zodiac = call.data
    text = await get_text_of_horoscope(zodiac=zodiac)
    if text:
        await call.message.edit_text(text=text, reply_markup=get_zodiac_keyboard_with_back())
    else:
        await call.message.answer("Гороскоп для данного знака не найден.", reply_markup=get_zodiac_keyboard_with_back())

@router.callback_query(F.data == 'data_of_user')#написать реализацию
async def get_horoscope_1(call: CallbackQuery):
    await call.message.answer('Введите свою дату рождения в формате ДД.ММ.ГГГГ:')

@router.message()#сейм
async def process_date_input(message: Message):
    try:
        date_str = message.text
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        zodiac_sign = get_zodiac_sign_by_date(date_obj)
        horoscope_text = await get_text_of_horoscope(zodiac=zodiac_sign)
        if horoscope_text:
            response_text = f'Ваш знак зодиака: {zodiac_names[zodiac_sign]}\n\n{horoscope_text}'
            await message.answer(text=response_text, reply_markup = get_command())
        else:
            await message.answer("Гороскоп для вашего знака не найден.")

    except ValueError:
        await message.answer('Неверный формат даты. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ.')
    except Exception as e:
        print(f"An error occured: {e}")
        await message.answer("Произошла ошибка, попробуйте снова")


def get_zodiac_sign_by_date(date: datetime) -> str:
    day = date.day
    month = date.month
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "gemini"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "libra"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "scorpio"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "aquarius"
    else:
        return "pisces"

def get_zodiac_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Овен ♈', callback_data='aries')
    keyboard_builder.button(text='Телец ♉', callback_data='taurus')
    keyboard_builder.button(text='Близнецы ♊', callback_data='gemini')
    keyboard_builder.button(text='Рак ♋', callback_data='cancer')
    keyboard_builder.button(text='Лев ♌', callback_data='leo')
    keyboard_builder.button(text='Дева ♍', callback_data='virgo')
    keyboard_builder.button(text='Весы ♎', callback_data='libra')
    keyboard_builder.button(text='Скорпион ♏', callback_data='scorpio')
    keyboard_builder.button(text='Стрелец ♐', callback_data='sagittarius')
    keyboard_builder.button(text='Козерог ♑', callback_data='capricorn')
    keyboard_builder.button(text='Водолей ♒', callback_data='aquarius')
    keyboard_builder.button(text='Рыбы ♓', callback_data='pisces')
    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()

@router.callback_query(F.data == 'back_to_main')
async def back_to_main_menu(call: CallbackQuery):
    await call.message.edit_text("Выберите команду:", reply_markup=get_command())

def get_zodiac_keyboard_with_back():
    keyboard_builder = InlineKeyboardBuilder()
    for sign, name in zodiac_names.items():
        keyboard_builder.button(text=name, callback_data=sign)
    keyboard_builder.add(InlineKeyboardButton(text='Назад', callback_data='back_to_main'))  # Кнопка "Назад"
    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()

def get_command():
    keyboard_builder1 = InlineKeyboardBuilder()
    keyboard_builder1.button(text='Выбрать свой знак зодиака', callback_data='zodiac_of_user')
    keyboard_builder1.button(text='Расчитать знак зодиака по дате рождения', callback_data='data_of_user')
    keyboard_builder1.adjust(1)
    return keyboard_builder1.as_markup()

async def main():
    bot: Bot = Bot(token=BOT_TOKEN)
    dp: Dispatcher = Dispatcher()
    dp.include_router(router=router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())