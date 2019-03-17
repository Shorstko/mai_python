# ==================
# ДЗ состоит из двух частей:

# 1) потренироваться писать код на примере кейса с квартирами

# 2) поиграть в "Угадай число" http://www.mathtask.ru/0047-game-01.php, найти и описать несколько (минимум 2) стратегии, как в нее можно выигрывать быстрее. Старайтесь описывать так, чтобы это было похоже на алгоритм. В идеале - напишите псевдокод
# что такое псевдокод: https://ru.wikipedia.org/wiki/Псевдокод_(язык_описания_алгоритмов)
# примеры псевдокода тут https://ru.wikihow.com/писать-псевдокод
# ==================

import csv
flats_list = list()
with open('output.csv', encoding="utf-8") as csvfile:
	flats_csv = csv.reader(csvfile, delimiter=';')
	flats_list = list(flats_csv)

header = flats_list.pop(0)

#TODO 1:
# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
#и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
for flat in flats_list:
  if "новостройка" in flat:
    print("{}".format(flat))
# 2) добавьте в код выше подсчет количества новостроек


#TODO 2:
# 1) Сделайте описание квартиры в виде словаря. Используйте следующие поля из файла output.csv: ID, Количество комнат, Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:
flat_info = {"id":flat[0], "rooms":flat[1], "type":flat[2], "price":flat[11]}
# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря flat_info, который вы сделали в п.1 
subway_dict = {}
for flat in flats_list:
  subway = flat[3].replace("м.", "")
  flats_dict.setdefault(subway, list())
  subway_dict[subway].append(flat[0])
print(subway_dict)

# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.
# подсказка: делать цикл по словарю можно двумя способами: через ключи или сразу через ключи и значения
# Через ключи (в k получаем ключ, а значение получаем через k):
for k in subway_dict.keys():
  print("У метро {k} найдены квартиры: {subway_dict[k]}")
# Через ключ и значение (получаем сразу все). Обратите внимание на метод items!
for k, v in subway_dict.items():
  print("У метро {k} найдены квартиры: {v}")
