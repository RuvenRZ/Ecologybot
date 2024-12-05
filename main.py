import telebot
from telebot import types 
bot = telebot.TeleBot('7468396677:AAH6slPbmoclJqZBHoQb_H7yq--UmzK5o1k')

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Plastic = types.KeyboardButton('Пластик')
    Paper = types.KeyboardButton('Бумага')
    Glass = types.KeyboardButton('Стекло')
    BIO = types.KeyboardButton('БИО отходы')
    kb.row(Plastic, Paper)
    kb.row(Glass, BIO)
    bot.send_message(message.from_user.id, 'Привет, я бот помощник, я могу показать в какой мусорный бак ты должен выкинуть свои отходы чтобы сохранить лучшее!\n что вам надо выбросить?', reply_markup=kb )

@bot.message_handler(content_types=['text'])
def print_text(message):
    if message.text == 'Пластик':
        bot.send_message(message.from_user.id, 'Пластиковые бутылки, Пластикавая посуда')
    elif message.text == 'Бумага':
        bot.send_message(message.from_user.id, 'Бумага любого формата, картон' )
    elif message.text == 'Стекло':
        with open(f'images/glass.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)  
            bot.send_message(message.from_user.id, 'Стеклянные бутылки, Зеркала' )
    elif message.text == 'БИО отходы':
        bot.send_message(message.from_user.id, 'Фрукты, Овощи' )
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю' )


bot.polling()
