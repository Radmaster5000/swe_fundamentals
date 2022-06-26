from Project import create_project
from ProjectManager import ProjectManager
import ProjectManager


def add_project(project_manager):

    _project = create_project()
    print("project created..")
    project_manager.add_to_dataframe(_project)
    print("project added to project manager..")


def display_projects(project_manager):
    if project_manager.projects.empty:
        print("No projects to display")
        return

    else:
        print(project_manager.projects)
    # valid = False
    # while not valid:
    #     view = input("Please type '1' for an overview of projects, or '2' for full details: ")
    #     if view == '1':
    #         for i in project_manager.projects:
    #             print(i)
    #             valid = True
    #     elif view == '2':
    #         print(new_dataframe)
    #         valid = True
    #     else:
    #         print("Invalid selection")

    return


def quit_app():
    confirm = input("Are you sure you want to quit?").lower()
    if confirm == 'y':
        print("Save file?")
        quit()
    else:
        return 0