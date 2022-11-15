# Создайте список set_1, содержащий случайные числа в интервале [1, 10]. Он показывает количество элементов в списке
# пользователь. Посмотреть список.
# • Создайте второй список set_2, содержащий случайные числа в интервале [5, 15]. Количество элементов списка
# предоставляется пользователем. Посмотреть список.
# • Получить номер от пользователя. Напишите условный оператор, основанный на значении
# сохраненных в списках, будет отображаться одно из следующих сообщений: «Номер из набора 1», «Номер из
# набор 2" или "Такого номера нет в обоих наборах".
# • Создайте список set_1_2, объединяющий значения из списков set_1 и set_2. Сортировать и отображать
# список.




while True:
    import random

    list_1 = [1, 10]
    list_2 = [5, 15]
    generovane_liczby = int(input("Podaj liczbe"))

    for y  in range (generovane_liczby):
        x = random.randint(1, 10)
        list_1.append(x)

    print(list_1)
    generovane_liczby = int(input("Podaj liczbe"))

    for y in range(generovane_liczby):
        x = random.randint(5, 15)
        list_2.append(x)
    print(list_2)

    y = int(input("enter licz: "))
    if y in list_2:
        print("Number of first list")
    elif y in list_2:
        print("Number of secont list")
    else: print("Number not exitst of both lists")
    list_1_2 = list_1 + list_2
    print(list_1_2)
    list_1_2.sort()
    print(list_1_2)


    print("Spróbuj ponownie")