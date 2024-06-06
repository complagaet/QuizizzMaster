from selenium import webdriver
from selenium.webdriver.common.by import By
import JS.oh_my_js_collection as js_collection
import json


js_collection.DIR = "../JS/"


def main(params, driver, table):
    while True:
        try:
            driver.find_element(by=By.CLASS_NAME, value='course-target-link')
            print("-- Успешно вошел в аккаунт!")
            selector(params, driver, table)
            break
        except:
            continue


def selector(params, driver, table):
    while True:
        try:
            driver.find_element(by=By.CLASS_NAME, value='date-summary')
            break
        except:
            driver.execute_script(
                js_collection.show_info_screen(
                    f"<span style=\"color: green; font-weight: bold\">Здарова! Всего вопросов собрано: {table.total}<br></span>"
                    f"Выбери курс, откуда будешь брать вопросы<br>"
                    f"Закрой браузер чтобы закончить<br>"
                )
            )
            continue

    collector(params, driver, table)


def collector(params, driver, table):
    while True:
        try:
            driver.find_element(by=By.CLASS_NAME, value='response-label')
            driver.execute_script(
                js_collection.show_info_screen(
                    f"<span style=\"color: green; font-weight: bold\">Скачиваем твои переписки...<br></span>"
                    f"Подожди чуть-чуть<br>"
                )
            )
            driver.execute_script(
                js_collection.learn_quiz_parser()
            )
            try:
                driver.find_element(by=By.ID, value='learnParsedData')
                print(f"!!! {driver.title} OK!")
                count = table.collect_questions(json.loads(driver.find_element(by=By.ID, value='learnParsedData').text))
                table.generate_table()
                driver.execute_script(
                    js_collection.show_info_screen(
                        f"<span style=\"color: green; font-weight: bold\">Готово, {count} собрано! ({table.total} всего)<br></span>"
                        f"Иди к следующему квизу, зая<br>"
                    )
                )
                while True:
                    try:
                        driver.find_element(by=By.CLASS_NAME, value='response-label')
                    except:
                        collector(params, driver, table)
                        break
            except:
                continue
        except:
            try:
                driver.find_element(by=By.CLASS_NAME, value='date-summary')
                driver.execute_script(
                    js_collection.show_info_screen(
                        f"<span style=\"color: green; font-weight: bold\">Отлично! Всего вопросов собрано: {table.total}<br></span>"
                        f"А теперь, выбери квиз, крошка))<br>"
                    )
                )
            except:
                driver.execute_script(
                    js_collection.show_info_screen(
                        f"<span style=\"color: red; font-weight: bold\">Купи очки...<br></span>"
                        f"Малыш, ты открыл какую-то фигню... Открой квиз!!!<br>"
                    )
                )
