from Project import create_project
from DataframeController import add_to_dataframe
import ProjectManager


def add_project(project_manager, new_dataframe):

    _project = create_project()
    print("project created..")
    project_manager.add(_project)
    new_dataframe = add_to_dataframe(new_dataframe, _project)
    print("project added to project manager..")



def display_projects(project_manager, new_dataframe):
    if len(project_manager.projects) == 0:
        print("No projects to display")
        return

    valid = False
    while not valid:
        view = input("Please type '1' for an overview of projects, or '2' for full details: ")
        if view == '1':
            for i in project_manager.projects:
                print(i)
                valid = True
        elif view == '2':
            print(new_dataframe)
            valid = True
        else:
            print("Invalid selection")

    return


def quit_app():
    confirm = input("Are you sure you want to quit?").lower()
    if confirm == 'y':
        print("Save file?")
        quit()
    else:
        return 0