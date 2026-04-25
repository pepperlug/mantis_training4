from model.projects import Project
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randint(3, maxlen))])

def test_delete_project(app):
    #проверяем, есть ли хотя бы один проект, если нет — создаем
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="ProyyU", description="Hetuut"))
    # генерируем имя проекта
    project_name = random_string("Project-", 10)
    # создаём объект проекта
    project_data = Project(name=project_name, description="Test project description")
    # получаем список проектов до создания нового
    old_projects = app.project.get_project_list()
    # создаём проект
    app.project.create(project_data)
    # получаем список проектов после создания
    projects_after_create = app.project.get_project_list()
    # проверяем, что проект действительно появился
    assert project_name in projects_after_create
    # удаляем проект
    app.project.delete(project_name)
    # получаем список проектов после удаления
    new_projects = app.project.get_project_list()
    # формируем ожидаемый список
    old_projects.append(project_name)
    # убираем удаленный проект из ожидаемого списка
    old_projects.remove(project_name)
    # сортируем списки перед сравнением
    old_projects.sort()
    new_projects.sort()
    # проверяем, что проект удалён корректно
    assert old_projects == new_projects