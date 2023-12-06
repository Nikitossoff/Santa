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
            @bot.message_handler(commands=["start", "admin"])
            def start(message, res=False):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("santa.db")
                c  = db.cursor()
                if message.text == "/admin":
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
                        bot.delete_message(idtg, message.message_id)
                        try:
                            bot.delete_message(idtg, int(message.message_id)-1,2)
                        except:
                            pass
                    except:
                            pass
                    text.hello(bot, message)
            @bot.message_handler(content_types=['text'])
            def menu(message):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("santa.db")
                c  = db.cursor()
                if message.text == "Выбрать человека!":
                    c.execute("""SELECT idtg FROM users WHERE idtg = ?""", [idtg])
                    users = c.fetchone()
                    if users != None:
                        c.execute("SELECT * FROM users WHERE gift = 0 AND idtg <> ? ORDER BY RANDOM() LIMIT 1", (idtg,))
                        data = c.fetchone()
                        i = 0
                        a = types.ReplyKeyboardRemove()
                        time.sleep(1)
                        processing_message = bot.send_message(message.chat.id, "Обработка....", parse_mode='HTML', reply_markup=a)
                        while True:
                            bot.edit_message_text(chat_id=message.chat.id,message_id=processing_message.message_id,text=f"""
Выполняется генерация...
<b>Процент выполнения - {i}%</b>
                                              """, parse_mode='HTML')
                            i += 10
                            time.sleep(3)
                            if i == 100:
                                break
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJlVWVwiuRPsDWoXc5akbSCgsUKZNJVAAI1EgAChQ6pSYCQPfXpdLT8MwQ')
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Переролл(только один раз)", callback_data=f"Pere")
                        btn2 = types.InlineKeyboardButton(text="Перейти в меню", callback_data=f"lavmenu|{data}")
                        markup.add(btn1,btn2)
                        bot.send_message(idtg, f'''Готово! Бот вам выбрал человека - {data[0]} ''', reply_markup=markup, parse_mode='HTML')
                    else:
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
                        bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                idtg = str(call.message.chat.id)
                db = sqlite3.connect("santa.db")
                c = db.cursor()
                if "lavmenu" in call.data:
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
                if "Dop" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                if "Podr" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass

                if "Udal" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                if "Pere" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    c.execute("""SELECT idtg FROM users WHERE idtg = ?""", [idtg])
                    users = c.fetchone()
                    if users != None:
                        c.execute("SELECT * FROM users WHERE gift = 0 AND idtg <> ?  ORDER BY RANDOM() LIMIT 1", (idtg,))
                        data = c.fetchone()
                        i = 0
                        a = types.ReplyKeyboardRemove()
                        time.sleep(1)
                        processing_message = bot.send_message(call.message.chat.id, "Обработка....", parse_mode='HTML', reply_markup=a)
                        while True:
                            bot.edit_message_text(chat_id=call.message.chat.id,message_id=processing_message.message_id,text=f"""
Выполняется генерация...
<b>Процент выполнения - {i}%</b>
                                              """, parse_mode='HTML')
                            i += 10
                            time.sleep(3)
                            if i == 100:
                                break
                        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJlVWVwiuRPsDWoXc5akbSCgsUKZNJVAAI1EgAChQ6pSYCQPfXpdLT8MwQ')
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Перейти в меню", callback_data=f"lavmenu|{data}")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''Готово! Бот вам выбрал человека - {data[0]} ''', reply_markup=markup, parse_mode='HTML')
                    else:
                        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
                        bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
            bot.infinity_polling()
        else:
            print("Произшла ошибка проверьте код")
main()