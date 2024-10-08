# Некоторые переменные для обработчиков команд

from decouple import config


# handlers.menu
# Временная база заказов в текущий день
# {user_id: {
#            'name': 'Тагир',
#            'drink': 'Шиповник'
#           }
# }
orders = {}

# handlers.menu
# КАТЕГОРИИ И ПОДКАТЕГОРИИ НАПИТКОВ
drink_names = ['Американо', 'Шиповник', 'Фильтр-кофе']
americano_options = ['Американо', 'Американо с молоком',
                     'Американо со сливками', 'Американо с овсяным молоком']
rosehip_options = ['Шиповник', 'Шиповник с мёдом', 'Шиповник со льдом',
                   'Шиповник с мёдом и льдом']
drink_options = {'Американо': americano_options, 'Шиповник': rosehip_options}

# amerincano_options = ['Сливки', 'Овсяное молоко 🥛',
#                       'Просто американо, пожалуйста ☕️']
# rosehip_options = ['Лёд 🧊', 'Мёд 🍯', 'Всего и побольше 😋 🧊 🍯',
#                    'Просто шип, пожалуйста']
