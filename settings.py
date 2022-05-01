"""
Это файл для хранения константных настроек, таких как токены,
ID группы и других вспомогательных переменных/классов/объектов.
"""


from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule

###################################################################################################

"""Токен бота
Для получения необходимо перейти в управление группой → Работа с API → Создать ключ

Полученный ключ скопировать и вставить в переменную ниже.
"""
BOT_TOKEN = '3f27ee7eeed4a0fbbd25ca10268e5ac9a7ca76c039572968e72e505f157c8af4ef43b9d4eba3f9f9757d8'

###################################################################################################

"""Токен пользователя
Для получения необходимо перейти по ссылке https://vkhost.github.io, выбрать "vk.com" → Разрешить.

Адресная строка будет выглядеть так: 

https://oauth.vk.com/blank.html#access_token=<ВАШ_ДЛИННЫЙ_ТОКЕН>&expires_in=86400&user_id=<ВАШ_ID>

Оттуда нужно скопировать токен и вставить в переменную ниже.
"""
API_TOKEN = '5ac36922e028dbb5fad9ee24c64881b4937c15e53f3803b1b039948b5dcd19128d955d1b9e25a0c2a806c'

###################################################################################################

# ID группы
GROUP_ID = -206953782

###################################################################################################

# Плейлист с треками для рандома
PLAYLIST = (
    "audio-2001569263_106569263",
    "audio-2001314735_104314735",
    "audio-2001666307_107666307",
    "audio-2001485231_107485231",
    "audio-2001179822_107179822",
    "audio-2001460832_107460832",
    "audio-2001064907_106064907",
    "audio-2001139034_107139034",
    "audio-2001139066_107139066",
    "audio-2001735638_106735638",
    "audio-2001900514_105900514",
    "audio-2001732849_106732849",
    "audio-2001634477_106634477",
    "audio-2001855393_104855393",
    "audio-2001146727_107146727",
    "audio-2001302334_106302334",
    "audio-2001240319_104240319",
    "audio-2001240319_104240319",
    "audio-2001138967_107138967",
    "audio-2001138971_107138971",
)

###################################################################################################


class GreetingRule(ABCRule[Message]):
    """Фильтр приветствия"""
    async def check(self, event: Message) -> bool:
        greetings = (
            'привет',
            'приветствую',
            'здравствуй',
            'здравствуйте',
            'хай',
            'здорово',
            'ку',
            'начать',
            'ghbdtn',
            'qq'
        )
        return event.text.lower() in greetings

###################################################################################################


CONSTANTS = {
    'BOT_TOKEN': BOT_TOKEN,
    'API_TOKEN': API_TOKEN,
    'GROUP_ID': GROUP_ID,
    'PLAYLIST': PLAYLIST,
    'GREETING_RULE': GreetingRule,
}