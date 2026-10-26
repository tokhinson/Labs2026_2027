from csv import reader
from math import floor
from random import randint
import xml.dom.minidom as minidom

def get_table(filename):
    try:
        with open(filename, mode='r', encoding='windows-1251') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            return table
    except FileNotFoundError:
        print(f"файл не найден: {filename}")
        return 0


# задание 1
# table = get_table('books.csv')[1::]

# countLines30 = 0
# for line in table:
#     if len(line[1]) > 30: countLines30 += 1
# print(f'Количество книг с названием более 30 символов: {countLines30}')

# while True:
#     autor = input('Искать книги 2015 или 2018 автора: ').lower()
#     countResults = 0
#     for line in table:
#         if autor in line[4].lower() and line[6].split()[0][-4::] in ['2015', '2018']:
#             print(f' Автор: {line[4]}; ID: {line[0]}; Название: {line[1]}; Имеющийся тип: {line[2]}; Дата поступления: {line[6]}; Цена: {line[7]} рублей')
#             countResults += 1

#     if countResults == 0:
#         print(f'\u001b[31mСовпадений не найдено\u001b[0m')
#     else:
#         print(f'\u001b[32mВсего найдено: {countResults} совпадений\u001b[0m')

#     n = input('Продолжить поиск? (y/n): ')
#     if n.lower() == 'n':
#         break

# with open('booksInfo.txt', 'w') as file:
#     for i in range(1, 21):
#         rndm = randint(0, len(table))
#         link = f'{table[rndm][4]}. {table[rndm][1]} - {table[rndm][6].split()[0][-4::]}'
#         file.write(f'{i}) {link} + \n')


# задание 2
with minidom.parse('currency.xml') as dom:
    dom.normalize()

    elements = dom.getElementsByTagName('Valute')

    valutedict = dict()

    for node in elements:
        charCode, nominal = '', 0
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'CharCode' and child.firstChild.nodeType == 3:
                    charCode = child.firstChild.data
            if child.nodeType == 1:
                if child.tagName == 'Nominal' and child.firstChild.nodeType == 3:
                    nominal = int(child.firstChild.data)
        if charCode != '' and nominal != 0:
            valutedict[charCode] = nominal

    print(valutedict)


# допзадание
# table = get_table('books-en.csv')[1::]
# publishers = set()

# popularBooks = sorted(table, key=lambda x: -int(x[5]))[0:20:]

# with open('booksInfo.txt', 'a') as file:

#     file.write('Все имеющиеся издательства:\n')
#     for line in table:
#         publishers.add(line[4])

#     for publ in publishers:
#         file.write(publ+'\n')

#     file.write('\n\n20 Самых популярных книг:\n')
#     for line in popularBooks:
#         file.write(f'{line[2]}. {line[1]} - {line[3]}\n')
 
