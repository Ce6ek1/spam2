separator = '---' * 24

members = [
    {
        # Лёгкий вход USER
        'username': 'u',
        'password': 'u',
        'role': 'user',
        'taken_books': ['Дракула'],
        'history': ['Гарри Поттер и Тайная комната', 'О дивный новый мир']
    },
    {
        # Лёгкий вход ADMIN
        'username': 'a',
        'password': 'a',
        'role': 'admin',
        'taken_books': [],
        'history': []
    },
    {
        'username': 'Oleg',
        'password': 'qwerty',
        'role': 'user',
        'taken_books': ["Война и мир"],
        'history': ["Преступление и наказание", "451 градус по Фаренгейту", "Дракула"]
    },
    {
        'username': 'CoolMan228',
        'password': 'CoolPassword123',
        'role': 'user',
        'taken_books': ['Преступление и наказание', 'Моби Дик'],
        'history': ['Гарри Поттер и Тайная комнат', 'Идиот']
    },
    {
        'username': 'Admin',
        'password': 'ReallyHardPassword',
        'role': 'admin',
        'taken_books': [],
        'history': []
    }
]

books = [
    {
        'title': 'Война и мир',
        'author': 'Лев толстой',
        'genre': 'классика',
        'rating': 4.1,
        'date': 1873,
        'book_date': 2002
    },
    {
        'title': 'Преступление и наказание',
        'author': 'Федор Достоевский',
        'genre': 'классика',
        'rating': 4.8,
        'date': 1866,
        'book_date': 2012
    },
    {
        'title': 'Гарри Поттер и философский камень',
        'author': 'Дж.К. Роулинг',
        'genre': 'фэнтези',
        'rating': 4.8,
        'date': 1997,
        'book_date': 2015
    },
    {
        'title': 'Властелин колец',
        'author': 'Джон Рональд Руэл Толкин',
        'genre': 'фэнтези',
        'rating': 4.9,
        'date': 1955,
        'book_date': 2001
    },
    {
        'title': "451 градус по Фаренгейту",
        'author': 'Рэй Брэдбери',
        'genre': "научная фантастика",
        'rating': 4.5,
        'date': 1953,
        'book_date': 1996
    },
    {
        'title': 'Сияние',
        'author': 'Стивен Кинг',
        'genre': 'хоррор',
        'rating': 4.7,
        'date': 1977,
        'book_date': 2011
    },
    {
        'title': 'Эмма',
        'author': 'Джейн Остин',
        'genre': 'романтика',
        'rating': 4.4,
        'date': 1815,
        'book_date': 2002
    },
    {
        'title': 'Дракула',
        'author': 'Брам Стокер',
        'genre': 'хоррор',
        'rating': 4.5,
        'date': 1897,
        'book_date': 1998
    },
    {
        'title': 'Скотный двор',
        'author': 'Джордж Оруэлл',
        'genre': 'комедия',
        'rating': 4.6,
        'date': 1945,
        'book_date': 2004
    },
    {
        'title': 'Хроники Нарнии',
        'author': 'Клайв Стейплз Льюис',
        'genre': 'фэнтези',
        'rating': 4.8,
        'date': 1956,
        'book_date': 2018
    },
    {
        'title': 'Анна Каренина',
        'author': 'Лев Толстой',
        'genre': 'классика',
        'rating': 4.7,
        'date': 1877,
        'book_date': 2003
    },
    {
        'title': 'Идиот',
        'author': 'Федор Достоевский',
        'genre': 'классика',
        'rating': 4.6,
        'date': 1869,
        'book_date': 1999
    },
    {
        'title': 'Гарри Поттер и Тайная комната',
        'author': 'Дж.К. Роулинг',
        'genre': 'фэнтези',
        'rating': 4.8,
        'date': 1998,
        'book_date': 2020
    },
    {
        'title': 'Время жить и время умирать',
        'author': 'Эрих Мария Ремарк',
        'genre': 'классика',
        'rating': 4.5,
        'date': 1954,
        'book_date': 1997
    },
    {
        'title': 'Моби Дик',
        'author': 'Герман Мелвилл',
        'genre': 'классика',
        'rating': 4.4,
        'date': 1851,
        'book_date': 2001
    },
    {
        'title': 'Гарри Поттер и узник Азкабана',
        'author': 'Дж.К. Роулинг',
        'genre': 'фэнтези',
        'rating': 4.9,
        'date': 1999,
        'book_date': 2022
    },
    {
        'title': 'Крестный отец',
        'author': 'Марио Пьюзо',
        'genre': 'криминальный роман',
        'rating': 4.8,
        'date': 1969,
        'book_date': 1999
    },
    {
        'title': 'О дивный новый мир',
        'author': 'Олдос Хаксли',
        'genre': 'научная фантастика',
        'rating': 4.7,
        'date': 1932,
        'book_date': 2002
    },
    {
        'title': 'Краткая история времени',
        'author': 'Стивен Хокинг',
        'genre': 'научная литература',
        'rating': 4.6,
        'date': 1988,
        'book_date': 1992
    },
    {
        'title': 'Хоббит, или Туда и обратно',
        'author': 'Джон Рональд Руэл Толкин',
        'genre': 'фэнтези',
        'rating': 4.8,
        'date': 1937,
        'book_date': 2004
    },
    {
        'title': '1984',
        'author': 'Джордж Оруэлл',
        'genre': 'дистопия',
        'rating': 4.6,
        'date': 1949,
        'book_date': 2001
    },
    {
        'title': 'Мидлмарч',
        'author': 'Джордж Элиот',
        'genre': 'классика',
        'rating': 4.5,
        'date': 1871,
        'book_date': 1993
    },
    {
        'title': 'Убить пересмешника',
        'author': 'Харпер Ли',
        'genre': 'классика',
        'rating': 4.7,
        'date': 1960,
        'book_date': 2003
    },
    {
        'title': 'В поисках утраченного времени',
        'author': 'Марсель Пруст',
        'genre': 'классика',
        'rating': 4.5,
        'date': 1927,
        'book_date': 1993
    },
    {
        'title': 'Рождение злого',
        'author': 'Стивен Кинг',
        'genre': 'хоррор',
        'rating': 4.6,
        'date': 1981,
        'book_date': 2014
    },
    {
        'title': 'Оно',
        'author': 'Стивен Кинг',
        'genre': 'хоррор',
        'rating': 4.7,
        'date': 1986,
        'book_date': 2019
    },
    {
        'title': 'Норвежский лес',
        'author': 'Харуки Мураками',
        'genre': 'современная проза',
        'rating': 4.6,
        'date': 1987,
        'book_date': 2000
    },
    {
        'title': 'Чужак в стране чужих',
        'author': 'Роберт Хайнлайн',
        'genre': 'научная фантастика',
        'rating': 4.4,
        'date': 1961,
        'book_date': 2003
    },
    {
        'title': 'Дикая вода',
        'author': 'Виктория По',
        'genre': 'романтика',
        'rating': 4.5,
        'date': 2005,
        'book_date': 2023
    },
    {
        'title': 'Задачи на разные темы',
        'author': 'Сергей Довлатов',
        'genre': 'современная проза',
        'rating': 4.4,
        'date': 1991,
        'book_date': 1993
    },
    {
        'title': 'Слепые отдельности',
        'author': 'Игорь Губерман',
        'genre': 'сатира',
        'rating': 4.5,
        'date': 1996,
        'book_date': 2007
    }
]

