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
        'role': 'admin'
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
        'role': 'admin'
    }
]



clients = [{'name': 'Dmitriy',
            'username': '123',
            'role' : 'client',
            'taken_books': ['joker', 'joper'],
            'history': ['joker', 'joper', 'jojo']
            }]

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

dict_of_arguments_books = {
    'название': 'title',
    'автор': 'author',
    'жанр': 'genre',
    'рейтинг': 'rating',
    'дата публикации': 'date',
    'дата книги': 'book_date'
}

dict_of_arguments_users = {
    'имя': 'username',
    'пароль': 'password',
    'взятые книги': 'taken_books',
    'история': 'history'
}

user_search_dict = {
    '1': 'title',
    '2': 'author',
    '3': 'genre',
    '4': 'date'
}
def start_menu():
    print(f'\t\tДобро пожаловать в сеть библиотеки!\n'
          f'\tВведите ниже свои данные в формате username:password\n'
          f'\t\t\tПример - User:User password\n'
          f'{separator}')
    enter = input().split(':')
    if len(enter) != 2:
        print(f'Вы ввели данные в неправильном формате, просьба ввести их в формате username:password\n{separator}')
        return start_menu()
    for member in members:
        if (enter[0] == member['username']) and (enter[1] == member['password']):
            print(f'Вход успешен!\n{separator}')
            if member['role'] == 'user':
                return user_menu(member=member)
            else:
                return admin_menu(member=member)
    print(f'Введено неправильное имя пользователя или пароль\n{separator}')
    return start_menu()

def user_menu(member=None):
    print(f'Добро пожаловать - {member['username']}!\n'
          f'Выберите действие:\n'
          f'1. Посмотреть каталог книг\n'
          f'2. Найти книгу по названию\n'
          f'3. Найти книгу по жанру\n'
          f'4. Найти книгу по автору\n'
          f'5. Посмотреть книги по рейтингу.\n'
          f'6. Посмотреть взятые книги\n'
          f'7. Посмотреть историю\n'
          f'8. Изменить пароль аккаунта\n'
          f'9. Выход')
    user_input = input('>>> ')
    if user_input == "1":
        print("\n".join(list(map(info, books))))
    elif user_input == "2":
        search('title')
    elif user_input == "3":
        search('genre')
    elif user_input == "4":
        search('author')
    elif user_input == "5":
        sort_rating()
    elif user_input == "6":
        print(separator, f'\nВаши взятые книги:\n{'\n'.join(member["taken_books"])}')
    elif user_input == "7":
        print(separator, f'\nВаши история:\n{'\n'.join(member["history"])}')
    elif user_input == '8':
        change_password(member)
        print('Введите старый и новый пароли в формате old_password:new_password\n\t\tНовый пароль должен содержать минимум 3 символа')
        enter = input().split(':')
        if len(enter) != 2:
            print('Пожалуйста введите пароли в формате old_password:new_password')
        elif enter[0] == enter[1]:
            print('Новый пароль не должен совпадать со старым!')
        elif len(enter[1]) < 3:
            print('Длина нового пароля должна быть больше 3')
        elif enter[0] in member['password']:
            member['password'] = enter[1]
    elif user_input == "9":
        return start_menu()
    else:
        print('Вы ввели некорректную команду, просьба ввести цифру\n')
    return user_menu(member=member)

