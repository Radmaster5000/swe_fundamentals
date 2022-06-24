from Exceptions import *
from Project import Project


class ProjectManager:

    def __init__(self):
        self._projects = []

    @property
    def projects(self):
        return self._projects

    def add(self, project):
        if isinstance(project, Project):
            if project in self.projects:
                raise ProjectManagerError("Project already in Project Manager")
            self._projects.append(project)

    def remove(self, project):
        if isinstance(project, Project) and project in self.projects:
            self._projects.remove(project)

    @property
    def number_of_cars(self):
        return len(self._projects)

    def clear(self):
        self._projects.clear()

