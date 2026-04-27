from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app
        base_url = app.config["web"]["baseUrl"]
        self.client = Client(base_url + "api/soap/mantisconnect.php?wsdl")

    def can_login(self,app,username,password):
        base_url = app.config["web"]["baseUrl"]
        client = Client(base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username,password)
            return True
        except WebFault:
            return False

    def get_project_list(self):

        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']

        projects = self.client.service.mc_projects_get_user_accessible(username, password)

        result = []
        for p in projects:
            result.append(p.name)
        return result
