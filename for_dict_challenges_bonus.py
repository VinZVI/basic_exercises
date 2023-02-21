"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, которые стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice([None,
                                        random.choice([m["id"] for m in messages])
                                        if messages else None]),
            "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def print_user_max_massages(messages):
    # count_id = {}
    # for message in messages:
    #     id = message['sent_by']
    #     value = count_id.setdefault(id, 0)
    #     value += 1
    #     count_id[id] = value
    # id_max_massages = max(count_id, key=count_id.get)
    # print(f'ID пользователя, который написал больше всех сообщений: {id_max_massages}')
    # наверняка есть способ гораздо проще решить эту задачу (для закрепления list comprehensions)
    id_max_massages2 = max([(m['sent_by'], [n['sent_by'] for n in messages].count(m["sent_by"])) for m in messages],
                           key=lambda x: x[1])
    print(
        f'ID пользователя, который написал больше всех сообщений: {id_max_massages2[0]} - {id_max_massages2[1]} сообщений')


def print_user_max_reply(messages):
    counter_users_reply = {}
    for message in messages:
        for message_reply in messages:

            if message['reply_for'] == message_reply['id']:
                value = counter_users_reply.setdefault(message_reply['sent_by'], 0)
                counter_users_reply[message_reply['sent_by']] = value + 1

    user_max_reply = max(counter_users_reply, key=counter_users_reply.get)
    print(f'ID пользователя, на сообщения которого больше всего отвечали: {user_max_reply}')


def print_user_max_seen(messages):
    counter_users_seen = {}
    for message in messages:
        message_seen_by = set(message['seen_by'])
        value = counter_users_seen.setdefault(message['sent_by'], set())
        counter_users_seen[message['sent_by']] = value.union(message_seen_by)

    print(f"ID пользователей, сообщения которых видело больше всего уникальных пользователей: ")
    print(*[f'{key} - {len(value)} сообщений' for key, value in counter_users_seen.items()], sep='\n')


def print_time_max_messages(messages):
    counter_time_messages = {'до 12': 0, 'с 12 до 18': 0, 'после 18': 0}
    for message in messages:
        if 12 <= message['sent_at'].hour <= 18:
            counter_time_messages['с 12 до 18'] += 1
        elif 18 < message['sent_at'].hour < 24 or 0 <= message['sent_at'].hour < 4:
            counter_time_messages['после 18'] += 1
        else:
            counter_time_messages['до 12'] += 1

    print(f'Время, когда в чате больше всего сообщений: {max(counter_time_messages, key=counter_time_messages.get)} часов')

def print_id_message_long_tread(messages):
    capacity_tread = []

    for message in messages:

        if message['reply_for']:
            reply = message['reply_for']
            tread_messages = [message['id'], reply]
            while reply:
                for message_reply in messages:
                    if reply == message_reply['id']:
                        if message_reply['reply_for'] == None:
                            reply = None
                            break
                        else:
                            tread_messages.append(message_reply['reply_for'])
                            reply = message_reply['reply_for']
                            break
            capacity_tread.append(tread_messages)

    print(f'ID сообщения самых длинных тредов (цепочек ответов): {max(capacity_tread, key=lambda x: len(x))[-1]}')



if __name__ == "__main__":
    messages = generate_chat_history()
    print_user_max_massages(messages)
    print_user_max_reply(messages)
    print_user_max_seen(messages)
    print_time_max_messages(messages)
    print_id_message_long_tread(messages)