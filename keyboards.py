"""
Это файл для хранения громоздкого синтаксиса клавиатуры.
"""


from vkbottle import Keyboard, KeyboardButtonColor, Text

keyboard = Keyboard(one_time=False, inline=False)

#!               Требования на 3

keyboard.add(
    Text("Кто автор?", payload={"cmd": "author"}),
    color=KeyboardButtonColor.SECONDARY
)

keyboard.row()  # Переходим на следующую строку
keyboard.add(
    Text("Что ты умеешь?", payload={"cmd": "help"}),
    color=KeyboardButtonColor.SECONDARY
)


# keyboard.row()  # Переходим на следующую строку
keyboard.add(
    Text("Сколько время?", payload={"cmd": "time"}),
    color=KeyboardButtonColor.SECONDARY
)


keyboard.row()  # Переходим на следующую строку
keyboard.add(
    Text("Как получить файл?", payload={"cmd": "file"}),
    color=KeyboardButtonColor.SECONDARY
)

#!               Требования на 4

keyboard.row()  # Переходим на следующую строку
keyboard.add(
    Text("Отправь последний пост", payload={"cmd": "post"}),
    color=KeyboardButtonColor.PRIMARY
)

keyboard.row()  # Переходим на следующую строку
keyboard.add(
    Text("Как отправить сообщение?", payload={"cmd": "msg"}),
    color=KeyboardButtonColor.PRIMARY
)

#!               Требования на 5

keyboard.row()  # Переходим на следующую строку
keyboard.add(
    Text("Расскажи анекдот", payload={"cmd": "joke"}),
    color=KeyboardButtonColor.POSITIVE
)


# keyboard.row()  # Переходим на следующую строку
keyboard.add(
    Text("Включи музыку", payload={"cmd": "music"}),
    color=KeyboardButtonColor.POSITIVE
)
