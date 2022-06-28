import unittest
from swe_fundamentals.Exceptions import *
from swe_fundamentals.Project import Project


class ProjectTests(unittest.TestCase):
    def test_default_values(self):
        # Arrange

        # Act
        project = Project()

        # Assert
        self.assertEqual('Example', project.name)
        self.assertEqual(0.0, project.version)
        self.assertEqual('Default description', project.description)
        self.assertEqual('2022-01-01', project.start_date)
        self.assertEqual('2022-01-01', project.last_modified)
        self.assertEqual(['None'], project.languages)
        self.assertEqual(['None'], project.contributors)
        self.assertEqual('http://www.arm.com', project.link)

    def test_create_project_values(self):
        # Arrange

        # Act
        project = Project('Alpha', 0.1, 'Develop data storage app', '2022-05-01', '2022-05-02', ['Python'], ['Phil'], 'http://www.github.com/radmaster5000')

        # Assert
        self.assertEqual('Alpha', project.name)
        self.assertEqual(0.1, project.version)
        self.assertEqual('Develop data storage app', project.description)
        self.assertEqual('2022-05-01', project.start_date)
        self.assertEqual('2022-05-02', project.last_modified)
        self.assertEqual(['Python'], project.languages)
        self.assertEqual(['Phil'], project.contributors)
        self.assertEqual('http://www.github.com/radmaster5000', project.link)

    def test_create_project_missing_name(self):
        # Assert
        with self.assertRaises(ProjectNameError) as context:
            project = Project('', 0.1, 'Develop data storage app', '2022-05-01', '2022-05-02', ['Python'], ['Phil'], 'http://www.github.com/radmaster5000' )
        self.assertEqual('Project name must be between 1 and 10 characters', str(context.exception))

    def test_create_project_long_name(self):
        # Assert
        with self.assertRaises(ProjectNameError) as context:
            project = Project('Supercalofragelisticexpiali-project', 0.1, 'Develop data storage app', '2022-05-01', '2022-05-02', ['Python'], ['Phil'], 'http://www.github.com/radmaster5000' )
        self.assertEqual('Project name must be between 1 and 10 characters', str(context.exception))

    def test_create_project_version_integer(self):
        # Assert
        with self.assertRaises(ProjectVersionError) as context:
            project = Project('Alpha', 1, 'test version', '2022-05-01', '2022-05-02', ['Python'], ['Phil'], 'http://www.github.com/radmaster5000')
        self.assertEqual('Version must be of type: float', str(context.exception))

    def test_create_project_long_description(self):
        # Assert
        with self.assertRaises(ProjectDescriptionError) as context:
            project = Project('Alpha', 0.1, 'Develop data storage appDevelop data storage appDevelop data storage appDevelop data storage appDevelop data storage appDevelop data storage appDevelop data storage app', '2022-05-01', '2022-05-02', ['Python'], ['Phil'], 'http://www.github.com/radmaster5000' )
        self.assertEqual('Description must be less than 150 chars', str(context.exception))

    def test_start_date_format(self):
        # Assert
        with self.assertRaises(ProjectStartDateError) as context:
            project = Project('Alpha', 0.1, 'Develop data storage app', '01/05/22', '2022-05-02', ['Python'], ['Phil'], 'http://www.github.com/radmaster5000')
        self.assertEqual('Start date must be in format YYYY-MM-DD', str(context.exception))

    def test_last_modified_format(self):
        # Assert
        with self.assertRaises(ProjectLastModifiedError) as context:
            project = Project('Alpha', 0.1, 'Develop data storage app', '2022-05-02', '01/05/22', ['Python'], ['Phil'], 'http://www.github.com/radmaster5000')
        self.assertEqual('Last modified date must be in format YYYY-MM-DD', str(context.exception))

    def test_languages_not_string(self):
        # Assert
        with self.assertRaises(ProjectLanguagesError) as context:
            project = Project('Alpha', 0.1, 'Develop data storage app', '2022-05-02', '2022-05-02', [1], ['Phil'], 'http://www.github.com/radmaster5000')
        self.assertEqual("All languages must be of type: 'string'", str(context.exception))

    def test_contributors_not_string(self):
        # Assert
        with self.assertRaises(ProjectContributorsError) as context:
            project = Project('Alpha', 0.1, 'Develop data storage app', '2022-05-02', '2022-05-02', ['Python'], [1], 'http://www.github.com/radmaster5000')
        self.assertEqual("All contributors must be of type: 'string'", str(context.exception))

    def test_contributors_empty(self):
        # Assert
        with self.assertRaises(ProjectContributorsError) as context:
            project = Project('Alpha', 0.1, 'Develop data storage app', '2022-05-02', '2022-05-02', ['Python'], [], 'http://www.github.com/radmaster5000')
        self.assertEqual("Contributors needs at least one person. Like, you!", str(context.exception))

    def test_link_missing_prefix(self):
        # Assert
        with self.assertRaises(ProjectLinkError) as context:
            project = Project('Alpha', 0.1, 'Develop data storage app', '2022-05-02', '2022-05-02', ['Python'], ['Phil'], 'github.com/radmaster5000')
        self.assertEqual("Link must contain full link, starting with 'http://' or 'https://'", str(context.exception))

if __name__ == '__main__':
    unittest.main()
