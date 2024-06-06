DIR = ""


def show_info_screen(data):
    global DIR
    with open(f"{DIR}Bobatron.js", 'r', encoding='utf-8') as f:
        BOBATRON = f.read()
    with open(f"{DIR}info_screen.js", 'r', encoding='utf-8') as f:
        ret = f"{BOBATRON}\n{f.read()}\n"
        ret += f"InfoScreen.create('{data}');"
    return ret


def learn_quiz_parser():
    global DIR
    with open(f"{DIR}learnQuizParser.js", 'r', encoding='utf-8') as f:
        ret = f.read()
    return ret
