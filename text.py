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
import numpy as np
def hello(bot, message=None, call=None):
    try:
        idtg = str(message.from_user.id)
    except:
        idtg = str(call.message.chat.id)
    try:
        bot.delete_message(idtg, message.message_id)
        bot.delete_message(idtg, int(message.message_id)-1)
        try:
            bot.delete_message(idtg, int(message.message_id)-2)
            try:
                bot.delete_message(idtg, int(message.message_id)-3)
                try:
                    bot.delete_message(idtg, int(message.message_id)-4)
                    try:
                        bot.delete_message(idtg, int(message.message_id)-5)
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать человека!")
    markup.add(btn1)
    file = open("hello.jpg", "rb")
    try:
        bot.send_sticker(idtg, 'CAACAgIAAxkBAAJlBWVvZFJawM0Ql_mcD7790kwJ4yAUAAICEwACKZNgSSrrCEqnzUAfMwQ')
        bot.send_photo(idtg, file, f'''Привет, <u><b>{message.from_user.first_name}</b></u>!❄️
Добро пожаловать в игру <u>"Тайный санта"</u>!🎅 
Я бот, который поможет тебе организовать небольшой праздник в предверии Нового Года!🥳 
Ну что давай расскажу как играть в Тайного Санту...🎁''',reply_markup=markup,parse_mode='HTML')
        bot.send_message(idtg, f'''
        "Тайный Санта" - это игра с анонимным дарением порядков, в которой даритель является также и получателям подарка. 
🎅 > 🎁 > 🎅 > 🎁 > 🎅
Она играеться как в небольшой компании до 5 человек, так и в большом дружном классе!
        ''', reply_markup=markup, parse_mode='HTML')
    except:
        bot.send_sticker(idtg, 'CAACAgIAAxkBAAJlBWVvZFJawM0Ql_mcD7790kwJ4yAUAAICEwACKZNgSSrrCEqnzUAfMwQ')
        bot.send_photo(idtg, file, f'''Привет, <u><b>{message.from_user.first_name}</b></u>!❄️
Добро пожаловать в игру <u>"Тайный санта"</u>!🎅 
Я бот, который поможет тебе организовать небольшой праздник в предверии Нового Года!🥳 
Ну что давай расскажу как играть в Тайного Санту...🎁''',reply_markup=markup,parse_mode='HTML')
        bot.send_message(idtg, f'''
        "Тайный Санта" - это игра с анонимным дарением порядков, в которой даритель является также и получателям подарка. 
🎅 > 🎁 > 🎅 > 🎁 > 🎅
Она играеться как в небольшой компании до 5 человек, так и в большом дружном классе!
        ''', reply_markup=markup, parse_mode='HTML')
def admin(bot, message=None, call=None):
    db = sqlite3.connect("santa.db")
    c  = db.cursor()
    idtg = (message.from_user.id)
    c.execute("""SELECT idtg FROM admins WHERE idtg = ?""", [idtg])
    admins = c.fetchone()
    if admins != None:
        try:
            c.execute("""SELECT rowid FROM users ORDER BY rowid DESC LIMIT 1""")
            users = c.fetchone()[0]
        except:
            users = 0
        try:
           c.execute("""SELECT present FROM users WHERE present = 0""")
           loxi = len(c.fetchall())
        except:
           loxi = 0
        markup = types.InlineKeyboardMarkup(row_width = 1)
        btn1 = types.InlineKeyboardButton(text="Добавить/Удалить пользователя", callback_data=f"Dop")
        btn2 = types.InlineKeyboardButton(text="Изменить данные пользователя", callback_data=f"Udal")
        btn3 = types.InlineKeyboardButton(text="Рассылка", callback_data=f"admsend")
        btn4 = types.InlineKeyboardButton(text="База данных", callback_data=f"admindb")
        btn5 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data=f"Main")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        file = open("img.jpg", "rb")
        bot.send_photo(idtg, file, f'''
<b>Admin меню</b>
Нагрузка сервера - {psutil.cpu_percent(interval=0.1)}%
Всего пользователей - {users}
Пользователей не сделавших прокрут - {loxi}
                        ''',  reply_markup=markup, parse_mode='HTML')
    else:
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
        bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
