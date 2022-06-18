
## Всем привет. Это мой новый проект по работе с почтовым ящиком.



![This is screenshot](https://sun9-9.userapi.com/impg/-9g3vCOB_51dQijzQ44XBEFWNrKuktA0WvOe8A/P0vN5o47BK8.jpg?size=898x319&quality=95&sign=95a924bf57ccffe50e59679d53e4484e&type=album)
- Скачайте все файлы в новую папку на своём компьютере
- С помощью терминала перейдите в эту новую папку - **cd ~\your_directory**
- Создайте виртуальное окружение для работы с этим проектом в этой директории - **python -m venv venv**
- Активируйте его с помощью команды -  **venv\Scripts\activate (для Windows)**
- Установите в своё окружение нужные зависимости - **pip install -r requirements.txt**

## Чтобы запустить тест используйте команду:
> pytest -s -v test_mail.py

## Тест должен выполнить все пункты из этой задачи
> 1.	Login to any email box.
> 2.	Send from 10 mails from current box to yourself with:
> - Theme: Random string with 10 symbols (letters and numbers only)
> - Body: Random string with 10 symbols (letters and numbers only)
> 3.	Check that all 10 mails are delivered.
> 4.	Collect data from all incoming mails and save it as Object (Dictionary), where:
> - Key is theme of mail
> - Value is body of mail
> 5.	Send collected data to yourself as: “Received mail on theme {Theme} with message: {Body}. It contains {Count of letters} letters and {Count of numbers} numbers” (repeat for each mail).
> 6.	Delete all received mails except the last one.
