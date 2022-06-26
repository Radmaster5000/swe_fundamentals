from Exceptions import *
from Project import Project
import pandas as pd


class ProjectManager:

    def __init__(self):
        self._projects = pd.DataFrame(columns=['Name', 'Version', 'Description', 'Start Date',
                                               'Last Modified', 'Languages used', 'Contributors',
                                               'Link'])

    @property
    def projects(self):
        return self._projects

    def add_to_dataframe(self, project):
        self._projects['Name'] = [project.name]
        self._projects['Version'] = [project.version]
        self._projects['Description'] = [project.description]
        self._projects['Start Date'] = [project.start_date]
        self._projects['Last Modified'] = [project.last_modified]
        self._projects['Languages used'] = [project.languages]
        self._projects['Contributors'] = [project.contributors]
        self._projects['Link'] = [project.link]
        # self._projects.append({'Name': project.name, 'Version': project.version, 'Description': project.description,
        #                               'Start Date': project.start_date, 'Last Modified': project.last_modified,
        #                               'Languages used': project.languages, 'Contributors': project.contributors,
        #                               'Link': project.link}, ignore_index=True)

    def load_demo_data(self):
        self._projects = pd.read_csv('test_data.csv', index_col=False, quotechar="'")
        print("demo data loaded!")

    def remove_row(self):
        index = int(input("please choose an index: "))
        self._projects = self._projects.drop(index)
        print("row removed")

# # Load data
# test_dataframe = pd.read_csv('test_data.csv')

    # def add(self, project):
    #     if isinstance(project, Project):
    #         if project in self.projects:
    #             raise ProjectManagerError("Project already in Project Manager")
    #         self._projects.append(project)
    #
    # def remove(self, project):
    #     if isinstance(project, Project) and project in self.projects:
    #         self._projects.remove(project)
    #
    # @property
    # def number_of_projects(self):
    #     return len(self._projects)
    #
    # def clear(self):
    #     self._projects.clear()