def menu(bot, message=None, call=None):
    try:
        idtg = str(message.from_user.id)
    except:
        idtg = str(call.message.chat.id)
    try:
        bot.delete_message(idtg, message.message_id)
        bot.delete_message(idtg, int(message.message_id)-1)
        try:
            bot.delete_message(idtg, int(message.message_id)-2)
            try:
                bot.delete_message(idtg, int(message.message_id)-3)
                try:
                    bot.delete_message(idtg, int(message.message_id)-4)
                    try:
                        bot.delete_message(idtg, int(message.message_id)-5)
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass
    db = sqlite3.connect("santa.db")
    c  = db.cursor()
    try:
        c.execute("""SELECT * FROM users""")
        users = len(c.fetchall())
    except:
        users = 0
    try:
        c.execute("""SELECT present FROM users WHERE present = 0""")
        loxi = len(c.fetchall())
    except:
        loxi = 0
    file = open("menu.jpg", "rb")
    c.execute("""SELECT * FROM users WHERE idtg = ?""", [idtg])
    data = c.fetchone()
    c.execute("""SELECT pererol FROM users WHERE idtg = ?""", [idtg])
    pererol = c.fetchone()[0]
    markup = types.InlineKeyboardMarkup(row_width = 1)
    btn1 = types.InlineKeyboardButton(text="Подробности о человеке", callback_data=f"Podr")
    markup.add(btn1)
    if pererol == 1:
        btn2 = types.InlineKeyboardButton(text="Переролл(только один раз)", callback_data=f"Pere|{data[3]}")
        markup.add(btn2)
    bot.send_photo(idtg, file, f'''
    <b>Меню</b>
Человек котрому вы дарите - {data[3]}
Стоимость - {data[2]} (можно и больше)
Нагрузка сервера - {psutil.cpu_percent(interval=0.1)}%
Всего пользователей - {users}
Пользователей не сделавших прокрут - {loxi}
                    ''',  reply_markup=markup, parse_mode='HTML')
def generation(bot, message=None, call=None):
    try:
        idtg = str(message.from_user.id)
    except:
        idtg = str(call.message.chat.id)
    db = sqlite3.connect("santa.db")
    c  = db.cursor()
    try:
        bot.delete_message(idtg, message.message_id)
        bot.delete_message(idtg, int(message.message_id)-1)
        try:
            bot.delete_message(idtg, int(message.message_id)-2)
            try:
                bot.delete_message(idtg, int(message.message_id)-3)
                try:
                    bot.delete_message(idtg, int(message.message_id)-4)
                    try:
                        bot.delete_message(idtg, int(message.message_id)-5)
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass
    c.execute("""SELECT idtg FROM users WHERE idtg = ?""", [idtg])
    users = c.fetchone()
    if users != None:
        i = 0
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, f"""
Обработка...""", parse_mode='HTML', reply_markup=a)
        try:
            bot.delete_message(idtg, message.message_id)
            bot.delete_message(idtg, int(message.message_id)-1)
            try:
                bot.delete_message(idtg, int(message.message_id)-2)
                try:
                    bot.delete_message(idtg, int(message.message_id)-3)
                    try:
                        bot.delete_message(idtg, int(message.message_id)-4)
                        try:
                            bot.delete_message(idtg, int(message.message_id)-5)
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        time.sleep(1)
        bot.send_message(message.chat.id, f"""
Подготовка к генерации...
<b>Процент выполнения - {i}%</b>""", parse_mode='HTML')
        try:
            while True:
                bot.edit_message_text(chat_id=message.chat.id, message_id=int(message.message_id+2),text=f"""
Генерируем...
<b>Процент выполнения - {i}%</b>""", parse_mode='HTML')
                i += 50
                time.sleep(1)
                if i == 100:
                    bot.edit_message_text(chat_id=message.chat.id, message_id=int(message.message_id+2),text=f"""
Генерируем...
<b>Процент выполнения - 100%</b>""", parse_mode='HTML')
                    try:
                        bot.delete_message(idtg, int(message.message_id+2))
                        bot.delete_message(idtg, int(message.message_id)+1)
                    except:
                        pass
                    break
        except:
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn1 = types.KeyboardButton("Выбрать человека!")
            markup.add(btn1)
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJnEWV4Z_Tom3feLp1Id_yCaiPTxwIpAAKREgACEFGoSX_KPekwYirmMwQ')
            bot.send_message(idtg, f'''Произошла ошибка, попробуйте еще раз!''', reply_markup=markup, parse_mode='HTML')
        c.execute("""SELECT present FROM users WHERE present <> ? AND idtg <> ?""", [0, idtg])
        data1 = c.fetchall()
        names_in_data1 = [row[0] for row in data1]  
        c.execute("SELECT name FROM users WHERE idtg <> ?", [idtg])
        data2 = c.fetchall()
        names_in_data2 = [row[0] for row in data2] 
        names_array1 = np.array(names_in_data1)
        names_array2 = np.array(names_in_data2)
        remaining_names = np.setdiff1d(names_array2, names_array1)
        if len(remaining_names) > 0:
            # Выбрать случайное имя из remaining_names

            random_name = np.random.choice(remaining_names)
            c.execute("""SELECT pererol FROM users WHERE idtg = ?""", [idtg])
            pererol = c.fetchone()[0]
            c.execute("""SELECT name FROM users WHERE idtg = ?""", [idtg])
            imya = c.fetchone()[0]
            c.execute("""SELECT * FROM price ORDER BY RANDOM() LIMIT 1""")
            tsena = c.fetchone()[0]
            c.execute("""UPDATE users SET gift = ? WHERE name = ?""", [imya, random_name])
            c.execute(f"""UPDATE users SET price = ?, present = ? WHERE idtg = ?""", [tsena, random_name, idtg])
            db.commit()
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJlqWVzUNOgORUZqe9U3eOwRSSr2cftAAJoEwACvb6wSQLnwBPY3i1VMwQ')
            markup = types.InlineKeyboardMarkup(row_width = 1)
            if pererol == 1:
                btn1 = types.InlineKeyboardButton(text="Переролл(только один раз)", callback_data=f"Pere|{random_name}")
                markup.add(btn1)
            btn2 = types.InlineKeyboardButton(text="Перейти в меню", callback_data=f"Main|{random_name}")
            markup.add(btn2)
            file = open("Gen.png", "rb")
            bot.send_photo(idtg, file, f'''Готово! Бот вам выбрал человека - {random_name} ''', reply_markup=markup, parse_mode='HTML')
        else:
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            btn1 = types.KeyboardButton("Выбрать человека!")
            markup.add(btn1)
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJnEWV4Z_Tom3feLp1Id_yCaiPTxwIpAAKREgACEFGoSX_KPekwYirmMwQ')
            bot.send_message(idtg, f'''Произошла ошибка, попробуйте еще раз! Возможно нет возможных имен!''', reply_markup=markup, parse_mode='HTML')
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
        bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
