import sqlite3

# Подключение к базе данных
connect = sqlite3.connect('User.db')
cursor = connect.cursor()

# Создание таблиц
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject VARCHAR (50) NOT NULL,
        grade INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    )
''')

connect.commit()

# Функция добавления пользователя
def add_user(name, age, hobby):
    try:
        cursor.execute(
            'INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)',
            (name, age, hobby)
        )
        connect.commit()
        print(f"Пользователь {name} добавлен.")
    except sqlite3.Error as e:
        print("Ошибка при добавлении пользователя:", e)

# Функция добавления оценки
def add_grade(user_id, subject, grade):
    try:
        cursor.execute(
            'INSERT INTO grades (user_id, subject, grade) VALUES (?, ?, ?)',
            (user_id, subject, grade)
        )
        connect.commit()
        print(f"Оценка {grade} по предмету {subject} добавлена пользователю с ID {user_id}.")
    except sqlite3.Error as e:
        print("Ошибка при добавлении оценки:", e)

# Функция получения всех пользователей с их оценками
def get_users_with_grades():
    try:
        cursor.execute('''
            SELECT users.user_id, users.name, users.age, grades.subject, grades.grade
            FROM users 
            LEFT JOIN grades ON users.user_id = grades.user_id
        ''')
        users = cursor.fetchall()
        for user in users:
            print(f"ID: {user[0]}, NAME: {user[1]}, AGE: {user[2]}, SUBJECT: {user[3]}, GRADE: {user[4]}")
    except sqlite3.Error as e:
        print("Ошибка при получении данных:", e)

# Функция обновления оценки по ID оценки
def update_grade(grade_id, new_grade):
    try:
        cursor.execute(
            'UPDATE grades SET grade = ? WHERE grade_id = ?',
            (new_grade, grade_id)
        )
        connect.commit()
        if cursor.rowcount:
            print(f"Subject ID {grade_id} updated to grade {new_grade}!")
        else:
            print(f"Оценка с ID {grade_id} не найдена.")
    except sqlite3.Error as e:
        print("Ошибка при обновлении оценки:", e)

# Функция удаления пользователя по ID (все его оценки тоже удаляются)
def delete_user(user_id):
    try:
        cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
        connect.commit()
        if cursor.rowcount:
            print(f"Пользователь с ID {user_id} удален.")
        else:
            print(f"Пользователь с ID {user_id} не найден.")
    except sqlite3.Error as e:
        print("Ошибка при удалении пользователя:", e)

# Функция удаления оценки по ID
def delete_grade(grade_id):
    try:
        cursor.execute('DELETE FROM grades WHERE grade_id = ?', (grade_id,))
        connect.commit()
        if cursor.rowcount:
            print(f"Оценка с ID {grade_id} удалена.")
        else:
            print(f"Оценка с ID {grade_id} не найдена.")
    except sqlite3.Error as e:
        print("Ошибка при удалении оценки:", e)

# Пример использования
if __name__ == "__main__":
    add_user("Ardager", 23, "плавать")
    add_user("Oleg", 23, "читать")
    add_user("John", 25, "играть в шахматы")

    add_grade(1, "Алгебра", 5)
    add_grade(2, "Геометрия", 4)
    add_grade(3, "Физика", 3)

    print("\n--- Список пользователей с оценками ---")
    get_users_with_grades()

    print("\n--- Обновляем оценку ---")
    update_grade(2, 5)

    print("\n--- Удаляем пользователя с ID 1 ---")
    delete_user(1)

    print("\n--- Список пользователей после удаления ---")
    get_users_with_grades()

# Закрываем соединение
connect.close()
