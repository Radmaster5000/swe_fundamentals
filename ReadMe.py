

def ReadMe():
    """
    Displays information regarding purpose and usage of the application
    """

    print("""
    PURPOSE
    This application has been created to log Projects used by the team and record information regarding who worked on
    it. This is so that a team member who is new to a project can find a little more information about it.
    
    BASIC USAGE:
    
    CREATE A NEW PROJECT
    (Input the following fields; name, version, description,
    start date, last modified, languages, contributors,
    link to the repository)

    REMOVE PROJECTS
    (Delete a project that has been abandoned/no longer needs to be recorded)

    UPDATE PROJECTS
    (Editing an existing project)
    PLEASE NOTE: When changing values for 'Languages Used' or 'Contributors', please enter all new values in one
    entry. Values should be separated by a comma.

    DISPLAY PROJECTS
    (Print the Projects currently contained within the Project Manager
    
    LOAD DATA
    (load any csv file into the current Project Manager) 
    Enter the name of the file without .csv suffix and make sure the .csv file is in the main directory.
    
    QUIT
    The user is asked if they want to save the DataFrame to a CSV file. Choosing 'yes' prompts the user to enter
    a name for the file. If the user does not save, any inputted information from the session will be lost.
    """)

