# Автоматизация тест-кейса для сайта МТС

## Описание кейса
Данный тест автоматизирует позитивный и негативный сценарии подключения тарифа на сайте MTS с использованием Playwright и Pytest.

### Структура тестов:
1. Позитивный тест проверяет успешное подключение тарифа при корректном вводе данных.
2. Негативный тест проверяет, что при вводе некорректного адреса появляется сообщение об ошибке.

## Инструкции по запуску:
1. Клонируйте репозиторий или скачайте проект:
    ```bash
    git clone https://github.com/barKoZZeR/Test_tasks_mts.git
   
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt

3. Перейдите в директорию, где у вас находятся тесты, например, если вы находитесь в директории проекта (test_project), то:
    ```bash
   cd Task_2_tests

4. Запустите тесты с помощью следующей команды:
    ```bash
   pytest --headed --slowmo 500

Тесты используют задержку для работы с динамическими элементами интерфейса (используется --slowmo 500).
Для изменения регионов и ввода адресов используются селекторы страницы сайта.