dict_of_arguments_members = {
    '1': 'username',
    '2': 'password',
    '3': 'role',
    '4': 'taken_books',
    '5': 'history'
}

dict_of_arguments_books = {
    '1': 'title',
    '2': 'author',
    '3': 'genre',
    '4': 'rating',
    '5': 'date',
    '6': 'book_date'
}

user_search_dict = {
    '1': 'title',
    '2': 'author',
    '3': 'genre',
}

def start_menu():
    print(f'{separator}\n\t\tДобро пожаловать в сеть библиотеки!\n'
          f'\tВведите ниже свои данные в формате username:password\n'
          f'\t\t\tПример - User:User password\n'
          f'{separator}')
    enter = input().split(':')
    if len(enter) != 2:
        print('Вы ввели данные в неправильном формате, просьба ввести их в формате username:password')
        return start_menu()
    for member in members:
        if enter[0] == member['username'] and enter[1] == member['password']:
            print('Вход успешен!')
            if member['role'] == 'user':
                return user_menu(member=member)
            return admin_menu(member=member)
    print('Логин или пароль неправильный!')
    return start_menu()

def user_menu(member):
    print(f'\n{separator}\nДобро пожаловать - {member['username']}!\n'
          f'Выберите действие:\n'
          f'1. Посмотреть каталог книг\n'
          f'2. Найти книгу по названию\n'
          f'3. Найти книгу по автору\n'
          f'4. Найти книгу по жанру\n'
          f'5. Сортировка книг по рейтингу.\n'
          f'6. Посмотреть свой аккаунт\n'
          f'7. Изменить пароль аккаунта\n'
          f'8. Выход')
    user_input = input('>>> ')
    if user_input in user_commands:
        if user_input == '2':
            user_commands[user_input]('title')
        elif user_input == '3':
            user_commands[user_input]('author')
        elif user_input == '4':
            user_commands[user_input]('genre')
        elif user_input in ['6', '7']:
            user_commands[user_input](member)
        else:
            user_commands[user_input]()
    else:
        print('Данной команды нет в списке!')
    user_menu(member=member)


