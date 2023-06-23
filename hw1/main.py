from psycopg2 import connect

from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from os import getenv

load_dotenv()
credentials = {
    'host': getenv('PG_HOST'),
    'port': int(getenv('PG_PORT')),
    'user': getenv('PG_USER'),
    'password': getenv('PG_PASSWORD'),
    'dbname': getenv('PG_DBNAME'),
}

connection = connect(**credentials, cursor_factory=RealDictCursor)
cursor = connection.cursor()
cursor.execute('SELECT * from equipment')
data = cursor.fetchall()
if len(data) > 10:
    new_len = 10
if len(data) <= 10:
    new_len = len(data)
print('Викторина на тему: Россия')
print("Для выхода нажмите 'q'")
rans, chislo = 0, 0
while chislo < new_len:
    row = data[chislo]
    id = row['id']
    question = row['question']
    answer_1 = row['answer_1']
    answer_2 = row['answer_2']
    answer_3 = row['answer_3']
    right_answer = int(row['right_answer'])
    print('\n'.join((f'Вопрос № {id}',
                        f'{question}',
                        'Варианты ответа: ',
                        f'{answer_1}',
                        f'{answer_2}',
                        f'{answer_3}',
                        'Ваш ответ: \n')))
    otvet_int = input()
    if otvet_int == 'q':
        break
    try:
        otvet = int(otvet_int)
    except ValueError:
        print('Вводите число!')
        continue
    if otvet == int(right_answer):
        print('Правильно!\n')
        rans += 1
    else:
        print(f'Неверно! Правильный ответ: {right_answer}\n')
    chislo += 1
print(f'Ваш результат: {rans} из {new_len}')

cursor.close()
connection.close()
