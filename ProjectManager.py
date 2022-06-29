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

    def load_data(self):
        """
        Reads the data from the test_data file and writes it to the DataFrame.
        """
        file = input("Please enter the name of the file you wish to load (without csv extension), or type 'c' "
                     "to cancel: ")
        if not cancel(file):
            try:
                existing_data = pd.read_csv(f"CSV_Files/{file}.csv", index_col=False, quotechar="'")
                self._projects = self._projects.append(existing_data, ignore_index=True)
                self._projects = change_to_commas(self._projects)
                print("data loaded!")
            except FileNotFoundError:
                print("Sorry, that file cannot be found")

    def save_data(self):
        """
        Saves the data to a csv file.
        """
        file = input("What would you like to call the file? (without csv extension), or type 'c' "
                     "to cancel: ")
        if not cancel(file):
            self._projects = change_from_commas(self._projects)
            self._projects.to_csv(f"CSV_Files/{file}.csv", index=False)
            print(f"File saved to: CSV_Files/{file}.csv")

    def remove_row(self):
        """
        Deletes the specified row from the DataFrame.
        """
        index = input("please choose an index, or type 'c' to cancel: ")
        # THE BELOW WAS REFACTORED INTO THE cancel(choice) FUNCTION
        # if index == 'c' or index == 'C':
        #     print("returning to main menu")
        if not cancel(index):
            self._projects = self._projects.drop(int(index))
            print("row removed")

    def update_record(self):
        """
        Changes the data in the specified cell to the new input from the user.
        """
        index = input("please choose an index to update, or type 'c' to cancel: ")
        # THE BELOW WAS REFACTORED INTO THE cancel(choice) FUNCTION
        # if index == 'c' or index == 'C':
        #     print("returning to main menu")
        if not cancel(index):
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


def cancel(choice):
    if choice == 'c' or choice == 'C':
        print("Returning to main menu")
        return True
    else:
        return False


def change_to_commas(dataframe):
    """
    Changes all the ';' to ',' to give the impression of a list
    Args:
        dataframe: The DataFrame containing semi-colons

    Returns:
        dataframe: The DataFrame containing commas
    """
    for i in range(len(dataframe["Languages Used"])):
        dataframe["Languages Used"][i] = dataframe["Languages Used"][i].replace(';', ',')

    for i in range(len(dataframe["Contributors"])):
        dataframe["Contributors"][i] = dataframe["Contributors"][i].replace(';', ',')

    return dataframe


def change_from_commas(dataframe):
    """
    Changes all the ',' to ';' to give the impression of a list
    Args:
        dataframe: The DataFrame containing commas

    Returns:
        dataframe: The DataFrame containing semi-colons
    """
    for i in range(len(dataframe["Languages Used"])):
        dataframe["Languages Used"][i] = dataframe["Languages Used"][i].replace(',', ';')

    for i in range(len(dataframe["Contributors"])):
        dataframe["Contributors"][i] = dataframe["Contributors"][i].replace(',', ';')

    return dataframe
