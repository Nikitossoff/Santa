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
def main():
    while True:
        if True:
            bot = telebot.TeleBot('6730404345:AAFDzd2dNczarAiz40S7bXlAMF-qX9QSrp4')
            @bot.message_handler(commands=["start", "room"])
            def start(message, res=False):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("base.db")
                c  = db.cursor()
                if "/room" in message.text:
                    try:
                        bot.delete_message(idtg, message.message_id)
                        try:
                            bot.delete_message(idtg, int(message.message_id)-1,2)
                        except:
                            pass
                    except:
                            pass
                    text.admin(bot, message=message)
                if message.text == "/start":
                    try:
                        bot.delete_message(idtg, message.message_id-1)
                        bot.delete_message(idtg, message.message_id-2)
                        bot.delete_message(idtg, message.message_id-3)
                        bot.delete_message(idtg, message.message_id-4)
                    except: 
                        pass
                    c.execute("""SELECT * FROM users WHERE idtg= ?""", [idtg])
                    if c.fetchone() == None:
                        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                        btn1 = types.KeyboardButton("")
                        markup.add(btn1)
                        file = open("hello.jpg", "rb")
                        c.execute(f"INSERT INTO users VALUES (?,?,?)",(idtg, message.from_user.username, "Не установлено👽"))
                        db.commit()
                        bot.send_sticker(idtg, 'CAACAgIAAxkBAAJlBWVvZFJawM0Ql_mcD7790kwJ4yAUAAICEwACKZNgSSrrCEqnzUAfMwQ')
                        bot.send_photo(idtg, file, f'''
Привет!❄️
Добро пожаловать в игру <u>"Тайный санта"</u>!🎅 
Я бот, который поможет тебе организовать небольшой праздник в предверии Нового Года!🥳 
Ну что давай расскажу как играть в Тайного Санту...🎁
                        ''', parse_mode='HTML')
                        time.sleep(1)
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="В меню👌", callback_data=f"menu")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''
"Тайный Санта" - это игра с анонимным дарением порядков, в которой даритель является также и получателям подарка. 
🎅 > 🎁 > 🎅 > 🎁 > 🎅
Она играеться как в небольшой компании до 5 человек, так и в большом дружном классе!
Но думаю ты разберёшься! Переходи в главное меню😉
                        ''', reply_markup=markup, parse_mode='HTML')
                    else:
                        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                        btn1 = types.KeyboardButton("Найти комнату🔎")
                        btn2 = types.KeyboardButton("Создать комнату🎅")
                        markup.add(btn1, btn2)
                        btn3 = types.KeyboardButton("Мои комнаты👨‍👨‍👦‍👦")
                        markup.add(btn3)
                        bot.send_message(idtg, f'''
Главное Меню❄
                        ''', reply_markup=markup, parse_mode='HTML')
            @bot.message_handler(content_types=['text'])
            def menu(message):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("base.db")
                c  = db.cursor()
                if message.text == "Найти комнату🔎":
                    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                    btn1 = types.KeyboardButton("В меню👈")
                    markup.add(btn1)
                    bot.send_message(idtg, f'''
🔎Введи код приглашения:
                    ''', reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, find)
                if message.text == "Создать комнату🎅":
                    abc = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
                    room = ""
                    for a in range(1, 6):
                        b = abc[random.randint(0, len(abc)-1)]
                        room += b
                    c.execute(f"INSERT INTO rooms VALUES (?,?,?,?)",(room, "Имя не указано😢", "Бюджет не указан😭", idtg))
                    db.commit()
                    c.execute(f'''CREATE TABLE room{room} (
                    idtg    TEXT,
                    name    TEXT,
                    dopname TEXT,
                    present TEXT,
                    give    TEXT
                    );''')
                    db.commit()
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Настроить комнату⚙", callback_data=f"room {room}")
                    btn2 = types.InlineKeyboardButton(text="В меню👈", callback_data=f"menu")
                    markup.add(btn1, btn2)
                    bot.send_message(idtg, f'''
Комната успешно создана!🎄
Смотреть за своими комнатами можно в главном меню
                    ''', reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, find)
            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                idtg = str(call.message.chat.id)
                db = sqlite3.connect("base.db")
                c = db.cursor()
                if "menu" in call.data:
                    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                    btn1 = types.KeyboardButton("Найти комнату🔎")
                    btn2 = types.KeyboardButton("Создать комнату🎅")
                    markup.add(btn1, btn2)
                    btn3 = types.KeyboardButton("Мои комнаты👨‍👨‍👦‍👦")
                    markup.add(btn3)
                    bot.send_message(idtg, f'''
Главное Меню❄
                    ''', reply_markup=markup, parse_mode='HTML')




            def find(message):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("base.db")
                c  = db.cursor()
                if message.text == "В меню👈":
                    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                    btn1 = types.KeyboardButton("Найти комнату🔎")
                    btn2 = types.KeyboardButton("Создать комнату🎅")
                    markup.add(btn1, btn2)
                    btn3 = types.KeyboardButton("Мои комнаты👨‍👨‍👦‍👦")
                    markup.add(btn3)
                    bot.send_message(idtg, f'''
Главное Меню❄
                    ''', reply_markup=markup, parse_mode='HTML')
                else:
                    pass
            bot.infinity_polling()
        else:
            print("Произшла ошибка проверьте код")
main()