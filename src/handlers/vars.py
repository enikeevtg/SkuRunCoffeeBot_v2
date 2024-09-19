# Some variables handlers

# handlers.menu
from decouple import config


order_id = int(config('FIRST_ORDER_ROW'))
# Временная база заказов в текущий день
# {user_id: {
#            'name': 'Тагир',
#            'drink': 'Шиповник'
#           }
# }
orders = {}


# КАТЕГОРИИ И ПОДКАТЕГОРИИ НАПИТКОВ
drink_names = ['Американо', 'Шиповник', 'Фильтр-кофе']
amerincano_options = ['Американо', 'Американо со сливками',
                      'Американо с овсяным молоком']
rosehip_options = ['Шиповник', 'Шиповник с мёдом', 'Шиповник со льдом',
                   'Шиповник с мёдом и льдом']

# amerincano_options = ['Сливки', 'Овсяное молоко 🥛',
#                       'Просто американо, пожалуйста ☕️']
# rosehip_options = ['Лёд 🧊', 'Мёд 🍯', 'Всего и побольше 😋 🧊 🍯',
#                    'Просто шип, пожалуйста']
