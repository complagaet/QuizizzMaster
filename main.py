from selenium import webdriver
from selenium.webdriver.common.by import By
import JS.oh_my_js_collection as js_collection
import scenarios.learn
import storage


js_collection.DIR = "JS/"


def main(params):
    print(params)

    driver = webdriver.Chrome()
    driver.get(params['url'])
    driver.implicitly_wait(3)

    driver.execute_script(
        js_collection.show_info_screen(
            f"<span style=\"color: green; font-weight: bold\">Добро пожаловать в QuizzizMaster</span><br>"
            f"Чтобы продолжить войди в учётку бро"
        )
    )

    table = storage.Table(params['save_path'])

    if params['type'] == 1:
        scenarios.learn.main(params, driver, table)

    input()


def collect_startup_params():
    print("Салам, это прога для сбора твоих переписок :)\n==================")
    url = {
        1: 'https://learn.astanait.edu.kz/dashboard',
        2: 'https://moodle.astanait.edu.kz/login/index.php'
    }
    params = {
        'url': "",
        'type': int(input('Выбери тип работы:\n 1. Learn\n 2. Moodle (НЕ РАБОТАЕТ)\n > ')),
        'save_path': storage.save_as("result.xlsx")
    }
    if (1 <= params['type'] <= 1) and params['save_path']:
        params['url'] = url[params['type']]
        return params
    else:
        print("\n==================\nФигово ввёл параметры...\n==================\n")
        collect_startup_params()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(collect_startup_params())
