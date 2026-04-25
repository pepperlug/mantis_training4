# test/test_add_project.py
from model.projects import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randint(3, maxlen))])


def test_add_project(app):
    def test_add_project(app):
        # Генерируем имя проекта
        project_name = random_string("Project-", 10)
        # Создаем обьект проекта
        project_data = Project(name=project_name, description="Test project description")
        # Получаем список проектов до добавления нового
        old_projects = app.project.get_project_list()
        # Создаём новый проект
        app.project.create(project_data)
        # Получаем список проектов после добавления
        new_projects = app.project.get_project_list()
        # Добавляем имя созданного проекта в старый список для сравнения
        old_projects.append(project_name)
        # Сортируем списки
        old_projects.sort()
        new_projects.sort()
        # Проверяем старый и новый список проектов
        assert old_projects == new_projects