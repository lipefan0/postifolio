from app.models.project import Project

class ProjectController:
    @staticmethod
    def get_all_projects():
        # Aqui você pode carregar dados do seu arquivo data.py ou de um banco de dados
        projects_data = [
            {"title": "Projeto 1", "description": "Descrição 1", "image_url": "url1", "project_url": "url1"},
            {"title": "Projeto 2", "description": "Descrição 2", "image_url": "url2", "project_url": "url2"}
        ]
        return [Project(**project) for project in projects_data]

    @staticmethod
    def get_project_by_title(title):
        # Lógica para buscar um projeto específico
        pass