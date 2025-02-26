Описание
Проект предназначен для автоматизации тестирования веб-приложения с использованием Selenium, pytest и Allure. Тесты написаны на Python.

Установка
1.	Клонируйте репозиторий:
git clone https://github.com/username/repository.git
2.	Перейдите в директорию проекта:
cd Sprint_6
3.	Создайте и активируйте виртуальное окружение:
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
4.	Установите зависимости:
pip install -r requirements.txt
Запуск тестов

Для запуска тестов используйте команду:
pytest
Для генерации отчета Allure:
pytest --alluredir=allure-results
allure serve allure-results

Структура проекта
	tests/: Каталог с тестами.
	pages/: Страницы для реализации паттерна Page Object.
	conftest.py: Конфигурация для pytest.
