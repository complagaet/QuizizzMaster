# QuizizzMaster

The program was created to collect and convert quizzes from the [learn.astanait.edu.kz](https://learn.astanait.edu.kz) and Moodle to Quizizz-compatable *.xlsx file. 
![App Screenshot](https://i.imgur.com/JVIpc1R.png)
![App Screenshot](https://i.imgur.com/TjjG0PR.png)
For the program to work, you need to have completed a lecture in [learn.astanait.edu.kz](https://learn.astanait.edu.kz) or an open review of a quiz in Moodle

## Launch

Selenium, OpenPyXL and Tkinter must be installed in your Python environment.
```bash
pip install selenium
pip install openpyxl
pip install tk
```
After installing these modules, you can launch QuizizzMaster via main.py using CMD or Terminal.
```bash
python main.py
```
Also, by default it uses Google Chrome as the browser to work with, but you can change the browser in main.py to any modern one supported by Selenium.

## Export and Usage

QuizizzMaster automatically saves all collected questions, so after all the work you can close the program with peace of mind and upload the result to Quizizz 😌
![App Screenshot](https://i.imgur.com/SnZp7wa.png)