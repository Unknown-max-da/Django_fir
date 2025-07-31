from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Telefon raqamni yuborish', request_contact=True)
        ],
        [
            KeyboardButton(text='Lokatsiya yuborish',request_location=True),
            KeyboardButton(text='Adminga murojat')
        ],
        [
            KeyboardButton(text='/ariza'),
            KeyboardButton(text='/stop'),
            KeyboardButton(text='help')
        ]
    ],
    resize_keyboard=True,
    # is_persistent=True
    input_field_placeholder='Tugmalardan birini bosing!'
)


admin_murojaat_tasdiq=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ha'),
            KeyboardButton(text="yo'q")
        ]
    ]
)