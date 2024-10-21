# Django-сервер с REST API и Swagger

## Описание
Это простой сервер, созданный на базе Django с использованием Django REST Framework (DRF). Сервер предоставляет два основных маршрута для обработки запросов:
1. **/inverse (POST)**: принимает JSON, меняет местами ключи и их значения.
2. **/unstable (GET)**: с рандомной вероятностью возвращает либо статус 200 с сообщением "HAPPY", либо статус 400 с сообщением "UNHAPPY".

Также сервер включает документацию API с использованием Swagger
## Инструкция к запуску

1. Клонируйте репозиторий или скачайте проект:
    ```bash
    git clone https://github.com/barKoZZeR/Test_tasks_mts.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd Task_3_server
    ```

3. Создайте виртуальную среду:
    ```bash
    python -m venv venv


4. Активируйте виртуальную среду:
    - Для macOS и Linux:
      ```bash
      source venv/bin/activate

    - Для Windows:
      ```bash
      venv\Scripts\activate


5. Установите зависимости:
    ```bash
    pip install -r requirements.txt

##Запуск сервера
1. Запустите сервер с помощью команды:
    ```bash
    python manage.py runserver

2. Откройте браузер и перейдите по адресу: http://127.0.0.1:8000/. Вы увидите интерфейс Swagger для тестирования API.
3. В открывшемся интерфейсе нажмите на "POST /inverse/", далее "Try it out".
4. Поменяйте значение "string" на "value1" и нажмите "Execute".
5. В ответ вы получите {"value1": "key1"}.
6. Нажмите на "GET /unstable/" ---> "Try it out" ---> "Execute"
7. Когда вы будете нажимать "Execute" - вы будете получать рандомные ответы (HAPPY или UNHAPPY), в зависимости от кода ответа.