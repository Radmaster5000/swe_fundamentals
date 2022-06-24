

def add_to_dataframe(dataframe, project):
    dataframe['Name'] = [project.name]
    dataframe['Version'] = [project.version]
    dataframe['Description'] = [project.description]
    dataframe['Start Date'] = [project.start_date]
    dataframe['Last Modified'] = [project.last_modified]
    dataframe['Languages used'] = [project.languages]
    dataframe['Contributors'] = [project.contributors]
    dataframe['Link'] = [project.link]
    # dataframe = dataframe.append({'Name': project.name, 'Version': project.version, 'Description': project.description,
    #                               'Start Date': project.start_date, 'Last Modified': project.last_modified,
    #                               'Languages used': project.languages, 'Contributors': project.contributors,
    #                               'Link': project.link}, ignore_index=True)

    return dataframe