def Izmena(bot, message=None, call=None):
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
    x = (call.data.split("|")[1])
    c.execute("""SELECT * FROM users WHERE name = ?""", [x])
    users = c.fetchone()
    file = open("img.jpg", "rb")
    markup = types.InlineKeyboardMarkup(row_width = 1)
    btn1 = types.InlineKeyboardButton(text="Изменить Имя", callback_data=f"Izmenitimya|{x}")
    btn2 = types.InlineKeyboardButton(text="Изменить нелюбимый продукт", callback_data=f"Izmenitproduct|{x}")
    btn3 = types.InlineKeyboardButton(text="Удалить чел. кот-й. получит подарок", callback_data=f"Izmenitpodarok|{x}")
    btn4 = types.InlineKeyboardButton(text="Изменить IDTG", callback_data=f"Izmenitidtg|{x}")
    btn5 = types.InlineKeyboardButton(text="Изменить  Размер", callback_data=f"Izmenitrazmer|{x}")
    btn6 = types.InlineKeyboardButton(text="Изменить  present", callback_data=f"Izmenitpresent|{x}")
    btn7 = types.InlineKeyboardButton(text="Обратно ", callback_data=f"Udal")
    markup.add(btn1, btn2, btn3,btn4, btn5, btn6, btn7)
    bot.send_photo(idtg, file, f'''
Имя - {users[0]}
Нелюбимый продукт - {users[4]}
Человек котрому подарит подарок - {users[3]}
Idtg - {users[1]}
Размер - {users[7]}
Выберите что хотите измеить:
    ''',  reply_markup=markup, parse_mode='HTML')
def Skibidi(bot, message=None, call=None):
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
    file = open("img.jpg", "rb")
    markup = types.InlineKeyboardMarkup(row_width = 1)
    btn1 = types.InlineKeyboardButton(text="Добавить пользователя", callback_data=f"QWERT")
    btn2 = types.InlineKeyboardButton(text="Удалить пользователя", callback_data=f"Roy")
    btn3 = types.InlineKeyboardButton(text="Вернуться ", callback_data=f"adminm")
    markup.add(btn1, btn2, btn3)
    bot.send_photo(idtg, file, f'''
Выберите действие
    ''',  reply_markup=markup, parse_mode='HTML')