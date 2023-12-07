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
                    c.execute("""SELECT present FROM users WHERE idtg = ?""", [idtg])
                    try:
                        Pe = c.fetchone()[0]
                    except:
                        Pe = 999
                    if Pe == 999:
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
                        bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
                    else:
                        if Pe == 0:
                            text.hello(bot, message)
                        else:
                            text.menu(bot, message)
                    
            @bot.message_handler(content_types=['text'])
            def menu(message):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("santa.db")
                c  = db.cursor()
                if message.text == "Выбрать человека!":
                    text.generation(bot, message=message)
            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                idtg = str(call.message.chat.id)
                db = sqlite3.connect("santa.db")
                c = db.cursor()
                if "adminm" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    text.admin(bot,call=call)
                if "Main" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    text.menu(bot,call=call)
                if "Dop" in call.data:
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
                    btn1 = types.InlineKeyboardButton(text="Добавить пользователя", callback_data=f"Dop1")
                    btn2 = types.InlineKeyboardButton(text="Удалить пользователя", callback_data=f"Udal1")
                    btn3 = types.InlineKeyboardButton(text="Вернуться ", callback_data=f"adminm")
                    markup.add(btn1, btn2, btn3)
                    bot.send_photo(idtg, file, f'''
Выберите действие
                    ''',  reply_markup=markup, parse_mode='HTML')
                if "Podr" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    c.execute("""SELECT present FROM users WHERE idtg = ?""", [idtg])
                    gift = c.fetchone()[0]
                    c.execute("""SELECT noise FROM users WHERE name = ?""", [gift])
                    data = c.fetchone()[0]
                    file = open("img.jpg", "rb")
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Обратно в меню", callback_data=f"Main")
                    markup.add(btn1)
                    bot.send_photo(idtg, file, f'''
Не любимые продукты и непереносимости - {data}
                    ''',  reply_markup=markup, parse_mode='HTML')
                if "Udal" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    file = open("img.jpg", "rb")
                    c.execute("""SELECT name FROM users""")
                    data = c.fetchall()
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    try:
                        for i in data:
                            btn1 = types.InlineKeyboardButton(text=f"{str(i[0])}", callback_data=f"Chert|{str(i[0])}")
                            markup.add(btn1)
                    except:
                        btn2 = types.InlineKeyboardButton(text=f"Произошла ошибка❌", callback_data=f"text")
                        markup.add(btn2)
                    btn4 = types.InlineKeyboardButton(text="Обратно в меню", callback_data=f"adminm")
                    markup.add(btn4)
                    bot.send_photo(idtg, file, f'''
Выберите человека:
                    ''',  reply_markup=markup, parse_mode='HTML')
                if "Chert" in call.data:
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
                    btn1 = types.InlineKeyboardButton(text="Изменить Имя", callback_data=f"Izmenitimya")
                    btn2 = types.InlineKeyboardButton(text="Изменить нелюбимый продукт", callback_data=f"Izmenitproduct")
                    btn3 = types.InlineKeyboardButton(text="Удалить чел. кот-й. получит подарок", callback_data=f"Izmenitpodarok")
                    btn4 = types.InlineKeyboardButton(text="Обратно ", callback_data=f"Udal")
                    markup.add(btn1, btn2, btn3,btn4)
                    bot.send_photo(idtg, file, f'''
Выберите что хотите измеить:
                    ''',  reply_markup=markup, parse_mode='HTML')
                if "Pere" in call.data:
                    try:
                        bot.delete_message(idtg, call.message.message_id)
                        bot.delete_message(idtg, int(call.message.message_id)-1)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-2)
                            try:
                                bot.delete_message(idtg, int(call.message.message_id)-3)
                                try:
                                    bot.delete_message(idtg, int(call.message.message_id)-4)
                                    try:
                                        bot.delete_message(idtg, int(call.message.message_id)-5)
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
                        bot.send_message(call.message.chat.id, f"""
Обработка...""", parse_mode='HTML', reply_markup=a)
                        try:
                            bot.delete_message(idtg, call.message.message_id)
                            bot.delete_message(idtg, int(call.message.message_id)-1)
                            try:
                                bot.delete_message(idtg, int(call.message.message_id)-2)
                                try:
                                    bot.delete_message(idtg, int(call.message.message_id)-3)
                                    try:
                                        bot.delete_message(idtg, int(call.message.message_id)-4)
                                        try:
                                            bot.delete_message(idtg, int(call.message.message_id)-5)
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
                        bot.send_message(call.message.chat.id, f"""
Подготовка к генерации...
<b>Процент выполнения - {i}%</b>""", parse_mode='HTML')
                        time.sleep(1)
                        while True:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=int(call.message.message_id+2),text=f"""
Генерируем...
<b>Процент выполнения - {i}%</b>""", parse_mode='HTML')
                            i += 20
                            time.sleep(1)
                            if i == 100:
                                bot.edit_message_text(chat_id=call.message.chat.id, message_id=int(call.message.message_id+2),text=f"""
Генерируем...
<b>Процент выполнения - 100%</b>""", parse_mode='HTML')
                                time.sleep(1)
                                try:
                                    bot.delete_message(idtg, int(call.message.message_id+2))
                                    bot.delete_message(idtg, int(call.message.message_id)+1)
                                except:
                                    pass
                                break
                        c.execute("SELECT * FROM users WHERE gift = 0 AND idtg <> ? ORDER BY RANDOM() LIMIT 1", (idtg,))
                        data = c.fetchone()
                        c.execute("""SELECT pererol FROM users WHERE idtg = ?""", [idtg])
                        pererol = c.fetchone()[0]
                        c.execute("""SELECT name FROM users WHERE idtg = ?""", [idtg])
                        imya = c.fetchone()[0]
                        c.execute("""SELECT * FROM price ORDER BY RANDOM() LIMIT 1""")
                        tsena = c.fetchone()[0]
                        c.execute("""UPDATE users SET pererol = ? WHERE idtg = ?""", [0, idtg])
                        c.execute("""UPDATE users SET gift = ? WHERE name = ?""", [imya, data[0]])
                        c.execute(f"""UPDATE users SET price = ?, present = ? WHERE idtg = ?""", [tsena, data[0], idtg])
                        db.commit()
                        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJlVWVwiuRPsDWoXc5akbSCgsUKZNJVAAI1EgAChQ6pSYCQPfXpdLT8MwQ')
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        if pererol == 1:
                            btn1 = types.InlineKeyboardButton(text="Переролл(только один раз)", callback_data="Pere")
                            markup.add(btn1)
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Перейти в меню", callback_data=f"Main|{data[0]}")
                        markup.add(btn1)
                        bot.send_message(idtg, f'''Готово! Бот вам выбрал человека - {data[0]} ''', reply_markup=markup, parse_mode='HTML')
                    else:
                        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
                        bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
            bot.infinity_polling()
        else:
            print("Произшла ошибка проверьте код")
main()