def admin_menu(member=None):
    print(f'Добро пожаловать - {member['username']}!\n'
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
    if user_input == '1':
        print("".join(list(map(info, books))))
    elif user_input == '2':
        print('\n\n'.join(list(map(user_info, filter(lambda x: x, members)))))
    elif user_input == '3':
        user_search = input('Введите название книги, которую хотите изменить\n>>>')
        edit_book_menu(user_search)
    elif user_input == '4':
        user_search = input('Введите имя пользователя, которого хотите изменить\n>>>')
        edit_user_menu(user_search)
    elif user_input == '5':
        add_object('book')
    elif user_input == '6':
        add_object('user')
    elif user_input == '7':
        change_password(member)
    elif user_input == '8':
        start_menu()
    return admin_menu(member)

def add_object(object_):
    if object_ == 'book':
        books.append({'title': input('Введите название книги\n>>>'), 'author': input('Введите автора\n>>>'),
                      'genre': input('Введите жанр\n>>>'), 'rating': input('Введите жанр\n>>>'),
                      'date': input('Введите год написания книги\n>>>'), 'book_date': input('Введите год выпуска книги\n>>>')})
        return
    members.append({'username': input('Введите имя пользователя\n>>>'), 'password': input('Введите пароль пользователя\n>>>'),
                    'role': 'admin' if input('Напишите "+" если хотите добавить админа, ничего, если пользователя') == '+' else 'user',
                    'taken_books': [], 'history': []})

def edit_user_menu(user_username):
    selected_user = list(map(lambda user: user, filter(lambda user: user_username.lower() in user['username'] and user['role'] != 'admin', members)))
    if len(selected_user) > 1:
        print(f'По вашему запросу, нашлось больше 1 пользователя:\n{"\n".join(list(map(lambda user: user['username'], selected_user)))}\n---\nПросьба более точно ввести имя пользователя')
        return
    elif not selected_user:
        print('Вы не можете изменить данные у пользователя типа Admin!')
        return
    print(selected_user[0]['username'])
    user_choice = input('Это тот пользователь, которого вы хотите изменить y/n | д/н\n>>>')
    if user_choice in ['n', 'н']:
        return
    selected_user = selected_user[0]
    user_choice = input(f'Выберите параметр, который хотите изменить:\n{user_info(selected_user)}\n>>>').lower()
    if user_choice.strip() in dict_of_arguments_users.keys():
        edit_user(dict_of_arguments_users[user_choice.strip()], selected_user['username'])


def edit_user(argument, user_username):
    if argument == 'username':
        print('Введите новое имя пользователя')
    elif argument == 'password':
        print('Введите новый пароль')
    elif argument == 'taken_books':
        user_choice = input('1. Добавить\n2. Убрать\n3. Очистить взятые книги?\n>>>').strip()
        if user_choice== '1':
            add_history('taken_books', user_username)
            return
        elif user_choice == '2':
            remove_history('taken_books', user_username)
            return
        elif user_choice == '3':
            for member in members:
                if member['username'] == user_username:
                    member['taken_books'] = []
                    print('Теперь пользователь выглядит так', separator, user_info(member))
                    break
        else:
            print('Такой команды нет!')
            return
    elif argument == 'history':
        user_choice = input('1. Добавить взятую книгу\n2. Убрать взятую книгу\n3. Очистить все взятые книги?\n>>>').strip()
        if user_choice== '1':
            add_history('history', user_username)
            return
        elif user_choice == '2':
            remove_history('history', user_username)
            return
        elif user_choice == '3':
            for member in members:
                if member['username'] == user_username:
                    member['history'] = []
                    print('Теперь пользователь выглядит так', separator, user_info(member))
                    break
    for member in members:
        if member['username'] == user_username:
            member[argument] = input()
            print('Теперь пользователь выглядит так', separator, user_info(member))
            return

def add_history(argument, user_username):
    for member in members:
        if member['username'] == user_username:
            print(f'Введите название книги')
            member[argument].append(input('>>>'))
            print('Теперь пользователь выглядит так', separator, user_info(member))
            return

def remove_history(argument, user_username):
    for member in members:
        if member['username'] == user_username:
            print(f'Введите номер того параметра, который хотите удалить:\n{'\n'.join(f"{i + 1} - {arg}" for i, arg in enumerate(member[argument]))}')
            user_choice = input()
            member[argument].pop(int(user_choice) - 1) if user_choice.isdigit() else print('Вы ввели не число!')
            print('Теперь пользователь выглядит так', separator, user_info(member))
            return

def sort_rating():
    user_search = input('Выберите, по какому  критерию будет поиск по рейтингу:\n'
                        '1. По названию\n'
                        '2. По автору\n'
                        '3. Без фильтра\n'
                        '>>>')
    if user_search in ['1', '2']:
        print(''.join(list(map(info, sorted(search(user_search_dict[user_search], do_print=False),
                                                               key=lambda book: book['rating'], reverse=True)))))
    elif user_search == '3':
        print(''.join(list((map(info, sorted(books, key=lambda book: book['rating'], reverse=True))))))
    else:
        print('Нет такой команды!')

def edit_book_menu(book_title):
    selected_book = list(map(lambda book: book, filter(lambda book: book_title.lower() in book['title'].lower(), books)))
    if len(selected_book) > 1:
        print(f'По вашему запросу нашлось больше 1 книги:\n{'\n'.join(list(map(lambda book: book['title'], selected_book)))}\n---\nПросьба более точно ввести название книги')
        return
    elif not selected_book:
        print('По вашему запросу не нашлось пользователей')
        return
    print(selected_book[0]['title'])
    user_choice = input('Эта та книга, которую вы хотите изменить y/n | д/н\n>>>')
    if user_choice in ['n', 'н']:
        return
    selected_book = selected_book[0]
    user_choice = input(f"Выберите параметры, которые хотите изменить:\n{info(selected_book)}\n>>>").lower()
    if user_choice.strip() in dict_of_arguments_books.keys():
        edit_book(dict_of_arguments_books[user_choice.strip()], selected_book['title'])
    else:
        print('Такого параметра нет у книги!', separator, sep='\n')

def edit_book(argument, book_title):
    if argument == 'title':
        print('Введите новое название книги')
    elif argument == 'author':
        print('Введите нового автора книги')
    elif argument == 'genre':
        print('Введите новый жанр книги')
    elif argument == 'rating':
        print('Введите новый рейтинг книги')
    elif argument == 'date':
        print('Введите новую дату публикации книги')
    elif argument == 'book_date':
        print('Введите новую дату книги')
    for book in books:
        if book['title'] == book_title:
            book[argument] = input()
            print('Теперь книга выглядит так:', separator, info(book),  sep='\n')
            return

def change_password(member):
    print('Введите старый и новый пароли в формате old_password:new_password\n\t\tНовый пароль должен содержать минимум 3 символа')
    enter = input().split(':')
    if len(enter) != 2:
        print('Пожалуйста введите пароли в формате old_password:new_password без использования знака ":" в пароле!')
    elif enter[0] == enter[1]:
        print('Новый пароль не должен совпадать со старым!')
    elif len(enter[1]) < 3:
        print('Длина нового пароля должна быть больше 3')
    elif enter[0] in member['password']:
        member['password'] = enter[1]
        return
    return change_password(member=member)

def search(argument, do_print=True):
    if argument == 'title':
        user_search = input('Введите названия книг через запятую\n>>>').lower().replace(', ', ',').split(',')
    elif argument == 'author':
        user_search = input('Введите имена авторов через запятую\n>>>').lower().replace(', ', ',').split(',')
    elif argument == 'genre':
        user_search = input('Введите названия жанров через запятую\n>>>').lower().replace(', ', ',').split(',')
    if do_print:
        print(f'---' * 24,
              ''.join(list(map(info, filter(lambda book: any(search_argument.strip() in book[argument].lower() for search_argument in user_search), books)))), sep="\n")
    return list(filter(lambda book: any(search_argument.strip() in book[argument].lower() for search_argument in user_search), books))

def info(book):
    return f'Название - {book['title']}\nАвтор - {book['author']}\nЖанр - {book['genre']}\nРейтинг - {book['rating']}\nДата публикации - {book['date']}\nДата книги - {book['book_date']}\n{separator}\n'

def user_info(user):
    if user['role'] == 'user':
        return (f'Имя - {user['username']}\nРоль - {user['role']}\nПароль - {user['password']}\n'
                f'Взятые книги {user['taken_books']}\n'
                f'История пользователя - {user['history']}')
    return f'Имя - {user['username']}\nРоль - {user['role']}'


if __name__ == '__main__':
    start_menu()