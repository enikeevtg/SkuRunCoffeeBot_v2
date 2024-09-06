# Регистрация бегуна при первом входе в бота


from bot import bot
import common as common
import config
import db


@bot.message_handler(commands=['start'])
def start(message):
    db.create_person_table()

    user = db.get_cup_name_from_person_table(message.from_user.id)
    if user:
        bot.send_message(message.chat.id,
                         f'О, а я тебя знаю! Ты - {user} 😄')
        bot.send_message(message.chat.id, config.commans_msg)
    else:
        bot.send_animation(message.chat.id, config.starting_animation)
        bot.send_message(message.chat.id, config.starting_msg)
        bot.register_next_step_handler(message,
                                       common.get_cup_name_from_user,
                                       registration)


def registration(message):
    user_data = get_user_data_from_message(message)
    user = db.Person(*user_data)
    db.insert_user_to_person_table(user)
    bot.send_message(message.chat.id, f'{user_data[4]}, я тебя запомнил 😄')
    bot.send_message(message.chat.id, config.commans_msg)


def get_user_data_from_message(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    cup_name = message.text.strip()
    return (user_id, username, first_name, last_name, cup_name)
