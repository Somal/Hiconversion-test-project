Время решения задания: 13:00 - 23:30 4 июня 2016 (c перерывами)

### Запуск системы 
Для запуска надо клонировать репозиторий, зайти в папку `project` и вызвать в консоли `python manage.py runserver --insecure &`

Далее запуститься сервер. Форма логина можно посмотреть по адресу `http://localhost:8000/`.
Для создания инвайти нужно зайти в админку по `http://localhost:8000/admin/`. Там есть таблица `Invites`. При создании новой строчки в этой таблице создастся инвайт и в консоли Вы найдете ссылку для активации.
После перехода по ссылке Вы увидете Ваш логин и пароль, который и надо ввести в форме входа в систему.

### Улучшения
- Больше тестов
- Поиск багов в security
- Оптимизация быстродействия
