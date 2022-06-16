import unittest
from Exceptions import *
from Project import Project


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
        project = Project('Alpha', 0.1, 'Develop data storage app', '2022-05-01', '2022-05-02', ['Python'], ['Phil'], 'github.com/radmaster5000')

        # Assert
        self.assertEqual('Alpha', project.name)
        self.assertEqual(0.1, project.version)
        self.assertEqual('Develop data storage app', project.description)
        self.assertEqual('2022-05-01', project.start_date)
        self.assertEqual('2022-05-02', project.last_modified)
        self.assertEqual(['Python'], project.languages)
        self.assertEqual(['Phil'], project.contributors)
        self.assertEqual('github.com/radmaster5000', project.link)

    def test_create_project_missing_name(self):
        # Assert
        with self.assertRaises(ProjectNameError) as context:
            project = Project('', 0.1, 'Develop data storage app', '2022-05-01', '2022-05-02', ['Python'], ['Phil'], 'github.com/radmaster5000' )
        self.assertEqual('Project name must be between 1 and 10 characters', str(context.exception))

    def test_create_project_long_name(self):
        # Assert
        with self.assertRaises(ProjectNameError) as context:
            project = Project('Supercalofragelisticexpiali-project', 0.1, 'Develop data storage app', '2022-05-01', '2022-05-02', ['Python'], ['Phil'], 'github.com/radmaster5000' )
        self.assertEqual('Project name must be between 1 and 10 characters', str(context.exception))


if __name__ == '__main__':
    unittest.main()
