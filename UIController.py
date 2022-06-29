from Project import create_project


def add_project(project_manager):
    """
    Create a new Project object, then add it to the Project Manager DataFrame

    Args:
        project_manager (Project Manager object): The active DataFrame within the application
    """
    _project = create_project()
    print("project created..")
    project_manager.add_to_dataframe(_project)
    print("project added to project manager..")


def display_projects(project_manager):
    """
    Print the Project Manager DataFrame to the terminal

    Args:
        project_manager (Project Manager object): The active DataFrame within the application
    """
    if project_manager.projects.empty:
        print("No projects to display")
        return
    else:
        print(project_manager.projects)

    return


def quit_app(project_manager):
    """
    Saves the DataFrame and exits the application.
    """
    confirm = input("Are you sure you want to quit?").lower()
    if confirm == 'y':
        project_manager.projects.to_csv("CSV_Files/project_manager.csv", index=False)
        print("Project Manager saved")
        quit()
    else:
        return 0