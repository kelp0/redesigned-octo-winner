#Работу выполнили: Скороходов М. 50%, Лысенко М. 50%, Ячин Д. 40%.

import json

with open('case.json','r') as treefile: #Импорт начального дерева.
    tree = json.load(treefile)

def tree_edit(tree): #Рекурсивная функция, пробегает по вложенным словарям.
    possible_answers = ['yes','no']
    print(tree['question'])
    a = input('Ответом может являться Yes или No: ').lower()
    while a not in possible_answers: #Запрос ответа на вопрос, обработка ошибок.
        a = input('Такого ответа не предусмотрено. Ответом является Yes или No: ').lower()

    if type(tree[a]) == dict: #Проверка типа элемента.
        tree_edit(tree[a])

    elif type(tree[a]) == str:
        print('Вы загадали: ', tree[a])
        reality = input('Ответ удовлетворяет вашим ожиданиям? (Введите Yes или No): ').lower() #Добавление новых вопросов в случае необходимости.
        while reality not in possible_answers:
             reality = input('Такого ответа не предусмотрено. Ответом является Yes или No: ').lower()
        if reality == 'yes':
            print('Благодарим вас за то, что выбрали нашу программу!')
        elif reality == 'no':
            question = input('Какой вопрос помог бы нам отгадать то, что вы загадали?: ')
            new = {'question':question,'yes':None,'no':None}
            print('Спасибо, что помогаете нам улучшать эту программу!')
            tree[a] = new
            
    elif tree[a] is None: #Добавление новго ответа.
        new = input('Наши алгоритмы не в силах найти правильный ответ. Назовите его: ')
        print('Спасибо, что помогаете нам улучшать эту программу!')
        tree[a] = new

tree_edit(tree) #Экспорт полученного дерева.
with open('case.json','w') as treefile:
    json.dump(tree, treefile, indent=3)
        
possible_answers = ['yes','no'] #Цикл, воспроизводящий функцию до тех пор, пока пользователь хочет повторять ее.
contin = ''
while not contin == 'no':
    contin = input('Желаете начать с начала? (Введите Yes или No): ').lower()
    while contin not in possible_answers:
        contin = input('Такого ответа не предусмотрено. Ответом является Yes или No: ').lower
    if contin == 'yes':
        tree_edit(tree)
        with open('case.json','w') as treefile:
            json.dump(tree, treefile, indent=3)

print('До свидания!')
