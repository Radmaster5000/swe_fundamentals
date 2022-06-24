from Project import create_project
import ProjectManager


def add_project(project_manager):

    _project = create_project()
    print("project created..")
    project_manager.add(_project)
    print("project added to project manager..")


def display_projects(project_manager):
    for i in project_manager.projects:
        print(i)


def quit_app():
    confirm = input("Are you sure you want to quit?").lower()
    if confirm == 'y':
        print("Save file?")
        quit()
    else:
        return 0