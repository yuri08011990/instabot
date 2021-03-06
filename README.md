## **Instabot**

Бот для 'накрутки' лайків і підписників.

______________

Принцип роботи:
Користувач задає список хештегів, які близькі по тематиці його акаунту.
Бот збирає певну кількість довільних постів по кожному хештегу (також у довільному порядку) та лайкає їх. І все. Користувачі, чиї фотки було лайкнуто з імовірністю приблизно 30% лайкають у відповідь, та з імовірністю приблизно 15% підписуються. Цей показник неточний і залежить від тематики акаунтів.

______________

Увага:
Лише для української версії Інстаграму. На інших мовах інтерфейсу працювати не буде.

______________

Вимоги для запуску:

 - Бот працює лише з браузером Firefox 
 - Для роботи бота потрібно встановити geckodriver. 
 - Також потрібно встановити Селеніум. `pip install selenium` в командному рядку.

______________

Як запустити:
Відкрити файл settings.py текстовим редактором та вписати свої логін/пароль у відповідні поля. Також слід перелічити список хештегів, по яких має орієнтуватись бот.
В командному рядку ввести `python igbot.py` знаходячись у директорії зі скриптом.

______________

В планах:

 - [ ] Додати інтерфейс
 - [ ] Додати підтримку англійської мови

______________

<img src="https://drive.google.com/uc?export=view&id=1YKMrFKDI16S0F3J4fswX2AKU0o3tBbqP" width=500>
<img src="https://drive.google.com/uc?export=view&id=1GXwiFdoMD5YC7SkV_ivOYuBEvbuMUKkm" width=500>
