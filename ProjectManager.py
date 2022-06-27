from Project import *
import pandas as pd



class ProjectManager:
    """
    Dataframe object to store all the projects as rows.
    """
    def __init__(self):
        self._projects = pd.DataFrame(columns=['Name', 'Version', 'Description', 'Start Date',
                                               'Last Modified', 'Languages Used', 'Contributors',
                                               'Link'])

    @property
    def projects(self):
        return self._projects

    def add_to_dataframe(self, project):
        """
        Takes a project object and converts the data into a DataFrame row

        Args:
             project (project object): All of the inputted information in relation to the project

        """
        # MORE ELEGANT WAY OF SETTING THE VALUES USED INSTEAD
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
        """
        Reads the data from the test_data file and writes it to the DataFrame.
        """
        test_data = pd.read_csv('test_data.csv', index_col=False, quotechar="'")
        self._projects = self._projects.append(test_data, ignore_index=True)
        print("demo data loaded!")

    def remove_row(self):
        """
        Deletes the specified row from the DataFrame.
        """
        index = input("please choose an index, or type 'c' to cancel: ")
        if index == 'c' or index == 'C':
            print("returning to main menu")
        else:
            self._projects = self._projects.drop(int(index))
            print("row removed")

    def update_record(self):
        """
        Changes the data in the specified cell to the new input from the user.
        """
        index = input("please choose an index to update, or type 'c' to cancel: ")
        if index == 'c' or index == 'C':
            print("returning to main menu")
        else:
            index = int(index)
            attr = input("please enter the attribute you would like to update: ")
            new_value = input("please enter the new value of the attribute: ")
            # THE BELOW WAS QUITE LENGTHY TO WRITE OUT FOR EACH ATTRIBUTE, SO WAS MADE SHORTER
            # if attr == 'Name':
            #     new_value = input("please enter the new value of the attribute: ")
            #     valid = check_name(new_value)
            #     if valid:
            #         self._projects.at[index, attr] = new_value
            #         print("record updated")
            #     else:
            #         print("sorry, invalid input")
            if (attr == 'Name' and check_name(new_value)) or (attr == 'Version' and check_version(new_value))\
                    or (attr == 'Description' and check_description(new_value)) or (attr == 'Start Date' and check_start_date(new_value))\
                    or (attr == 'Last Modified' and check_last_modified(new_value)) or  attr == 'Link' and check_link(new_value):
                self._projects.at[index, attr] = new_value
                print("record updated")
            elif (attr == 'Languages Used' and check_lang(new_value)) or (attr == 'Contributors' and check_cont(new_value)):
                new_list = f"[{new_value}]"
                self._projects.at[index, attr] = new_list
                print("record updated")
            else:
                print("sorry, invalid input")