def admin_menu(member):
    print(f'\n{separator}\nДобро пожаловать - {member['username']}!\n'
          f'Выберите действие:\n'
          f'1. Посмотреть каталог книг\n'
          f'2. Посмотреть список клиентов\n'
          f'3. Изменить книгу\n'
          f'4. Изменить пользователя\n'
          f'5. Добавить книгу\n'
          f'6. Добавить пользователя\n'
          f'7. Изменить пароль\n'
          f'8. Выход')
    user_input = input('>>> ')
    if user_input in admin_commands:
        if user_input in ['3', '5']:
            admin_commands[user_input]('book')
        elif user_input == '4':
            admin_commands[user_input]('member', member)
        elif user_input == '6':
            admin_commands[user_input]('member')
        elif user_input == '7':
            change_password(member=member)

        else:
            admin_commands[user_input]()
    admin_menu(member=member)


def search_books(argument, do_print=True):
    if argument == 'title':
        user_input = input('Введите название книги\n').lower().strip()
    elif argument == 'author':
        user_input = input('Введите имя автора\n').lower().strip()
    else:
        user_input = input('Введите жанр книги\n').lower().strip()
    if not do_print:
        return list(filter(lambda book: user_input in book[argument].lower(), books))
    print_books(list_of_books=(list(filter(lambda book: user_input in book[argument].lower(), books))))

def sort_books():
    user_input = input('Введите номер того, по какому критерию сделать фильтрацию:\n1. Название\n2. Автор\n3. Жанр\n')
    if user_input not in user_search_dict.keys():
        print('Вы ввели некорректное значение')
        return
    user_input = user_search_dict[user_input]
    print_books(list_of_books=(list(sorted(search_books(user_input, do_print=False), key=lambda book: book['rating'], reverse=True))))

def change_password(member):
    new_password = input('Введите новый пароль: ')
    if ':' in new_password:
        print('В пароле не может содержать знак ":"')
        return change_password(member=member)
    member['password'] = new_password

def print_members():
    print('\n'.join(list(map(lambda member: f'\nUsername - {member['username']}\nПароль - {member['password']}\nРоль - {member['role']}\n'
          f'Взятые книги - {member['taken_books']}\nИстория - {member['history']}', members))))

def print_member(member):
    print(f'\nUsername - {member['username']}\nПароль - {member['password']}\nРоль - {member['role']}\n'
          f'Взятые книги - {member['taken_books']}\nИстория - {member['history']}')

def print_books(list_of_books=books):
    print('\n\n'.join(list(map(lambda book: f'Название - {book['title']}\nАвтор - {book['author']}\nЖанр - {book['genre']}\n'
                                            f'Рейтинг - {book['rating']}\nГод публикации произведения - {book['date']}\n'
                                            f'Год создания книги - {book['book_date']}', list_of_books))))

def print_book(book):
    print(f'Название - {book['title']}\nАвтор - {book['author']}\nЖанр - {book['genre']}\n'
                                            f'Рейтинг - {book['rating']}\nГод публикации произведения - {book['date']}\n'
                                            f'Год создания книги - {book['book_date']}')

