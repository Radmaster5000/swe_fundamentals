import unittest
from ProjectManager import ProjectManager
from UIController import display_projects, add_project, quit_app


class UITests(unittest.TestCase):
    def test_no_projects_to_display(self):
        # Arrange
        _project_manager = ProjectManager()

        # Assert
        self.assertEqual(None, display_projects(_project_manager))

    def test_add_project_without_manager(self):
        # Act
        with self.assertRaises(TypeError) as context:
            add_project()
        self.assertEqual("add_project() missing 1 required positional argument: 'project_manager'", str(context.exception))

    def test_quit_app_without_manager(self):
        # Act
        with self.assertRaises(TypeError) as context:
            quit_app()
        self.assertEqual("quit_app() missing 1 required positional argument: 'project_manager'", str(context.exception))


if __name__ == '__main__':
    unittest.main()
