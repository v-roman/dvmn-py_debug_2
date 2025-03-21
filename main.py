import os
from dotenv import load_dotenv
from weather_sdk import get_new_event, SMSServer

load_dotenv()

token = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'

token_sms = os.getenv('SMS_TOKEN')
server = SMSServer(token_sms)

new_event = get_new_event(token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{1}: {2} {3} {4} ожидается {0}. Будьте внимательны и осторожны.'''

sms_message = sms_template.format(
phenomenon_description,
    town_title,
    event_time,
    event_date,
    event_area,
)

server.send(sms_message)
# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: вывод в терминал Регион:  Погода:
# Вывод: гипотеза оправдалась

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: вывод в терминал Курск
# Вывод: гипотеза оправдалась

# Гипотеза 2.2: В town_title не название города
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: вывод в терминал Курск
# Вывод: гипотеза оправдалась

# Гипотеза 3: token на самом деле пуста
# Способ проверки: Выведу переменную token
# Код для проверки: print(token)
# Установленный факт: вывод в терминал None
# Вывод: гипотеза верна переменная token пуста

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Выведу переменную token
# Код для проверки: print(token)
# Установленный факт: вывод в терминал aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: гипотеза оправдалась в переменной token есть данные

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: Выведу переменную token
# Код для проверки: print(token)
# Установленный факт: вывод в терминал aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: гипотеза подтвердилась

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: Выведу переменную token до строчки new_event
# Код для проверки: print(token)
# Установленный факт: вывод в терминал aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: гипотеза подтвердилась

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Выведу переменную event_time
# Код для проверки: print(event_time, 'event_time')
# Установленный факт: вывод в терминал утром и в дневное время event_time
# Вывод: гипотеза оправдалась в переменной event_time - время

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Выведу переменную event_date
# Код для проверки: print(event_date, 'event_date')
# Установленный факт: вывод в терминал 19 марта event_date
# Вывод: гипотеза оправдалась, в переменной event_date - дата

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Выведу переменную event_area
# Код для проверки: print(event_area, 'event_area')
# Установленный факт: вывод в терминал к. Архыз event_area
# Вывод: гипотеза оправдалась, в переменной event_area - место

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Выведу переменную phenomenon_description
# Код для проверки: print(phenomenon_description, 'phenomenon_description')
# Установленный факт: вывод в терминал усиление ветра порывами до 14 м/с phenomenon_description
# Вывод: гипотеза оправдалась, в переменной phenomenon_description - погодного явления

# Гипотеза 6: Переменные написаны с опечаткой
# Способ проверки: выделить переменную и проверить подсветяться ли другие такие же переменные
# Установленный факт: переменные подсвечиваются
# Вывод: гипотеза оправдалась, переменные записаны правильно

# Гипотеза 7: названия переменных нужно записывать в обычных скобках
# Способ проверки: заменить фигурные скобки на обычные
# Код для проверки: sms_template = '''(town_title): (event_time) (event_date) (event_area) ожидается (phenomenon_description). Будьте внимательны и осторожны.'''
# Установленный факт: ошибка исчезла, но переменные не передались в .format
# Вывод: переменные в скобках передавать можно

# Гипотеза 8: В шаблоне нужно использовать номерные индексы вместо именных
# Способ проверки: заменить индексы на номерные
# Код для проверки: sms_template = '''{1}: {2} {3} {4} ожидается {0}. Будьте внимательны и осторожны.'''
# Установленный факт: код работает
# Вывод: гипотеза подтвердилась