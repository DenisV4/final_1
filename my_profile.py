# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
n = ''
a = 0
ph = ''
e = ''
x = 0
ad = 0
i = ''
# business info
og = ''
inn = ''
ac = ''
bn = ''
rtn = ''
ca = ''

def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, x_parameter, ad_parameter, i_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Индекс: ', x_parameter)
    print('Почтовый адрес: ', ad_parameter)
    if i:
        print('')
        print('Дополнительная информация:')
        print(i_parameter)

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

def validate_number(line, length):
    size = 0
    for char in line:
        if not char.isdigit():
            return False
        size += 1

    return size == length

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                n = input('Введите имя: ')
                while 1:
                    # validate user age
                    a = int(input('Введите возраст: '))
                    if a > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch

                e = input('Введите адрес электронной почты: ')
                ux = input('Введите Индекс: ')
                x = ''.join(c for c in ux if c.isdigit())
                ad = input('Введите почтовый адрес: ')
                i = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input business info
                while 1:
                    og = input("Введите ОГРНИП: ")
                    if validate_number(og, 15):
                        break
                    print('ОГРНИП должен содержать 15 цифр')

                inn = input("Введите ИНН: ")
                while 1:
                    ac = input("Введите расчётный счёт: ")
                    if validate_number(ac, 20):
                        break
                    print('Расчётный счёт должен содержать 20 цифр')

                bn = input("Введите название банка: ")
                rtn = input("Введите БИК: ")
                ca = input("Введите корреспондентский счёт: ")
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(n, a, ph, e, x, ad, i)

            elif option2 == 2:
                general_info_user(n, a, ph, e, x, ad, i)

                # print business info
                print('')
                print('Информация о предпринимателе:')
                print('ОГРНИП: ', og)
                print('ИНН: ', inn)
                print('Банковские реквизиты')
                print('Расчётный счёт: ', ac)
                print('Название банка: ', bn)
                print('БИК: ', rtn)
                print('Корреспондентский счёт: ', ca)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