def add_thing(thing):
    if thing == 'book':
        try:
            books.append({'title': input('Введите название книги: ').strip(), 'author': input('Введите имя автора: ').strip(), 'genre': input('Введите жанр книги: ').strip(),
                          'rating': float(input('Введите рейтинг книги: ')), 'date': int(input('Введите год публикации произведения: ')),
                          'book_date': int(input('Введите год создания книги: '))})
        except ValueError:
            print('Вы ввели не число!')
        print('Книга успешно добавлена!')
    if thing == 'member':
        new_username = input('Введите username пользователя: ').strip()
        for member in members:
            if new_username == member['username']:
                print('Пользователь с таким username уже существует!')
                return
        members.append({'username': input('Введите username пользователя: ').strip(), 'password': input('Введите пароль пользователя: ').strip(),
                        'role': 'admin' if input('Введите + чтобы добавить админа').strip() == '+' else 'user', 'taken_books': [],
                        'history': []})
        print('Пользователь успешно добавлен!')

def edit_thing(thing, current_member):
    if thing == 'book':
        user_input = input('Введите название книги, которую хотите изменить: ').lower().strip()
        for book in books:
            if user_input == book['title'].lower():
                print_book(book)
                user_input = input('Какое значение книги вы хотите изменить?\n1. Название\n2. Автор\n3. Жанр\n4. Рейтинг\n5. Год публикации\n6. Год создания книги\n')
                if user_input in dict_of_arguments_books.keys():
                    if user_input == '1':
                        book[dict_of_arguments_books[user_input]] = input('Введите название книги: ')
                    elif user_input == '2':
                        book[dict_of_arguments_books[user_input]] = input('Введите имя автора книги: ')
                    elif user_input == '3':
                        book[dict_of_arguments_books[user_input]] = input('Введите жанр книги: ')
                    elif user_input == '4':
                        book[dict_of_arguments_books[user_input]] = float(input('Введите рейтинг книги: '))
                    elif user_input == '5':
                        book[dict_of_arguments_books[user_input]] = int(input('Введите год публикации произведения: '))
                    else:
                        book[dict_of_arguments_books[user_input]] = int(input('Введите год создания книги: '))
                    return
                else:
                    print('Вы ввели несуществующую команду')
                    return
        print('такой книги нет в списке книг!')
    if thing == 'member':
        user_input = input('Введите username пользователя, которого хотите изменить: ').strip()
        for member in members:
            if user_input == member['username'].lower():
                if user_input == current_member['username']:
                    print('Вы не можете изменить себя')
                    return
                print_member(member)
                user_input = input('Какое значение пользователя вы хотите изменить?\n1. Username\n2. Пароль\n3. Роль\n'
                                   '4. Взятые книги\n5. История')
                if user_input in dict_of_arguments_members.keys():
                    if user_input == '1':
                        element = input('Введите новый username, не используя знак ":": ')
                        if ':' in user_input:
                            print('Новый username содержит знак ":"')
                            return
                        member[dict_of_arguments_members[user_input]] = element
                    elif user_input == '2':
                        element = input('Введите новый пароль, не используя знак ":": ')
                        if ':' in user_input:
                            print('Новый username содержит знак ":"')
                            return
                        member[dict_of_arguments_members[user_input]] = element
                    elif user_input == '3':
                        member[dict_of_arguments_members[user_input]] = 'admin' if input('Введите + если хотите изменить роль на admin: ') == '+' else 'user'
                    elif user_input == '4':
                        elements = input('Введите книги, которые хотите добавить во взятые книги через запятую: ').split(', ')
                        for element in elements:
                            member[dict_of_arguments_members[user_input]].append(element)
                        return
                    elif user_input == '5':
                        elements = input('Введите книги, которые вы хотите добавить в историю через запятую: ')
                        for element in elements:
                            member[dict_of_arguments_members[user_input]].append(element)
                    return
                else:
                    print('Вы ввели несуществующую команду!')
                    return
        print('Такого пользователя нет в списке')

user_commands = {
    '1': print_books,
    '2': lambda argument: search_books(argument),
    '3': lambda argument: search_books(argument),
    '4': lambda argument: search_books(argument),
    '5': sort_books,
    '6': lambda member: print_member(member),
    '7': lambda member: change_password(member),
    '8': start_menu
}

admin_commands = {
    '1': print_books,
    '2': print_members,
    '3': lambda thing: edit_thing(thing, None),
    '4': lambda thing, member: edit_thing(thing, member),
    '5': lambda thing: add_thing(thing),
    '6': lambda thing: add_thing(thing),
    '7': lambda member: change_password(member),
    '8': start_menu
}

if __name__ == '__main__':
    start_menu()
