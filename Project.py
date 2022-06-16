from Exceptions import *


class Project:
    """
    A class to create Project objects that contain all the required information
    """

    def __init__(self, name='Example', version=0.0, description='Default description',
                 start_date='2022-01-01', last_modified='2022-01-01', languages=['None'],
                 contributors=['None'], link='http://www.arm.com'):
        self.name = name
        self.version = version
        self.description = description
        self.start_date = start_date
        self.last_modified = last_modified
        self.languages = languages
        self.contributors = contributors
        self.link = link

    def __str__(self):
        return f"Project {self.name}, Version {self.version}, Description: {self.description}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) == 0 or len(name) > 10:
            raise ProjectNameError('Project name must be between 1 and 10 characters')
        self._name = name

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        if not isinstance(version, float):
            raise ProjectVersionError('Version must be of type: float')
        self._version = version
