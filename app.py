from datetime import datetime
from typing import Tuple
import random

from vkbottle import API, DocMessagesUploader
from vkbottle.bot import Bot, Message
from vkbottle.dispatch.rules.base import CommandRule

from keyboards import keyboard
from jokes_api import get_joke
from messages import MSG
from settings import CONSTANTS


# Объект бота
bot = Bot(token=CONSTANTS['BOT_TOKEN'])

# Объект API
api = API(token=CONSTANTS['API_TOKEN'])


@bot.on.message(command="помощь")
@bot.on.message(command="help")
@bot.on.message(payload={"cmd": "help"})
async def help_handler(message: Message):
    """Хэндлер команды /помощь (/help)"""
    await message.answer(MSG['help'])


@bot.on.message(command="автор")
@bot.on.message(command="author")
@bot.on.message(payload={"cmd": "author"})
async def author_handler(message: Message):
    """Хэндлер команды /автор (/author)"""
    text = 'Меня создала *id163865908 (Дарья Ильюшина) из группы 20-ПРИ.'
    await message.answer(text)


@bot.on.message(command="время")
@bot.on.message(command="time")
@bot.on.message(payload={"cmd": "time"})
async def time_handler(message: Message):
    """Хэндлер команды /время (/time)"""
    # Получаем текущий объект datetime
    now = datetime.now()

    # Получаем дату
    date = now.strftime(r"%d.%m.%Y")

    # Получаем время
    time = now.strftime(r"%H:%M")

    text = f'Сегодня {date}, на часах {time}.'
    await message.answer(text)


@bot.on.message(command="анекдот")
@bot.on.message(command="joke")
@bot.on.message(payload={"cmd": "joke"})
async def joke_handler(message: Message):
    """Хэндлер команды /анекдот (/joke)"""
    # Кортеж возможных вариантов ответа
    answers = (
        "Я погуглил и нашёл этот анекдот:",
        "Вспомнил ещё такой анекдот:",
        "Не ручаюсь за этот анекдот, нашёл его в Интернете. Рассказываю:",
        "Случайный анекдот из Интернета:"
    )

    # Выбираем случайный ответ из кортежа
    text = random.choice(answers)
    text += f'\n\n{get_joke()}'

    await message.answer(text)


@bot.on.message(command="музыка")
@bot.on.message(command="music")
@bot.on.message(payload={"cmd": "music"})
async def music_handler(message: Message):
    """Хэндлер команды /музыка (/music)"""
    # Кортеж возможных вариантов ответа
    answers = (
        "Смотри, какую песню нашёл!",
        "Послушай это:",
        "Как насчёт такой песни?",
        "Вот тебе замечательная песня."
    )
    # Выбираем случайный ответ из кортежа
    text = random.choice(answers)

    # Выбираем случайный трек из плейлиста
    track = random.choice(CONSTANTS["PLAYLIST"])

    await message.answer(text, attachment=track)


@bot.on.message(command="пост")
@bot.on.message(command="post")
@bot.on.message(payload={"cmd": "post"})
async def post_handler(message: Message):
    """Хэндлер команды /пост (/post)"""
    # Получаем список постов группы
    posts = await api.wall.get(CONSTANTS["GROUP_ID"])

    # Получаем последний пост из списка
    post = posts.items[1]

    # Формируем ID поста
    attachment = f'wall{CONSTANTS["GROUP_ID"]}_{post.id}'

    # Кортеж возможных вариантов ответа
    answers = (
        "Нашёл для тебя последний пост:",
        "Вот последний пост из группы:",
        "Недавний пост:",
        "Последняя публикация в группе:"
    )

    # Выбираем случайный ответ из кортежа
    text = random.choice(answers)

    await message.answer(text, attachment=attachment)


@bot.on.message(command="сбщ")
@bot.on.message(command="msg")
@bot.on.message(payload={"cmd": "msg"})
@bot.on.message(CommandRule("сбщ", ["/"], 1, "\r"))
@bot.on.message(CommandRule("msg", ["/"], 1, "\r"))
async def msg_handler(message: Message, args: Tuple[str] = None):
    """Хэндлер команды /сбщ (/msg)"""
    # Если команда вызвана без аргументов
    if not args:
        return await message.answer(MSG['msg_help'])

    # Получаем текст из аргументов
    msg = ' '.join(args)

    # Публикуем на стене запись с текстом от имени группы
    await api.wall.post(CONSTANTS["GROUP_ID"], from_group=True, message=msg)

    # Кортеж возможных вариантов ответа
    answers = (
        "Беги проверять, пост уже в группе!\n\n",
        "Отправил это сообщение в группу.\n\n",
        "Сообщение успешно отправлено в группу!\n\n",
        "Опубликовал на стене группы твоё сообщение.\n\n"
    )

    # Выбираем случайный ответ из кортежа
    text = random.choice(answers)

    await message.answer(f'{text}Вот его текст: {msg}')


@bot.on.message(command="файл")
@bot.on.message(command="file")
@bot.on.message(payload={"cmd": "file"})
@bot.on.message(CommandRule("файл", ["/"], 1))
@bot.on.message(CommandRule("file", ["/"], 1))
async def file_handler(message: Message, args: Tuple[str] = None):
    """Хэндлер команды /файл (/file)"""
    # Если команда вызвана без аргументов
    if not args:
        return await message.answer(MSG['file_help'])

    # Название файла
    filename = args[0]

    # Расширение файла
    extension = filename.split('.')[1]

    # Список запрещённых к отправке расширений
    forbidden_exts = ('.mp3', '.zip', '.rar', '.exe')

    # Проверка наличия расширения в списке запрещённых
    if extension in forbidden_exts:
        return await message.answer(
            'К сожалению, API ВК не позволяет мне отправить файл с таким расширением. '
            'Может быть, попробуем другой файл?'
        )

    # Если все хорошо, просто отправляем файл

    uploader = DocMessagesUploader(bot.api, generate_attachment_strings=True)
    try:
        uploaded_file = await uploader.upload(file_source=f'./documents/{filename}', title=f'{filename}', peer_id=message.from_id)
        await message.answer(f'Вот файл {filename}.', attachment=uploaded_file, )
    except:
        # Возникла ошибка? Скорее всего, файла не существует
        return await message.answer(f"Извини, я не могу найти файл {filename}.")


@bot.on.message()
async def all_handler(message: Message):
    """Хэндлер обработки всех остальных сообщений и приветствия"""
    """Хэндлер приветствия"""
    users = await bot.api.users.get(message.from_id)
    first_name = users[0].first_name
    await message.answer(f"Привет, {first_name}!\nСписок команд: /help /помощь", keyboard=keyboard)

bot.run_forever()
