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
    #Получаем текущий список проектов через SOAP перед тестом
    old_projects = app.soap.get_project_list()
    # выбираем случайный проект из списка для удаления
    project_to_delete = random.choice(old_projects)
    # удаляем проект через UI (или через app.project.delete)
    app.project.delete(project_to_delete)
    # получаем новый список проектов через SOAP
    new_projects = app.soap.get_project_list()
    # из старого списка удаляем выбранный проект
    old_projects.remove(project_to_delete)
    # сравниваем
    assert sorted(old_projects) == sorted(new_projects)