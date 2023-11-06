# SiriusTest
Automated tests for the registration form with Selenium and Pytest
Для запуска тестов необходимо:
1) Создать виртуальное окружение и активировать его.
2) Выполнить pip install -r requirements.txt
3) Команда pytest test_registration_page.py - запускает всю серию тестов
4) Можно запускать тесты по группам командой pytest -m имя_группы test_registration_page.py. Доступные группы указаны в файле pytest.ini
5) Можно запускать тесты в разных браузерах (доступны  Google Chrome и Firefox) командой pytest --browser_name=chrome test_registration_page.py. По умолчанию тесты запускаются в  Google Chrome.
