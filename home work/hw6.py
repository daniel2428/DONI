import sqlite3

# Подключение к базе данных
connect = sqlite3.connect('User.db')
cursor = connect.cursor()

# Создание таблицы, если ее нет
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# Функция для добавления пользователя
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")

# Добавление пользователей
add_user("John", 33, "swimming")
add_user("Samma", 23, "reading")
add_user("Wacka", 12, "dancing")

# Функция для получения всех пользователей
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print("Все пользователи получены:")

    for user in users:
        print(f"NAME: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")

get_all_users()

# Функция для получения пользователя по имени
def get_user_by_name(name):
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    user = cursor.fetchone()
    if user:
        return f"NAME: {user[0]} AGE: {user[1]} HOBBY: {user[2]}"
    else:
        return "Пользователь не найден"

# Пример вызова функции
print(get_user_by_name('John'))

