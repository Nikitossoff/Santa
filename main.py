# -*- coding: utf-8 -*-
# PS C:\Desktop\programmingNikita\Santa> & C:/Users/Олег/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Desktop/programmingNikita/Santa/main.py
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
def main():
    while True:
        if True:
            bot = telebot.TeleBot('ТОКЕН')
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
                        if Pe != 0:
                            text.menu(bot, message)
                        else:
                            text.hello(bot, message)
            @bot.message_handler(content_types=['text'])
            def menu(message):
                idtg = str(message.from_user.id)
                db = sqlite3.connect("santa.db")
                c  = db.cursor()
                if message.text == "Выбрать человека!":
                    c.execute("""SELECT present FROM users WHERE idtg = ?""", [idtg])
                    try:
                        Pe = c.fetchone()[0]
                    except:
                        Pe = 999
                    if Pe == 999:
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
                        bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
                    else:
                        if Pe != 0:
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn4 = types.InlineKeyboardButton(text="В меню👈", callback_data=f"Main")
                            markup.add(btn4)
                            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
                            bot.send_message(idtg, f'''Вы уже сгенирировали пользователя!''', reply_markup=markup,  parse_mode='HTML')
                        else:
                            text.generation(bot, message=message)
            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                idtg = (call.message.chat.id)
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
                    c.execute("""SELECT * FROM admins WHERE idtg = ?""", [idtg])
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
                        btn3 = types.InlineKeyboardButton(text="Рассылка", callback_data=f"admsend")
                        btn4 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data=f"Main")
                        markup.add(btn1, btn2, btn3, btn4)
                        file = open("img.jpg", "rb")
                        bot.send_photo(idtg, file, f'''
<b>Admin меню</b>
Нагрузка сервера - {psutil.cpu_percent(interval=0.1)}%
Всего пользователей - {users}
                        ''',  reply_markup=markup, parse_mode='HTML')
                    else:
                        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
                        bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
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
                    text.Skibidi(bot,call=call)
                if "QWERT" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    file = open("img.jpg", "rb")
                    bot.send_photo(idtg, file, f'''
Введите в виде Имя Фамилия; Размер одежды; Нелюбимые продукты; IDTG или CANCEL для отмены
                    ''', parse_mode='HTML')
                    bot.register_next_step_handler(call.message, Noviy)
                if "Roy" in call.data:
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
                            btn1 = types.InlineKeyboardButton(text=f"{str(i[0])}", callback_data=f"Lox|{str(i[0])}")
                            markup.add(btn1)
                    except:
                        btn2 = types.InlineKeyboardButton(text=f"Произошла ошибка❌", callback_data=f"text")
                        markup.add(btn2)
                    btn4 = types.InlineKeyboardButton(text="Обратно в меню", callback_data=f"adminm")
                    markup.add(btn4)
                    bot.send_photo(idtg, file, f'''
Выберите человека:
                    ''',  reply_markup=markup, parse_mode='HTML')
                if "Lox" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    x = (call.data.split("|")[1])
                    c.execute("""DELETE FROM users WHERE name = ?""", [x])
                    db.commit()
                    file = open("img.jpg", "rb")
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn4 = types.InlineKeyboardButton(text="Обратно", callback_data=f"Dop")
                    markup.add(btn4)
                    bot.send_photo(idtg, file, f'''
Готово!
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
                    try:
                        data = c.fetchone()[0]
                    except:
                        data = "Нету данных"
                    c.execute("""SELECT cap FROM users WHERE name = ?""", [gift])
                    cap = c.fetchone()[0]
                    file = open("Ojel.png", "rb")
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Обратно в меню", callback_data=f"Main")
                    markup.add(btn1)
                    bot.send_photo(idtg, file, f'''
Не любимые продукты и непереносимости - {data}
Размер - {cap}
                    ''',  reply_markup=markup, parse_mode='HTML')
                if "spam" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                if "admsend" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    bot.send_message(idtg, f'''
Текст или CANCEL для отмены
                    ''',  parse_mode='HTML')
                    bot.register_next_step_handler(call.message, ras)
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
                    text.Izmena(bot,call=call)
                    
                if "Izmenitpresent" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    x = (call.data.split("|")[1])
                    bot.send_message(idtg, f'''
Введите имя в виде: Имя Фамилия или CANCEL для отмены
                    ''',  parse_mode='HTML')
                    bot.register_next_step_handler(call.message, Dangeonmaster, x)
                if "Izmenitimya" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    x = (call.data.split("|")[1])
                    bot.send_message(idtg, f'''
Введите имя в виде: Имя Фамилия или CANCEL для отмены
                    ''',  parse_mode='HTML')
                    bot.register_next_step_handler(call.message, Master, x)
                if "Izmenitproduct" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    x = (call.data.split("|")[1])
                    bot.send_message(idtg, f'''
Введите нелюбимый продукт или CANCEL для отмены
                    ''',  parse_mode='HTML')
                    bot.register_next_step_handler(call.message, Slave, x )
                if "Izmenitpodarok" in call.data:
                    try:
                        try: 
                            bot.delete_message(idtg, call.message.message_id)
                            try:
                                bot.delete_message(idtg, int(call.message.message_id)-1,2)
                            except:
                                pass
                        except:
                            pass
                        x = (call.data.split("|")[1])
                        c.execute("""SELECT present FROM users WHERE name = ?""",[x])
                        gg = c.fetchone()[0]
                        c.execute("""UPDATE users SET gift = ? WHERE name = ?""", [0, gg])
                        c.execute("""UPDATE users SET present = ? WHERE name = ?""", [0, x])
                        c.execute("""UPDATE users SET pererol = ? WHERE name = ?""", [1, x])
                        db.commit()
                        file = open("img.jpg", "rb")
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn4 = types.InlineKeyboardButton(text="Обратно", callback_data=f"adminm")
                        markup.add(btn4)
                        bot.send_photo(idtg, file, f'''
Готово!
                        ''',  reply_markup=markup, parse_mode='HTML')
                    except:
                        file = open("img.jpg", "rb")
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn4 = types.InlineKeyboardButton(text="Обратно", callback_data=f"adminm")
                        markup.add(btn4)
                        bot.send_photo(idtg, file, f'''
Произошла ошибка!
                        ''',  reply_markup=markup, parse_mode='HTML')
                if "Izmenitidtg" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    x = (call.data.split("|")[1])
                    bot.send_message(idtg, f'''
Введите idtg в цифрах или CANCEL для отмены
                    ''',  parse_mode='HTML')
                    bot.register_next_step_handler(call.message, Cam, x)
                if "Izmenitrazmer" in call.data:
                    try: 
                        bot.delete_message(idtg, call.message.message_id)
                        try:
                            bot.delete_message(idtg, int(call.message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass
                    x = (call.data.split("|")[1])
                    bot.send_message(idtg, f'''
Введите размер или CANCEL для отмены
                    ''',  parse_mode='HTML')
                    bot.register_next_step_handler(call.message, Porn, x)
                if "admindb" in call.data:
                    file = open("santa.db", "rb")
                    bot.send_document(call.message.chat.id, file)
                if "Pere" in call.data:
                    c.execute("""SELECT pererol FROM users WHERE idtg = ?""", [idtg])
                    pererol = c.fetchone()[0]
                    if pererol == 1:
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
                            x = (call.data.split("|")[1])
                            c.execute("""UPDATE users SET pererol = ? WHERE idtg = ?""", [0, idtg])
                            c.execute("""UPDATE users SET gift = ? WHERE name = ?""", (0, x,))
                            c.execute("""UPDATE users SET present = ? WHERE idtg = ?""", [0, idtg])
                            db.commit()
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
                            try:
                                while True:
                                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=int(call.message.message_id+2),text=f"""
Генерируем...
<b>Процент выполнения - {i}%</b>""", parse_mode='HTML')
                                    i += 50
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
                            except:
                                markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
                                btn1 = types.KeyboardButton("Выбрать человека!")
                                markup.add(btn1)
                                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJnEWV4Z_Tom3feLp1Id_yCaiPTxwIpAAKREgACEFGoSX_KPekwYirmMwQ')
                                bot.send_message(idtg, f'''Произошла ошибка, попробуйте еще раз!''', reply_markup=markup, parse_mode='HTML')
                            c.execute("""SELECT present FROM users WHERE present <> ? AND idtg <> ?""", [0, idtg])
                            data1 = c.fetchall()
                            names_in_data1 = [row[0] for row in data1]  
                            c.execute("SELECT name FROM users WHERE idtg <> ?", [idtg])
                            data2 = c.fetchall()
                            names_in_data2 = [row[0] for row in data2] 
                            names_array1 = np.array(names_in_data1)
                            names_array2 = np.array(names_in_data2)
                    

                            # Найти имена, которые есть в names_array2, но отсутствуют в names_array1
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
                                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJlqWVzUNOgORUZqe9U3eOwRSSr2cftAAJoEwACvb6wSQLnwBPY3i1VMwQ')
                                markup = types.InlineKeyboardMarkup(row_width = 1)
                                if pererol == 1:
                                    btn1 = types.InlineKeyboardButton(text="Переролл(только один раз)", callback_data=f"Pere|{random_name}")
                                    markup.add(btn1)
                                btn2 = types.InlineKeyboardButton(text="Перейти в меню", callback_data=f"Main|{random_name}")
                                markup.add(btn2)
                                file = open("Gen.png", "rb")
                                bot.send_photo(idtg, file, f'''Готово! Бот вам выбрал человека - {random_name} ''', reply_markup=markup, parse_mode='HTML')
                            else:
                                markup = types.InlineKeyboardMarkup(row_width = 1)
                                btn2 = types.InlineKeyboardButton(text="Перейти в меню", callback_data=f"Main")
                                markup.add(btn2)
                                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJnEWV4Z_Tom3feLp1Id_yCaiPTxwIpAAKREgACEFGoSX_KPekwYirmMwQ')
                                bot.send_message(idtg, f'''Произошла ошибка, попробуйте еще раз! Возможно нет возможных имен!''', reply_markup=markup, parse_mode='HTML')
                        else:
                            bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
                            bot.send_message(idtg, f'''У вас нет доступа''',  parse_mode='HTML')
                    else:
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn2 = types.InlineKeyboardButton(text="Перейти в меню", callback_data=f"Main")
                        markup.add(btn2)
                        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJeRmVd2w70HltyLA65Ck4yDt8UPj1aAALzAAP3AsgPhnmk5pbwEy4zBA')
                        bot.send_message(idtg, f'''Вы уже генирировали человека, перейдите в меню!''', reply_markup=markup, parse_mode='HTML')
            def Noviy(message):
                idtg = str(message.chat.id)
                db = sqlite3.connect("santa.db")
                c = db.cursor()
                if message.text == "CANCEL":
                    text.Skibidi(bot, message=message)
                else:
                    pattern = r".+; .+; .+; .+$"
                    if not re.match(pattern, message.text):
                        try:
                            bot.delete_message(idtg, message.message_id)
                            try:
                                bot.delete_message(idtg, int(message.message_id)-1,2)
                            except:
                                pass
                        except:
                            pass 
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn3 = types.InlineKeyboardButton(text="Сначала👈", callback_data=f"Dop")
                        markup.add(btn3)
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeSmVd3D6b87zzI1ex_FcFGA1_m9LOAALbBQACP5XMCjz4rPnlRa-CMwQ')
                        bot.send_message(message.chat.id, f'''
<u><b>Вы написали неправильный текст, попробуйте еще раз</b></u>                                                                           
                        ''', reply_markup=markup, parse_mode='HTML') 
                    else:
                        try:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            text = message.text
                            parts =  text.split(';')
                            name = parts[0].strip()
                            razmer= parts[1].strip()
                            noise= parts[2].strip()
                            idi= parts[3].strip()
                            file = open("img.jpg", "rb")
                            c.execute(f"INSERT INTO users VALUES (?,?,?,?,?,?,?,?)",(name, idi, 0, 0, noise, 0, 1, razmer))
                            db.commit()
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn3 = types.InlineKeyboardButton(text="Обратно👈", callback_data=f"Dop")
                            markup.add(btn3)
                            bot.send_photo(idtg, file, f'''
Готово!
                            ''',  reply_markup=markup, parse_mode='HTML')
                        except:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn3 = types.InlineKeyboardButton(text="Обратно👈", callback_data=f"Dop")
                            markup.add(btn3)
                            bot.send_photo(idtg, file, f'''
Произошла ошибка!
                            ''',  reply_markup=markup, parse_mode='HTML')
            def ras(message):
                idtg = str(message.chat.id)
                db = sqlite3.connect("santa.db")
                c = db.cursor()
                if message.text == "СANCEL":
                    try:
                        bot.delete_message(idtg, message.message_id)
                        try:
                            bot.delete_message(idtg, int(message.message_id)-1,2)
                        except:
                            pass
                    except:
                        pass 
                    text.admin(bot, message=message)
                else:
                    bot.delete_message(idtg, message.message_id)
                    try:
                        bot.delete_message(idtg, int(message.message_id)-1,2)
                    except:
                        pass
                    c.execute("""SELECT idtg FROM users""")
                    idsh = c.fetchall()
                    count = 0
                    for i in idsh:
                        try:
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn1 = types.InlineKeyboardButton(text=f"Удалить сообщение", callback_data=f"spam")
                            markup.add(btn1)
                            bot.send_message(i[0], f'''
{message.text}
                            ''', reply_markup=markup, parse_mode='HTML')
                            count += 1
                        except:
                            pass
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn3 = types.InlineKeyboardButton(text="Сначала👈", callback_data=f"adminm")
                    markup.add(btn3)
                    bot.send_message(idtg, f'''
Отправленно - {count}
                    ''', reply_markup=markup, parse_mode='HTML')
                    
            def Dangeonmaster(message, x):
                idtg = str(message.chat.id)
                db = sqlite3.connect("santa.db")
                c = db.cursor()
                if message.text == "СANCEL":
                    try:
                        bot.delete_message(idtg, message.message_id)
                        try:
                            bot.delete_message(idtg, int(message.message_id)-1,2)
                        except:
                            pass
                    except:
                            pass 
                    text.admin(bot, message=message)
                else:
                    pattern = r".+ .+$"
                    if not re.match(pattern, message.text):
                        try:
                            bot.delete_message(idtg, message.message_id)
                            try:
                                bot.delete_message(idtg, int(message.message_id)-1,2)
                            except:
                                pass
                        except:
                            pass 
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn3 = types.InlineKeyboardButton(text="Сначала👈", callback_data=f"Udal")
                        markup.add(btn3)
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeSmVd3D6b87zzI1ex_FcFGA1_m9LOAALbBQACP5XMCjz4rPnlRa-CMwQ')
                        bot.send_message(message.chat.id, f'''
<u><b>Вы написали неправильный текст, попробуйте еще раз</b></u>                                                                           
                        ''', reply_markup=markup, parse_mode='HTML') 
                    else:
                        try:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            c.execute("""SELECT name FROM users WHERE idtg = ?""", [idtg])
                            imya = c.fetchone()[0]
                            c.execute("""SELECT present FROM users WHERE name = ?""",[x])
                            gg = c.fetchone()[0]
                            c.execute("""UPDATE users SET gift = ? WHERE name = ?""", [0, gg])
                            c.execute("""UPDATE users SET present = ? WHERE name = ?""", [message.text, x])
                            c.execute("""UPDATE users SET gift = ? WHERE name = ?""", [imya, message.text])
                            db.commit()
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn4 = types.InlineKeyboardButton(text="Обратно", callback_data=f"Udal")
                            markup.add(btn4)
                            bot.send_photo(idtg, file, f'''
Готово!
                            ''',  reply_markup=markup, parse_mode='HTML')
                        except:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn3 = types.InlineKeyboardButton(text="Обратно👈", callback_data=f"Udal")
                            markup.add(btn3)
                            bot.send_photo(idtg, file, f'''
Произошла ошибка!
                            ''',  reply_markup=markup, parse_mode='HTML')
            def Master(message, x):
                idtg = str(message.chat.id)
                db = sqlite3.connect("santa.db")
                c = db.cursor()
                if message.text == "СANCEL":
                    try:
                        bot.delete_message(idtg, message.message_id)
                        try:
                            bot.delete_message(idtg, int(message.message_id)-1,2)
                        except:
                            pass
                    except:
                            pass 
                    text.admin(bot, message=message)
                else:
                    pattern = r".+ .+$"
                    if not re.match(pattern, message.text):
                        try:
                            bot.delete_message(idtg, message.message_id)
                            try:
                                bot.delete_message(idtg, int(message.message_id)-1,2)
                            except:
                                pass
                        except:
                            pass 
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn3 = types.InlineKeyboardButton(text="Сначала👈", callback_data=f"Udal")
                        markup.add(btn3)
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeSmVd3D6b87zzI1ex_FcFGA1_m9LOAALbBQACP5XMCjz4rPnlRa-CMwQ')
                        bot.send_message(message.chat.id, f'''
<u><b>Вы написали неправильный текст, попробуйте еще раз</b></u>                                                                           
                        ''', reply_markup=markup, parse_mode='HTML') 
                    else:
                        try:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            c.execute("""UPDATE users SET name = ? WHERE name = ?""", [message.text, x])
                            db.commit()
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn4 = types.InlineKeyboardButton(text="Обратно", callback_data=f"Udal")
                            markup.add(btn4)
                            bot.send_photo(idtg, file, f'''
Готово!
                            ''',  reply_markup=markup, parse_mode='HTML')
                        except:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn3 = types.InlineKeyboardButton(text="Обратно👈", callback_data=f"Udal")
                            markup.add(btn3)
                            bot.send_photo(idtg, file, f'''
Произошла ошибка!
                            ''',  reply_markup=markup, parse_mode='HTML')
            def Slave(message, x):
                idtg = str(message.chat.id)
                db = sqlite3.connect("santa.db")
                c = db.cursor()
                if message.text == "СANCEL":
                    try:
                        bot.delete_message(idtg, message.message_id)
                        try:
                            bot.delete_message(idtg, int(message.message_id)-1,2)
                        except:
                            pass
                    except:
                            pass 
                    text.admin(bot, message=message)
                else:
                    pattern = r".+$"
                    if not re.match(pattern, message.text):
                        try:
                            bot.delete_message(idtg, message.message_id)
                            try:
                                bot.delete_message(idtg, int(message.message_id)-1,2)
                            except:
                                pass
                        except:
                            pass 
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn3 = types.InlineKeyboardButton(text="Сначала👈", callback_data=f"Udal")
                        markup.add(btn3)
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeSmVd3D6b87zzI1ex_FcFGA1_m9LOAALbBQACP5XMCjz4rPnlRa-CMwQ')
                        bot.send_message(message.chat.id, f'''
<u><b>Вы написали неправильный текст, попробуйте еще раз</b></u>                                                                           
                        ''', reply_markup=markup, parse_mode='HTML') 
                    else:
                        try:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            c.execute("""UPDATE users SET noise = ? WHERE name = ?""", [message.text, x])
                            db.commit()
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn4 = types.InlineKeyboardButton(text="Обратно", callback_data=f"Udal")
                            markup.add(btn4)
                            bot.send_photo(idtg, file, f'''
Готово!
                            ''',  reply_markup=markup, parse_mode='HTML')
                        except:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn3 = types.InlineKeyboardButton(text="Обратно👈", callback_data=f"Udal")
                            markup.add(btn3)
                            bot.send_photo(idtg, file, f'''
Произошла ошибка!
                            ''',  reply_markup=markup, parse_mode='HTML')
            def Cam(message, x):
                idtg = str(message.chat.id)
                db = sqlite3.connect("santa.db")
                c = db.cursor()
                if message.text == "СANCEL":
                    try:
                        bot.delete_message(idtg, message.message_id)
                        try:
                            bot.delete_message(idtg, int(message.message_id)-1,2)
                        except:
                            pass
                    except:
                            pass 
                    text.admin(bot, message=message)
                else:
                    pattern = r"\d+$"
                    if not re.match(pattern, message.text):
                        try:
                            bot.delete_message(idtg, message.message_id)
                            try:
                                bot.delete_message(idtg, int(message.message_id)-1,2)
                            except:
                                pass
                        except:
                            pass 
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn3 = types.InlineKeyboardButton(text="Сначала👈", callback_data=f"Udal")
                        markup.add(btn3)
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeSmVd3D6b87zzI1ex_FcFGA1_m9LOAALbBQACP5XMCjz4rPnlRa-CMwQ')
                        bot.send_message(message.chat.id, f'''
<u><b>Вы написали неправильный текст, попробуйте еще раз</b></u>                                                                           
                        ''', reply_markup=markup, parse_mode='HTML') 
                    else:
                        try:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            c.execute("""UPDATE users SET idtg = ? WHERE name = ?""", [message.text, x])
                            db.commit()
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn4 = types.InlineKeyboardButton(text="Обратно", callback_data=f"Udal")
                            markup.add(btn4)
                            bot.send_photo(idtg, file, f'''
Готово!
                            ''',  reply_markup=markup, parse_mode='HTML')
                        except:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn3 = types.InlineKeyboardButton(text="Обратно👈", callback_data=f"Udal")
                            markup.add(btn3)
                            bot.send_photo(idtg, file, f'''
Произошла ошибка!
                            ''',  reply_markup=markup, parse_mode='HTML')
            def Porn(message, x):
                idtg = str(message.chat.id)
                db = sqlite3.connect("santa.db")
                c = db.cursor()
                if message.text == "СANCEL":
                    try:
                        bot.delete_message(idtg, message.message_id)
                        try:
                            bot.delete_message(idtg, int(message.message_id)-1,2)
                        except:
                            pass
                    except:
                            pass 
                    text.admin(bot, message=message)
                else:
                    pattern = r".+$"
                    if not re.match(pattern, message.text):
                        try:
                            bot.delete_message(idtg, message.message_id)
                            try:
                                bot.delete_message(idtg, int(message.message_id)-1,2)
                            except:
                                pass
                        except:
                            pass 
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn3 = types.InlineKeyboardButton(text="Сначала👈", callback_data=f"Udal")
                        markup.add(btn3)
                        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJeSmVd3D6b87zzI1ex_FcFGA1_m9LOAALbBQACP5XMCjz4rPnlRa-CMwQ')
                        bot.send_message(message.chat.id, f'''
<u><b>Вы написали неправильный текст, попробуйте еще раз</b></u>                                                                           
                        ''', reply_markup=markup, parse_mode='HTML') 
                    else:
                        try:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            c.execute("""UPDATE users SET cap = ? WHERE name = ?""", [message.text, x])
                            db.commit()
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn4 = types.InlineKeyboardButton(text="Обратно", callback_data=f"Udal")
                            markup.add(btn4)
                            bot.send_photo(idtg, file, f'''
Готово!
                            ''',  reply_markup=markup, parse_mode='HTML')
                        except:
                            try:
                                bot.delete_message(idtg, message.message_id)
                                try:
                                    bot.delete_message(idtg, int(message.message_id)-1,2)
                                except:
                                    pass
                            except:
                                pass 
                            file = open("img.jpg", "rb")
                            markup = types.InlineKeyboardMarkup(row_width = 1)
                            btn3 = types.InlineKeyboardButton(text="Обратно👈", callback_data=f"Udal")
                            markup.add(btn3)
                            bot.send_photo(idtg, file, f'''
Произошла ошибка!
                            ''',  reply_markup=markup, parse_mode='HTML')
            bot.infinity_polling()
        else:
            print("Произшла ошибка проверьте код")
main()
