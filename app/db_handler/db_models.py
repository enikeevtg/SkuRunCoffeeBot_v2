# Функции работы с БД SQLite3

import sqlite3
from db_handler import db_queries
from decouple import config


class Person:
    'Person data model'
    def __init__(
        self,
        user_id,
        username,
        first_name,
        last_name,
        cup_name
    ) -> None:
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.cup_name = cup_name

    def __repr__(self):
        return f'''\
   user_id: {self.user_id}
  username: {self.username}
first_name: {self.first_name}
 last_name: {self.last_name}
  cup_name: {self.cup_name}
'''

    def get_person_data(self) -> tuple:
        return (self.user_id,
                self.username,
                self.first_name,
                self.last_name,
                self.cup_name)


def create_person_table(db_file=config('DB_FILE')):
    with sqlite3.connect(db_file) as conn:
        curs = conn.cursor()
        curs.execute(db_queries.q_create_person_table)


def insert_user_to_person_table(user: Person):
    with sqlite3.connect(config('DB_FILE')) as conn:
        curs = conn.cursor()
        curs.execute(db_queries.q_create_person_table)
        curs.execute(db_queries.q_insert_user_to_person_table,
                     user.get_person_data()
                     )
        conn.commit()


def select_user_from_person_table(user_id: int) -> tuple:
    user = None
    with sqlite3.connect(config('DB_FILE')) as conn:
        curs = conn.cursor()
        curs.execute(db_queries.q_check_user_in_person_table, (user_id,))
        user = curs.fetchall()
    return user[0] if len(user) > 0 else None


def get_cup_name_from_person_table(user_id: int):
    user = select_user_from_person_table(user_id)
    return user[5] if user != None else None


def update_cup_name_in_person_table(user_id: int, cup_name: str):
    with sqlite3.connect(config('DB_FILE')) as conn:
        curs = conn.cursor()
        curs.execute(db_queries.q_update_user_in_person_table,
                     (cup_name,
                      user_id))
        conn.commit()
