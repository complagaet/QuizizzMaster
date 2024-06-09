import json


def main(params, table):
    while True:
        questions = input("Скопируй сюда JSON, выданный парсером: ")
        try:
            table.collect_questions(json.loads(questions))
        except:
            print("-- Ошибка! Попробуй еще раз бро!")

        table.generate_table()
        if input(" 1. Продолжить\n 2. Выход\n > ") == "2":
            break
