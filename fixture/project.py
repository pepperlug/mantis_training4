class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        # Переход в раздел управления проектами
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    #метод создания проекта
    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector('input[value="Add Project"]').click()

    #метод удаления проекта
    def delete(self, name):
        wd = self.app.wd
        self.open_projects_page()
        # кликаем по имени проекта, чтобы открыть его свойства
        wd.find_element_by_link_text(name).click()
        # Нажимаем кнопку "Delete Project"
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        # подтверждаем удаление на второй странице
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()

    #ввод данных проекта
    def fill_project_form(self, project):
        wd = self.app.wd
        #
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    #получение списка проектов
    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        projects = []
        for element in wd.find_elements_by_css_selector("table tr td a"):
            name = element.text
            if name:
                projects.append(name)
        return projects