# -*- coding: utf-8 -*-
import telebot
from telebot import types
import random
import sqlite3
import secrets
import string
import psutil
import time
import os
import requests
import text
from datetime import  datetime
import re
def hello(bot, message=None, call=None):
    try:
        idtg = str(message.from_user.id)
    except:
        idtg = str(call.message.chat.id)
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать человека!")
    markup.add(btn1)
    file = open("img.jpg", "rb")
    try:
        bot.send_sticker(idtg, 'CAACAgIAAxkBAAJlBWVvZFJawM0Ql_mcD7790kwJ4yAUAAICEwACKZNgSSrrCEqnzUAfMwQ')
        bot.send_photo(idtg, file, f'''Привет, <u><b>{message.from_user.first_name}</b></u>!\nДобро пожаловать в <u>"Тайного санту"</u>! 🎅 Я бот! И вместе с тобой выберем челоека, которому ,<u>ты</u>, подаришь подарок!🎁''',reply_markup=markup,parse_mode='HTML')
    except:
        bot.send_sticker(idtg, 'CAACAgIAAxkBAAJlBWVvZFJawM0Ql_mcD7790kwJ4yAUAAICEwACKZNgSSrrCEqnzUAfMwQ')
        bot.send_photo(idtg, file, f'''Привет, <u><b>{message.from_user.first_name}</b></u>!\nДобро пожаловать в <u>"Тайного санту"</u>! 🎅 Я бот! И вместе с тобой выберем челоека, которому ,<u>ты</u>, подаришь подарок!🎁''',reply_markup=markup,parse_mode='HTML')
def admin(bot, message=None, call=None):
    try:
        idtg = str(message.from_user.id)
    except:
        idtg = str(call.message.chat.id)
    db = sqlite3.connect("santa.db")
    c  = db.cursor()
    c.execute("""SELECT idtg FROM admins WHERE idtg = ?""", [idtg])
    admins = c.fetchone()
    if admins != None:
        try:
            c.execute("""SELECT rowid FROM users ORDER BY rowid DESC LIMIT 1""")
            users = c.fetchone()[0]
        except:
            users = 0
        markup = types.InlineKeyboardMarkup(row_width = 1)
        btn1 = types.InlineKeyboardButton(text="Добавить/Удалить пользователя", callback_data=f"Dop")
        btn2 = types.InlineKeyboardButton(text="Изменить данные пользователя", callback_data=f"Udal")
        btn3 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data=f"glavmenu")
        markup.add(btn1, btn2, btn3)
        file = open("img.jpg", "rb")
        bot.send_photo(idtg, file, f'''
    <b>Admin меню</b>
    Нагрузка сервера - {psutil.cpu_percent(interval=0.1)}%
    Всего пользователей - {users}
        ''',  reply_markup=markup, parse_mode='HTML')
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
        bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
def menu(bot, message=None, call=None):
    try:
        idtg = str(message.from_user.id)
    except:
        idtg = str(call.message.chat.id)
    db = sqlite3.connect("santa.db")
    c  = db.cursor()
    try:
        c.execute("""SELECT rowid FROM users ORDER BY rowid DESC LIMIT 1""")
        users = c.fetchone()[0]
    except:
        users = 0
    file = open("img.jpg", "rb")
    c.execute("""SELECT * FROM users WHERE idtg = ?""", [idtg])
    data = c.fetchone()
    markup = types.InlineKeyboardMarkup(row_width = 1)
    btn1 = types.InlineKeyboardButton(text="Подробности о человеке", callback_data=f"Podr")
    markup.add(btn1)
    bot.send_photo(idtg, file, f'''
    <b>Меню</b>
    Человек котрому вы дарите - {data[3]}
    Стоимость - {data[2]}
    Нагрузка сервера - {psutil.cpu_percent(interval=0.1)}%
    Всего пользователей - {users}
                    ''',  reply_markup=markup, parse_mode='HTML')
def menu2(bot, message=None, call=None):
    try:
        idtg = str(message.from_user.id)
    except:
        idtg = str(call.message.chat.id)
    db = sqlite3.connect("santa.db")
    c  = db.cursor()
    try: 
        bot.delete_message(idtg, call.message.message_id)
        try:
            bot.delete_message(idtg, int(call.message.message_id)-1,2)
        except:
            pass
    except:
        pass
    try:
        c.execute("""SELECT rowid FROM users ORDER BY rowid DESC LIMIT 1""")
        users = c.fetchone()[0]
    except:
        users = 0
    data = (call.data.split("|")[1])
    c.execute("""SELECT name FROM users WHERE idtg = ?""", [idtg])
    imya = c.fetchone()
    c.execute("""SELECT * FROM price ORDER BY RANDOM() LIMIT 1""")
    tsena = c.fetchone()
    c.execute(f"""UPDATE users SET gift = {imya} WHERE name = ?""",[data[0]])
    c.execute(f"""UPDATE users SET price = {tsena}, SET present = {data[0]} WHERE idtg = ?""", [idtg])
    db.commit()
    markup = types.InlineKeyboardMarkup(row_width = 1)
    btn1 = types.InlineKeyboardButton(text="Подробности о человеке", callback_data=f"Podr")
    markup.add(btn1)
    file = open("img.jpg", "rb")
    bot.send_photo(idtg, file, f'''
    <b>Меню</b>
    Человек котрому вы дарите - {data[0]}
    Стоимость - {tsena}
    Нагрузка сервера - {psutil.cpu_percent(interval=0.1)}%
    Всего пользователей - {users}
    ''',  reply_markup=markup, parse_mode='HTML')