import random
import feedparser
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

python_wiki_rss_url= "https://news.yandex.ru/koronavirus.rss"   # Ссылка на rss новости, возможны любые новости в формате rss

feed = feedparser.parse( python_wiki_rss_url )

summ = 0
ft = []
for post in feed.entries:
    ft.append(post.title + "\n" + post.description + "\n" + post.link) # Разбиваем ленту на новости

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ созданный ранее
token = "Токин съели конспирологи:((("

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Commander
commander = Commander()

print("Бот запущен")
# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, ft[random.randint(0, 5)])

