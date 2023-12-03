import telebot
# create a new bot instance
bot = telebot.TeleBot('6157533013:AAG7ZxpndJqg7VG5sA_6tWlGePc8XlT4xto')

# define a handler function for the '/start' command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'REUBNE ELVIS Welcome to the official Telegram bot of our college! This bot has been created to assist our students with essential information related to college operations.\nUpon pressing the "/help" button, you will be directed to a comprehensive guide on the bots functionalities. Our bot is specifically designed to cater to the needs of our students by providing them with up-to-date information regarding college timing, bus schedules, and personnel in charge of different sectors.\nAs a student, you can easily access information about college schedules, including classes, exams, and holidays. Moreover, you can use this bot to find out the bus timings, routes, and destinations. This will help you to plan your commute to and from the college with ease.\nIn addition, the bot allows you to search for the contact details of different personnel in charge of various departments and services in the college. Whether you need to get in touch with the library staff or the IT department, our bot has got you covered.\nOverall, this bot is an excellent tool for students to stay informed about the college day-to-day operations. We hope that you find this bot helpful and convenient to use. Thank you for choosing our college as your place of learning.')

# define a handler function for the '/MG' command
@bot.message_handler(commands=['MG'])
def MG_user(message):
    bot.reply_to(message, 'MUDDA GUDU')
# define a handler function for the 'HODS' command
@bot.message_handler(commands=['HODS'])
def send_welcome(message):
    bot.reply_to(message, 'cse hod:-Mr.A.NARENDAR SIR\nphone no:-9*******\nDS hod:-V.Sambha Shiva rao\nphone no:-8919129028')
# define the function to handle the /help command
@bot.message_handler(commands=['help'])
def help(message):
    response = "Here are the commands I understand:\n"
    response += "/start - Start the bot\n"
    response += "/help - Show this help message\n"
    response += "/student-info - Get information about students\n"
    response += "/exams - Get information about exams\n"
    response += "/buss_info - Get information about the bus\n"
    response += "/status - Get the status of something\n"
    response += "/HODS - Get information about HOD\n"
    bot.reply_to(message, response)
# define a handler function for the 'buss' command
@bot.message_handler(commands=['buss'])
def send_welcome(message):
    bot.reply_to(message, 'Bus timings from your designated stop are scheduled between 7:30 and 8:00 in the morning. The bus service commences at 4:15 pm from the college premises and drops students and staff off at their respective stops, which serve as the buss pick-up points.for more info contact \n MR.******** \n \t phone no:9******')
# define a handler function for the 'students' command
@bot.message_handler(commands=['students'])
def send_welcome(message):
    bot.reply_to(message, 'hi')        
# start the bot
bot.polling()