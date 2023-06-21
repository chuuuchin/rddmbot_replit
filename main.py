### * Copyright Chuchin Dmitriy Maksimovich - All Rights Reserved
### * Unauthorized copying of any files, via any medium is strictly prohibited
### * Proprietary and confidential
### * Written by Dmitriy Chuchin <chuuchin@yandex.ru>, 18 April 2023
###

import telebot
import random

bot = telebot.TeleBot('5647150747:AAF_-ztxizqAbOBhb3uEtAq9wrj1LefHZT4')


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(
    message.chat.id,
    'Привет, это бета-версия Первобота для московского отделения Движения Первых.'
  )
  bot.send_message(
    message.chat.id,
    'Для начала зарегистрируйтесь - /register. Если вы уже зарегистрированы - войдите - /login. Обучение - /manual. Демо-режим - /demo.'
  )


@bot.message_handler(commands=['register'])
def register(message):
  bot.send_message(
    message.chat.id,
    'Итак, давай тебя зарегистрируем. Для начала определимся с полом. Ты мальчик - /boy - или девочка - /girl - ?'
  )

  @bot.message_handler(commands=['boy'])
  def boy(message):
    bio = bot.send_message(
      message.chat.id,
      'В следующем сообщении напиши о себе и своё имя пользователя (@...). Только пожалуйста, без всяких переносов строк. Ты же не хочешь, чтобы твои данные смешались с другими?\nВот пример: "Дмитрий, м, 14 лет, увелкаюсь программированием, живу в Яндекс.Лицее, @chuuuchin"'
    )
    bot.register_next_step_handler(bio, directionboy)

  def directionboy(message):
    data = message.text
    if '@' not in data:
      bot.send_message(message.chat.id, 'Ты не ввёл своё имя пользователя. Пожалуйста, запусти регистрацию - /register - заново.')
    else:
      file = open('boys_datas.txt', 'a+', encoding='utf-8')
      file.write('\n' + str(data))
      file1 = open('datas.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      list_of = open('list_off.png', 'rb')
      bot.send_photo(message.chat.id, list_of)
      bot.send_message(
        message.chat.id,
        'Теперь определим направление. Выше я отправил список. Ознакомься с ним и выбери то, что тебе по душе:\
      \n1. Образование и знания. Учись и познавай! - /educationdirectionboy\
            \n2. Наука и технологии. Дерзай и открывай! - /sciencedirectionboy\
            \n3. Труд, профессия и своё дело. Найди призвание! - /professiondirectionboy\
            \n4. Культура и искусство. Создавай и вдохновляй! - /culturedirectionboy\
            \n5. Волонтёрство и добровольчество. Благо твори! - /volunteerdirectionboy\
            \n6. Патриотризм и историческая память. Служи отечеству! - /patriotismdirectionboy\
            \n7. Спорт. Достигай и побеждай! - /sportdirectionboy\
            \n8. Здоровый образ жизни. Будь здоров! - /healthyhealthdirectionboy\
            \n9. Медиа и коммуникации. Расскажи о главном! - /mediadirectionboy\
            \n10. Дипломатия и международные отношения. Умей дружить! - /diplomacydirectionboy\
            \n11. Экология и охрана природы. Береги планету! - /ecologydirectionboy\
            \n12. Туризм и путешествия. Открывай страну! - /tourismdirectionboy')

    @bot.message_handler(commands=['educationdirectionboy'])
    def educationdirectionboy(message):
      file1 = open('education_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['sciencedirectionboy'])
    def sciencedirectionboy(message):
      file1 = open('science_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['professiondirectionboy'])
    def professiondirectionboy(message):
      file1 = open('profession_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['culturedirectionboy'])
    def culturedirectionboy(message):
      file1 = open('culture_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['volunteerdirectionboy'])
    def volunteerdirectionboy(message):
      file1 = open('volunteer_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['patriotismdirectionboy'])
    def patriotismdirectionboy(message):
      file1 = open('patriotism_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['sportdirectionboy'])
    def sportdirectionboy(message):
      file1 = open('sport_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['healthyhealthdirectionboy'])
    def healthyhealthdirectionboy(message):
      file1 = open('healthyhealth_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['mediadirectionboy'])
    def mediadirectionboy(message):
      file1 = open('media_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['diplomacydirectionboy'])
    def diplomacydirectionboy(message):
      file1 = open('diplomacy_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['ecologydirectionboy'])
    def ecologydirectionboy(message):
      file1 = open('ecology_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['tourismdirectionboy'])
    def tourismdirectionboy(message):
      file1 = open('tourism_direction_boy.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('boys_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирован! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

  @bot.message_handler(commands=['girl'])
  def girl(message):
    bio = bot.send_message(
      message.chat.id,
      'В следующем сообщении напиши о себе и своё имя пользователя (@...). Только пожалуйста, без всяких переносов строк. Ты же не хочешь, чтобы твои данные смешались с другими?\nВот пример: "Дмитрий, м, 14 лет, увелкаюсь программированием, живу в Яндекс.Лицее, @chuuuchin"'
    )
    bot.register_next_step_handler(bio, directiongirl)

  def directiongirl(message):
    data = message.text
    if '@' not in data:
      bot.send_message(message.chat.id, 'Ты не ввёла своё имя пользователя. Пожалуйста, запусти регистрацию - /register - заново.')
    else:
      file = open('girls_datas.txt', 'a+', encoding='utf-8')
      file.write('\n' + str(data))
      file1 = open('datas.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      list_of = open('list_off.png', 'rb')
      bot.send_photo(message.chat.id, list_of)
      bot.send_message(
        message.chat.id,
        'Теперь определим направление. Выше я отправил список. Ознакомься с ним и выбери то, что тебе по душе:\
      \n1. Образование и знания. Учись и познавай! - /educationdirectiongirl\
            \n2. Наука и технологии. Дерзай и открывай! - /sciencedirectiongirl\
            \n3. Труд, профессия и своё дело. Найди призвание! - /professiondirectiongirl\
            \n4. Культура и искусство. Создавай и вдохновляй! - /culturedirectiongirl\
            \n5. Волонтёрство и добровольчество. Благо твори! - /volunteerdirectiongirl\
            \n6. Патриотризм и историческая память. Служи отечеству! - /patriotismdirectiongirl\
            \n7. Спорт. Достигай и побеждай! - /sportdirectiongirl\
            \n8. Здоровый образ жизни. Будь здоров! - /healthyhealthdirectiongirl\
            \n9. Медиа и коммуникации. Расскажи о главном! - /mediadirectiongirl\
            \n10. Дипломатия и международные отношения. Умей дружить! - /diplomacydirectiongirl\
            \n11. Экология и охрана природы. Береги планету! - /ecologydirectiongirl\
            \n12. Туризм и путешествия. Открывай страну! - /tourismdirectiongirl'
      )

    @bot.message_handler(commands=['educationdirectiongirl'])
    def educationdirectiongirl(message):
      file1 = open('education_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['sciencedirectiongirl'])
    def sciencedirectiongirl(message):
      file1 = open('science_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['professiondirectiongirl'])
    def professiondirectiongirl(message):
      file1 = open('profession_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['culturedirectiongirl'])
    def culturedirectiongirl(message):
      file1 = open('culture_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['volunteerdirectiongirl'])
    def volunteerdirectiongirl(message):
      file1 = open('volunteer_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['patriotismdirectiongirl'])
    def patriotismdirectiongirl(message):
      file1 = open('patriotism_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['sportdirectiongirl'])
    def sportdirectiongirl(message):
      file1 = open('sport_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['healthyhealthdirectiongirl'])
    def healthyhealthdirectiongirl(message):
      file1 = open('healthyhealth_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['mediadirectiongirl'])
    def mediadirectiongirl(message):
      file1 = open('media_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['diplomacydirectiongirl'])
    def diplomacydirectiongirl(message):
      file1 = open('diplomacy_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['ecologydirectiongirl'])
    def ecologydirectiongirl(message):
      file1 = open('ecology_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')

    @bot.message_handler(commands=['tourismdirectiongirl'])
    def tourismdirectiongirl(message):
      file1 = open('tourism_direction_girl.txt', 'a+', encoding='utf-8')
      file1.write('\n' + str(data))
      file2 = open('girls_usernames.txt', 'a+', encoding='utf-8')
      file2.write('\n' + str(message.from_user.username))
      file3 = open('usernames.txt', 'a+', encoding='utf-8')
      file3.write('\n' + str(message.from_user.username))
      bot.send_sticker(
        message.chat.id,
        'CAACAgIAAxkBAAEIe1ZkLuPsUkhjaWJSgktAqOPtcyGeQwACdQADBc7CLbvpsgAB1nSKSy8E'
      )
      bot.send_message(
        message.chat.id,
        'Готово, ты зарегистрирована! Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')


@bot.message_handler(commands=['login'])
def login(message):
  f = open('usernames.txt', 'r')
  line = f.read()
  array = line.split('\n')
  for i in array:
    if message.from_user.username in i:
      bot.send_message(message.chat.id, 'Готово, ты вошёл в бота!')
      bot.send_message(
        message.chat.id, 'Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nИнформация о съездах и т.д. - /meetout\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \
                    \n\nДля открытия этого меню - /menu')
      break
  bot.send_message(
    message.chat.id,
    'Если тебе не выпало сообщение об удачном входе, то ты ещё не зарегистрирован в боте. Выполни /start заново и зарегистрируйся.\nОно выглядит так:\n\nГотово, ты вошёл в бота!'
  )

@bot.message_handler(commands=['manual'])
def manual(message):
  bot.send_message(message.chat.id, 'Тут мы расскажем тебе, как правильно пользоваться ботом.\nГотов? Тогда нажимай /start_manual и поехали!\n\nВернуться в начало - /start.')
@bot.message_handler(commands=['start_manual', 'manual_stage_1'])
def start_manual(message):
  bot.send_message(message.chat.id, 'Привет! Это обучалка первобота, где, как в путешествии, показаны интересные функции этого бота. В первую очередь мы с тобой отправимся на функцию «Новые знакомства».')
  bot.send_message(message.chat.id, 'Продолжить - /manual_stage_2\nВыйти - /start')
@bot.message_handler(commands=['manual_stage_2'])
def manual_stage_2(message):
  bot.send_message(message.chat.id, '«Новые знакомства» - функция, где ты можешь найти себе новых знакомых, хоть это и понятно по названию, не так ли?')
  bot.send_message(message.chat.id, 'Найдено новое знакомство, интересно, кто это? А, так это Администрация Первобота, которая всегда поможет тебе разобраться в баге или в проблеме, связанной с ботом. Состав администрации ты узнаешь в другой функции «Контакты»!')
  bot.send_message(message.chat.id, 'Продолжить - /manual_stage_3\nВернуться назад - /manual_stage_1\nВыйти - /start')
@bot.message_handler(commands=['manual_stage_3'])
def manual_stage_3(message):
  bot.send_message(message.chat.id, 'Приступим к функции «Контакты» - здесь ребята, которые, как и сказано мной ранее, всегда придут тебе на помощь!\
\n- А что делать, если не знаешь, кому именно написать?\
\n- Здесь тебе поможет следующая функция «Обратная связь»\
\n«Обратная связь», пригодится в случаях, если возникает срочный вопрос, но ты не хочешь беспокоить человека в личных сообщениях. Ты можешь отправить Яндекс.Форму со своей проблемой, и те, кто занимаются ботом, тебе ответят!')
  bot.send_message(message.chat.id, 'Продолжить - /manual_stage_4\nВернуться назад - /manual_stage_2\nВыйти - /start')
@bot.message_handler(commands=['manual_stage_4'])
def manual_stage_4(message):
  bot.send_message(message.chat.id, 'И так, в меню мы дошли до следующей функции - функции изменения данных аккаунта. Как понятно по названию, она изменяет данные в акаунте, но у тебя нет аккаунта! Надо его создать, а это значит, что мы подошли к концу, и мы должны прощаться, но для начала твоей жизни в боте ты должен посмотреть видео (https://vk.com/wall-220973423_1) или текст (https://t.me/firstsmovementnews/19) в наших социальных сетях!\n\nВернуться назад - /manual_stage_3\nВыйти - /start')

@bot.message_handler(commands=['demo', 'menu_demo'])
def demo(message):
  bot.send_message(message.chat.id, 'Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends_demo\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq_demo\
                    \nСсылки - /links_demo\
                    \nКонтакты - /contacts_demo\
                    \n\nДля открытия этого меню - /menu_demo\
                    \nДля выхода из демо-режима - /start')
@bot.message_handler(commands=['newfriends_demo'])
def newfriends_demo(message):
  bot.send_message(message.chat.id, 'Найдено новое знакомство - Дмитрий, м, 14 лет, увлекаюсь программированием, живу в Яндекс.Лицее, @chuuuchin\nЧтобы увидеть другие знакомства, зарегистрируйся!\n\nДля возврата в меню - /menu_demo')

@bot.message_handler(commands=['faq_demo'])
def faq_demo(message):
  bot.send_message(
    message.chat.id,
    '1. В: Что делать, если у меня неполадки с ботом?\nО: Писать менеджерам, вот их контакты: @wisac, @rrrrrrega, @nyusha_tsukiri.\
  \n\n2. В: Где можно посмотреть новые проекты Движения?\nО: Новые проекты Движения можно посмотреть тут: будьвдвижении.рф.\
  \n\n3. В: Как искать новых друзей?\nО: Найти друзей можно через команду /new_friends. Там ты сможешь выбрать, как именно искать друзей: анонимно, по полу или по интересам.\
  \n\n4. В: Как поменять информацию о себе?\nО: Для этого вызови функцию /edit_data и выбери, что именно ты хочешь поменять.\
                    \n\nДля возврата в меню - /menu_demo')

@bot.message_handler(commands=['links_demo'])
def links_demo(message):
  bot.send_message(
    message.chat.id, 'Основной чат "РДДМ Москва" - https://t.me/rddm_moscow\
                    \nОфициальный канал "Движения Первых" - https://t.me/rddm_official\
                    \nОфициальное сообщество ВК - https://vk.com/rddm_official\
                    \nПравила чата - https://t.me/rddm_moscow/59286\
                    \nВступить в Движение - https://будьвдвижении.рф/\
                    \n\nДля возврата в меню - /menu_demo')

@bot.message_handler(commands=['contacts_demo'])
def contacts_demo(message):
  bot.send_message(message.chat.id, 'Тут контакты тех, к кому ты можешь обратиться по любому вопросу, они всегда помогут!\
                    \n\nАнастасия Аксенова - комьюнити-менеджер сообщества - @hey_nastyaaa\
                    \nАнастасия Елецкая - старший комьюнити-менеджер - @EletskayaN\
                    \nСевда Миралиева - координатор акселератора - @s_miralieva\
                    \n\nКоманда Хранителей атмосферы чата:\
                    \nМатвей - @MtBb11\
                    \nСоня - @sonysska\
                    \nVioletta - @Violettzzz\
                    \nАрсений - @chelovek0125\
                    \nМария - @majezepr\
                    \nИрада - @just_iradochka\
                    \nНадежда - @Googbeste\
                    \nАриша - @rinvilo\
                    \n\nИ, конечно же, команда разработчиков бота:\
                    \nДима - разработчик бота - @chuuuchin\
                    \nВика - старший администратор - @wisac\
                    \nРегина - менеджер - @rrrrrrega\
                    \nМатвей - @MtBb11\
                    \n\
                    \n\nДля возврата в меню - /menu_demo')

@bot.message_handler(commands=['newfriends'])
def newfriends(message):
  bot.send_message(
    message.chat.id,
    'Как будем искать?\nРандомно - /randomnewfriends\nПо интересам - /interestsnewfriends\nАнонимно - /anonymousnewfriends\
                    \n\nДля возврата в меню - /menu')

  @bot.message_handler(commands=['randomnewfriends'])
  def randomnewfriends(message):
    bot.send_message(
      message.chat.id,
      'Кого будем искать - мальчика (/findboy) или девочку (/findgirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['findboy'])
    def findboy(message):
      file = open('boys_datas.txt', 'r')
      line = file.read()
      array = line.split('\n')
      temp = random.randint(0, len(array) - 1)
      bot.send_message(message.chat.id, array[temp])
      bot.send_message(message.chat.id, 'Можешь повторить поиск: /findboy')
      bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['findgirl'])
    def findgirl(message):
      file = open('girls_datas.txt', 'r')
      line = file.read()
      array = line.split('\n')
      temp = random.randint(0, len(array) - 1)
      bot.send_message(message.chat.id, array[temp])
      bot.send_message(message.chat.id, 'Можешь повторить поиск: /findgirl')
      bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

  @bot.message_handler(commands=['interestsnewfriends'])
  def interestsnewfriends(message):
    bot.send_message(
      message.chat.id, 'Выбери интерес, по которому будем искать:\
                          \nСписок направлений/интересов Движения:\
          \n1. Образование и знания. Учись и познавай! - /education\
          \n2. Наука и технологии. Дерзай и открывай! - /science\
          \n3. Труд, профессия и своё дело. Найди призвание! - /profession\
          \n4. Культура и искусство. Создавай и вдохновляй! - /culture\
          \n5. Волонтёрство и добровольчество. Благо твори! - /volunteer\
          \n6. Патриотризм и историческая память. Служи отечеству! - /patriotism\
          \n7. Спорт. Достигай и побеждай! - /sport\
          \n8. Здоровый образ жизни. Будь здоров! - /healthyhealth\
          \n9. Медиа и коммуникации. Расскажи о главном! - /media\
          \n10. Дипломатия и международные отношения. Умей дружить! - /diplomacy\
          \n11. Экология и охрана природы. Береги планету! - /ecology\
          \n12. Туризм и путешествия. Открывай страну! - /tourism')

    @bot.message_handler(commands=['education'])
    def education(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findeducationboy) или девочку (/findeducationgirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findeducationboy'])
      def findeducationboy(message):
        file = open('education_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findeducationboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findeducationgirl'])
      def findeducationgirl(message):
        file = open('education_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findeducationgirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['science'])
    def science(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findscienceboy) или девочку (/findsciencegirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findscienceboy'])
      def findscienceboy(message):
        file = open('science_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findscienceboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findsciencgirl'])
      def findsciencegirl(message):
        file = open('science_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findsciencegirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['profession'])
    def profession(messgae):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findprofessionboy) или девочку (/findprofessiongirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findprofessionboy'])
      def findprofessionboy(message):
        file = open('profession_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findprofessionboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findprofessiongirl'])
      def findprofessiongirl(message):
        file = open('profession_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findprofessiongirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['culture'])
    def culture(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findcultureboy) или девочку (/findculturegirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findcultureboy'])
      def findcultureboy(message):
        file = open('culture_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findcultureboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findculturegirl'])
      def findculturegirl(message):
        file = open('culture_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findculturegirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['volunteer'])
    def volunteer(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findvolunteerboy) или девочку (/findvolunteergirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findvolunteerboy'])
      def findvolunteerboy(message):
        file = open('volunteer_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findvolunteerboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findvolunteergirl'])
      def findvolunteergirl(message):
        file = open('volunteer_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findvolunteergirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['patriotism'])
    def patriotism(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findpatriotismboy) или девочку (/findpatriotismgirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findpatriotismboy'])
      def findpatriotismboy(message):
        file = open('patriotism_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findpatriotismboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findpatriotismgirl'])
      def findpatriotimgirl(message):
        file = open('patriotism_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findpatriotismgirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['sport'])
    def sport(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findsportboy) или девочку (/findsportgirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findsportboy'])
      def findsportboy(message):
        file = open('sport_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findsportboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findsportgirl'])
      def findsportgirl(message):
        file = open('sport_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findsportgirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['healthyhealth'])
    def healthyhealth(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findhealthyhealthboy) или девочку (/findhealthyhealthgirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findhealthyhealthboy'])
      def findhealthyhealthboy(message):
        file = open('healthyhealth_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findhealthyhealthboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findhealthyhealthgirl'])
      def findhealthyhealthgirl(message):
        file = open('healthyhealth_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findhealthyhealthgirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['media'])
    def media(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findmediaboy) или девочку (/findmediagirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findmediaboy'])
      def findmediaboy(message):
        file = open('media_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findmediaboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findmediagirl'])
      def findmediagirl(message):
        file = open('media_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findmediagirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['diplomacy'])
    def diplomacy(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/finddiplomacyboy) или девочку (/finddiplomacygirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['finddiplomacyboy'])
      def finddiplomacyboy(message):
        file = open('diplomacy_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /finddiplomacyboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['finddiplomacygirl'])
      def finddiplomacygirl(message):
        file = open('diplomacy_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /finddiplomacygirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['ecology'])
    def ecology(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findecologyboy) или девочку (/findecologygirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findecologyboy'])
      def findecologyboy(message):
        file = open('ecology_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findecologyboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findecologygirl'])
      def findecologygirl(message):
        file = open('ecology_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findecologygirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

    @bot.message_handler(commands=['tourism'])
    def tourism(message):
      bot.send_message(
        message.chat.id,
        'Кого будем искать - мальчика (/findtourismboy) или девочку (/findtourismgirl)?\
                    \n\nДля возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findtourismboy'])
      def findtourismboy(message):
        file = open('tourism_direction_boy.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findtourismboy')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

      @bot.message_handler(commands=['findtourismgirl'])
      def findtourismgirl(message):
        file = open('tourism_direction_girl.txt', 'r')
        line = file.read()
        array = line.split('\n')
        temp = random.randint(0, len(array) - 1)
        bot.send_message(message.chat.id, array[temp])
        bot.send_message(message.chat.id,
                         'Можешь повторить поиск: /findtourismgirl')
        bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')

  @bot.message_handler(commands=['anonymousnewfriends'])
  def anonymousnewfriends(message):
    f = open('usernames.txt', 'r')
    line = f.read()
    array = line.split('\n')
    temp = random.randint(0, len(array) - 1)
    bot.send_message(message.chat.id,
                     'Вот ссылка на него/неё: ' + '@' + array[temp])
    bot.send_message(message.chat.id, 'Для возврата в меню - /menu - или в меню знакомств - /newfriends')



@bot.message_handler(commands=['faq'])
def faq(message):
  bot.send_message(
    message.chat.id,
    '1. В: Что делать, если у меня неполадки с ботом?\nО: Писать менеджерам, вот их контакты: @wisac, @rrrrrrega, @nyusha_tsukiri.\
  \n\n2. В: Где можно посмотреть новые проекты Движения?\nО: Новые проекты Движения можно посмотреть тут: будьвдвижении.рф.\
  \n\n3. В: Как искать новых друзей?\nО: Найти друзей можно через команду /new_friends. Там ты сможешь выбрать, как именно искать друзей: анонимно, по полу или по интересам.\
  \n\n4. В: Как поменять информацию о себе?\nО: Для этого вызови функцию /edit_data и выбери, что именно ты хочешь поменять.\
                    \n\nДля возврата в меню - /menu')


@bot.message_handler(commands=['createfq'])
def createfq(message):
  newfq = bot.send_message(
    message.chat.id,
    'В следующем сообщении отправь вопрос, который должен появиться в списке, и ответ на него.\nДля возврата в меню - /menu'
  )
  bot.register_next_step_handler(newfq, createfq1)


def createfq1(message):
  data = message.text
  if data.startswith('/'):
    bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
  else:
    file = open('new_fqs.txt', 'a+', encoding='utf-8')
    file.write('\n' + str(data))
    bot.send_message(message.chat.id,
                     'Готово! Скоро твой вопрос появится в списке!')


@bot.message_handler(commands=['info'])
def info(message):
  bot.send_message(
    message.chat.id,
    'Проект бота был создан 7 марта 2023 года Чучиным Д. М. и Богдановым М. Ю. в качестве чат-бота для связи всего Движения.\n\n© Чучин Д. М., Богданов М. Ю., 2023'
  )


@bot.message_handler(commands=['links'])
def links(message):
  bot.send_message(
    message.chat.id, 'Основной чат "РДДМ Москва" - https://t.me/rddm_moscow\
                    \nОфициальный канал "Движения Первых" - https://t.me/rddm_official\
                    \nОфициальное сообщество ВК - https://vk.com/rddm_official\
                    \nПравила чата - https://t.me/rddm_moscow/59286\
                    \nВступить в Движение - https://будьвдвижении.рф/\
                    \n\nДля возврата в меню - /menu')


@bot.message_handler(commands=['feedback'])
def feedback(message):
  bot.send_message(
    message.chat.id,
    'Переходи по ссылке и оставляй обратную связь - https://forms.yandex.ru/u/641dd640eb61460571ab62a2/\
                    \n\nДля возврата в меню - /menu')


@bot.message_handler(commands=['menu'])
def menu(message):
  bot.send_message(
    message.chat.id, 'Выбирай, куда отправимся:\
                    \nНовые знакомства - /newfriends\
                    \nЧаВО (Частые Вопросы и Ответы) - /faq\
                    \nСсылки - /links\
                    \nОбратная связь - /feedback\
                    \nКонтакты - /contacts\
                    \nИзменение данных о себе - /edit_data\
                    \nБольше команд в боковом меню!\
                    \n\nДля открытия этого меню - /menu')


@bot.message_handler(commands=['contacts'])
def contacts(message):
  bot.send_message(message.chat.id, 'Тут контакты тех, к кому ты можешь обратиться по любому вопросу, они всегда помогут!\
                    \n\nАнастасия Аксенова - комьюнити-менеджер сообщества - @hey_nastyaaa\
                    \nАнастасия Елецкая - старший комьюнити-менеджер - @EletskayaN\
                    \nСевда Миралиева - координатор акселератора - @s_miralieva\
                    \n\nКоманда Хранителей атмосферы чата:\
                    \nМатвей - @MtBb11\
                    \nСоня - @sonysska\
                    \nVioletta - @Violettzzz\
                    \nАрсений - @chelovek0125\
                    \nМария - @majezepr\
                    \nИрада - @just_iradochka\
                    \nНадежда - @Googbeste\
                    \nАриша - @rinvilo\
                    \n\nИ, конечно же, команда разработчиков бота:\
                    \nДима - разработчик бота - @chuuuchin\
                    \nВика - старший администратор - @wisac\
                    \nРегина - менеджер - @rrrrrrega\
                    \nМатвей - @MtBb11\
                    \n\
                    \n\nДля возврата в меню - /menu')

@bot.message_handler(commands=['donate'])
def donate(message):
  bot.send_message(
    message.chat.id, 'Топ донатеров - /topdonations\
                    \nЗадонатить, если хочешь - /senddonation\
                    \n\nДля возврата в меню - /menu')

  @bot.message_handler(commands=['topdonations'])
  def topdonations(message):
    bot.send_message(
      message.chat.id, 'Тут будет топ донатов.\
                      \n\nДля возврата в меню - /menu')

  @bot.message_handler(commands=['senddonation'])
  def senddonation(message):
    bot.send_message(
      message.chat.id,
      'Если хочешь поблагодарить разработчиков за работу, можешь отправить любую сумму по этому номеру - 2200700767044562 - мы будем очень рады!\
                      \n\nДля возврата в меню - /menu')


@bot.message_handler(commands=['edit_data'])
def edit_data(message):
  bot.send_message(
    message.chat.id, 'Выбери, что ты хочешь изменить:\
                    \nИзменить имя пользователя (@...) - /edit_nickname\
                    \nИзменить имя - /edit_name\
                    \nИзменить данные о себе - /edit_about\
                    \n\nДля возврата в меню - /menu')

  @bot.message_handler(commands=['edit_nickname'])
  def edit_nickname(message):
    new_nickname = bot.send_message(
      message.chat.id,
      'Для начала введи своё старое имя пользователя, а потом через пробел - новое.'
    )
    bot.register_next_step_handler(new_nickname, edit_nickname1)

  def edit_nickname1(message):
    data = message.text
    if data.startswith('/'):
      bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
    else:
      file = open('edit_nickname.txt', 'a+', encoding='utf-8')
      file.write('\n' + str(data))
      bot.send_message(
        message.chat.id,
        'Готово, после недолгой модерации твоё имя пользователя поменяется!\
                        \n\nДля возврата в меню - /menu')

  @bot.message_handler(commands=['edit_name'])
  def edit_name(message):
    new_name = bot.send_message(
      message.chat.id,
      'Для начала введи своё имя пользователя, а потом через пробел - новое имя.'
    )
    bot.register_next_step_handler(new_name, edit_name1)

  def edit_name1(message):
    data = message.text
    if data.startswith('/'):
      bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
    else:
      file = open('edit_name.txt', 'a+', encoding='utf-8')
      file.write('\n' + str(data))
      bot.send_message(
        message.chat.id, 'Готово, после недолгой модерации твоё имя поменяется!\
                        \n\nДля возврата в меню - /menu')

  @bot.message_handler(commands=['edit_about'])
  def edit_about(message):
    new_about = bot.send_message(
      message.chat.id,
      'Для начала введи своё старое имя пользователя, а потом через пробел - новые данные.'
    )
    bot.register_next_step_handler(new_about, edit_about1)

  def edit_about1(message):
    data = message.text
    if data.startswith('/'):
      bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
    else:
      file = open('edit_about.txt', 'a+', encoding='utf-8')
      file.write('\n' + str(data))
      bot.send_message(
        message.chat.id,
        'Готово, после недолгой модерации данные о тебе поменяются!\
                        \n\nДля возврата в меню - /menu')

  @bot.message_handler(commands=['edit_direction'])
  def edit_direction(message):
    new_direction = bot.send_message(
      message.chat.id,
      'Для начала введи своё имя пользователя, а потом - новое/новые направления.'
    )
    bot.register_next_step_handler(new_direction, edit_direction1)

  def edit_direction1(message):
    data = message.text
    if data.startswith('/'):
      bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
    else:
      file = open('edit_direction.txt', 'a+', encoding='utf-8')
      file.write('\n' + str(data))
      bot.send_message(
        message.chat.id,
        'Готово, после недолгой модерации твои направления поменяются!\
                        \n\nДля возврата в меню - /menu')


@bot.message_handler(commands=['create_extra_profile'])
def create_extra_profile(message):
  data = bot.send_message(
    message.chat.id,
    'Так как профиль расширенный, все данные в нём будут проверяться, это может занять некоторое время. В следующем сообщении отправь любую информацию, которые ты хотел бы видеть в своём профиле.\nКак пример: район Лефортово, школа Содружество, 8 класс.\nДля возврата в меню - /menu'
  )
  bot.register_next_step_handler(data, create_extra_profile1)


def create_extra_profile1(message):
  data = message.text
  if data.startswith('/'):
    bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
  else:
    file = open('extra_profiles.txt', 'a+', encoding='utf-8')
    file.write('\n' + str(data))
    bot.send_message(
      message.chat.id,
      'Круто! Скоро твой профиль обновится! Если появятся какие-то вопросы, мы тебе напишем.'
    )
    bot.send_message(6220998434, data)


@bot.message_handler(commands=['ads'])
def ads(message):
  bot.send_message(
    message.chat.id,
    'Хочешь прорекламировать свой проект в нашем боте? Заполни эту форму - https://forms.yandex.ru/u/641dd78dc769f1054d12d502/ - или нажми сюда - /createadsrequest - мы с тобой свяжемся)\
                     \n\nДля возврата в меню - /menu')


@bot.message_handler(commands=['show_profile'])
def show_profile(message):
  username = message.from_user.username
  temp = ''
  f = open('datas.txt', 'r')
  line = f.read()
  array = line.split('\n')
  for i in array:
    if username in i:
      temp = i
  bot.send_message(message.chat.id, temp)


@bot.message_handler(commands=['createadsrequest'])
def createadsrequest(message):
  name = bot.send_message(
    message.chat.id,
    'Для начала следующим сообщением отправь своё имя.\nДля возврата в меню - /menu'
  )
  bot.register_next_step_handler(name, createadsrequest2)


def createadsrequest2(message):
  data = message.text
  if data.startswith('/'):
    bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
  else:
    file = open('ads_requests.txt', 'a+', encoding='utf-8')
    file.write('\n' + str(data))
    username = bot.send_message(
      messgae.chat.id,
      'Теперь отправь своё имя пользователя в ТГ (@...)\nДля возврата в меню - /menu'
    )
    bot.register_next_step_handler(username, createadsrequest)


def createadsrequest3(message):
  data = message.text
  if data.startswith('/'):
    bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
  else:
    file = open('ads_request.txt', 'a+', encoding='utf-8')
    file.write('\n' + str(data))
    thought = bot.send_message(
      message.chat.id,
      'В следующем сообщении опиши свой проект - напиши название, суть и т.д.\nДля возврата в меню - /menu'
    )
    bot.register_next_step_handler(thought, createadsrequest4)


def createadsrequest4(message):
  data = message.text
  if data.startswith('/'):
    bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
  else:
    file = open('ads_requests.txt', 'a+', encoding='utf-8')
    file.write('\n' + str(data))
    username = bot.send_message(
      message.chat.id,
      'Отлично! Скоро с тобой свяжется один из наших менеджеров!\nДля возврата в меню - /menu'
    )


@bot.message_handler(commands=['createbugreport'])
def createbugreport(message):
  name = bot.send_message(
    message.chat.id,
    'Для начала следующим сообщением отправь своё имя.\nДля возврата в меню - /menu'
  )
  bot.register_next_step_handler(name, createbugreport2)


def createbugreport2(message):
  data = message.text
  if data.startswith('/'):
    bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
  else:
    file = open('bug_reports.txt', 'a+', encoding='utf-8')
    file.write('\n' + str(data))
    username = bot.send_message(
      message.chat.id,
      'Теперь отправь своё имя пользователя в ТГ (@...)\nДля возврата в меню - /menu'
    )
    bot.register_next_step_handler(username, createbugreport3)


def createbugreport3(message):
  data = message.text
  if data.startswith('/'):
    bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
  else:
    file = open('bug_reports.txt', 'a+', encoding='utf-8')
    file.write('\n' + str(data))
    bug = bot.send_message(
      message.chat.id,
      'В следующем сообщении опиши ошибку.\nДля возврата в меню - /menu')
    bot.register_next_step_handler(bug, createbugreport4)


def createbugreport4(message):
  data = message.text
  if data.startswith('/'):
    bot.send_message(message.chat.id, 'Это команда, а не текст. Или запусти исходную команду, или новую.')
  else:
    file = open('bug_reports.txt', 'a+', encoding='utf-8')
    file.write('\n' + str(data))
    bot.send_message(
      message.chat.id,
      'Отлично! Скоро с тобой свяжется один из наших менеджеров!\nДля возврата в меню - /menu'
    )


@bot.message_handler(commands=['all_admin_panel'])
def all_admin_panel(message):
  bot.send_message(
    message.chat.id, 'Выбери один из пунктов:\
                      \n\nПосмотреть новые идеи, отправленные в бота: /passwordhidebotideas\
                      \nПосмотреть форму обратной связи: /passwordhidefeedbackform\
                      \nПосмотреть заявки на рекламу: /passwordhideadsrequests\
                      \nПосмотреть отчёты об ошибках - /passwordhidebugreports\
                      \nПосмотреть кол-во пользователей (за всё время) - /passwordhideuserscol\
                      \nПосмотреть новые вопросы и ответы - /passwordhidenewfqs\
                      \nБудут добавляться новые функции...')


@bot.message_handler(commands=['passwordhidenewfqs'])
def passwordhidenewfqs(message):
  password = bot.send_message(message.chat.id,
                              'Введи пароль для доступа к этой функции.')
  bot.register_next_step_handler(password, hidenewfqs)

  def hidebotideas(message):
    data = message.text
    if data == 'tooroot':
      f = open('new_fqs.txt', 'r')
      bot.send_document(message.chat.id, f)


@bot.message_handler(commands=['passwordhidebotideas'])
def passwordhidebotideas(message):
  password = bot.send_message(message.chat.id,
                              'Введи пароль для доступа к этой функции.')
  bot.register_next_step_handler(password, hidebotideas)


def hidebotideas(message):
  data = message.text
  if data == 'tooroot':
    bot.send_message(message.chat.id, 'coming soon...')


@bot.message_handler(commands=['passwordhidefeedbackform'])
def passwordhidefeedbackform(message):
  password = bot.send_message(message.chat.id,
                              'Введи пароль для доступа к этой функции.')
  bot.register_next_step_handler(password, hidefeedbackform)


def hidefeedbackform(message):
  data = message.text
  if data == 'tooroot':
    bot.send_message(message.chat.id, 'coming soon...')


@bot.message_handler(commands=['passwordhideadsrequests'])
def passwordhideadsrequests(message):
  password = bot.send_message(message.chat.id,
                              'Введи пароль для доступа к этой функции.')
  bot.register_next_step_handler(password, hideadsrequests)


def hideadsrequests(message):
  data = message.text
  if data == 'tooroot':
    ads_requests = open('ads_requests.txt', 'rb')
    bot.send_document(message.chat.id, ads_requests)


@bot.message_handler(commands=['passwordhidebugreports'])
def passwordhidebugreports(message):
  password = bot.send_message(message.chat.id,
                              'Введи пароль для доступа к этой функции.')
  bot.register_next_step_handler(password, hidebugreports)


def hidebugreports(message):
  data = message.text
  if data == 'tooroot':
    bug_reports = open('bug_reports.txt', 'rb')
    bot.send_document(message.chat.id, bug_reports)


@bot.message_handler(commands=['manager_admin_panel'])
def manager_admin_panel(message):
  bot.send_message(
    message.chat.id, 'Выбери один из пунктов:\
                    \nПосмотреть заявки на рекламу: /passwordhideadsrequests\
                      \nПосмотреть отчёты об ошибках - /passwordhidebugreports\
                    \nБудут добавляться новые функции...')


@bot.message_handler(commands=['passwordhideadsrequests'])
def passwordhideadsrequests(message):
  password = bot.send_message(message.chat.id,
                              'Введи пароль для доступа к этой функции.')
  bot.register_next_step_handler(password, hideadsrequests)


def hideadsrequests(message):
  data = message.text
  if data == 'manageroot':
    ads_requests = open('ads_requests.txt', 'rb')
    bot.send_document(message.chat.id, ads_requests)


@bot.message_handler(commands=['passwordhidebugreports'])
def passwordhidebugreports(message):
  password = bot.send_message(message.chat.id,
                              'Введи пароль для доступа к этой функции.')
  bot.register_next_step_handler(password, hidebugreports)


def hidebugreports(message):
  data = message.text
  if data == 'manageroot':
    bug_reports = open('bug_reports.txt', 'rb')
    bot.send_document(message.chat.id, bug_reports)


@bot.message_handler(commands=['passwordhidenewfqs'])
def passwordhidenewfqs(message):
  password = bot.send_message(message.chat.id,
                              'Введи пароль для доступа к этой функции.')
  bot.register_next_step_handler(password, hidenewfqs)


def hidenewfqs(message):
  data = message.text
  if data == 'manageroot':
    coll = open('new_fqs.txt', 'r')
    line = coll.read()
    array = line.split('\n')
    print(len(array))


bot.polling(none_stop=True, interval=0)

### * Copyright Chuchin Dmitriy Maksimovich - All Rights Reserved
### * Unauthorized copying of any files, via any medium is strictly prohibited
### * Proprietary and confidential
### * Written by Dmitriy Chuchin <chuuchin@yandex.ru>, 18 April 2023
###
