from Exceptions import *
from Project import Project
import pandas as pd


class ProjectManager:

    def __init__(self):
        self._projects = pd.DataFrame(columns=['Name', 'Version', 'Description', 'Start Date',
                                               'Last Modified', 'Languages Used', 'Contributors',
                                               'Link'])

    @property
    def projects(self):
        return self._projects

    def add_to_dataframe(self, project):
        # self._projects['Name'] = [project.name]
        # self._projects['Version'] = [project.version]
        # self._projects['Description'] = [project.description]
        # self._projects['Start Date'] = [project.start_date]
        # self._projects['Last Modified'] = [project.last_modified]
        # self._projects['Languages Used'] = [project.languages]
        # self._projects['Contributors'] = [project.contributors]
        # self._projects['Link'] = [project.link]
        self._projects.loc[len(self._projects.index)] = [project.name, project.version, project.description,
                                                    project.start_date, project.last_modified, project.languages,
                                                    project.contributors, project.link]

    def load_demo_data(self):
        test_data = pd.read_csv('test_data.csv', index_col=False, quotechar="'")
        self._projects = self._projects.append(test_data, ignore_index=True)
        print("demo data loaded!")

    def remove_row(self):
        index = input("please choose an index, or type 'c' to cancel: ")
        if index == 'c' or index == 'C':
            print("returning to main menu")
        else:
            self._projects = self._projects.drop(int(index))
            print("row removed")

    def update_record(self):
        index = input("please choose an index to update, or type 'c' to cancel: ")
        if index == 'c' or index == 'C':
            print("returning to main menu")
        else:
            index = int(index)
            attr = input("please enter the attribute you would like to update: ")
            new_value = input("please enter the new value of the attribute: ")
            self._projects.at[index, attr] = new_value
            print("record updated")

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

