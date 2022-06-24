from ProjectManager import ProjectManager
from Project import Project
from UIController import add_project, display_projects, quit_app

#import pandas as pd

from Exceptions import *
# from Help import help
# # Load data
# test_dataframe = pd.read_csv('test_data.csv')
# print(test_dataframe)


# Setup
new_project_manager = ProjectManager()

# Launch UI
def main_menu():
    selection = 0
    while selection != 5:
        selection = input("""
        
        Please select an option:
        1 = Create a project
        2 = Remove a project
        3 = Update a project
        4 = Display a project
        5 = Help
        6 = Quit
        
        """)

        try:
            selection = int(selection)
        except ValueError:
            pass

        if selection == 1:
            add_project(new_project_manager)
            # REFACTORED OUT TO A FUNCTION IN A UICONTROLLER MODULE
            # new_project = Project()
            # add_project = new_project.create_project()
            # print("project created..")
            # new_project_manager.add(add_project)
            # print("project added to project manager..")

        elif selection == 2:
            print("remove_record()")
        elif selection == 3:
            print("update_record()")
        elif selection == 4:
            display_projects(new_project_manager)
            # REFACTORED OUT TO A FUNCTION IN A UICONTROLLER MODULE
            # for i in new_project_manager.projects:
            #     print(i)
        elif selection == 5:
            help()
        elif selection == 6:
            selection = quit_app()
        else:
            print("Invalid selection")





if __name__ == '__main__':
    main_menu()


