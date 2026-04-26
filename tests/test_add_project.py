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
        # Получаем список проектов до добавления нового через Soap
        old_projects = app.soap.get_project_list()
        app.project.create(project_data)
        #Получаем список проектов после добавления нового через Soap
        new_projects = app.soap.get_project_list()
        old_projects.append(project_name)
        #формируем списки
        old_projects.sort()
        new_projects.sort()
        #cравниваем
        assert old_projects == new_projects