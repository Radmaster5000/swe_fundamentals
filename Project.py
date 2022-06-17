from Exceptions import *
import re


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

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if len(description) > 150:
            raise ProjectDescriptionError('Description must be less than 150 chars')
        self._description = description

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if not re.match(r"\d\d\d\d-[0-1]\d-[0-3]\d", start_date):
            raise ProjectStartDateError('Start date must be in format YYYY-MM-DD')
        self._start_date = start_date

    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        if not re.match(r"\d\d\d\d-[0-1]\d-[0-3]\d", last_modified):
            raise ProjectLastModifiedError('Last modified date must be in format YYYY-MM-DD')
        self._last_modified = last_modified

    @property
    def languages(self):
        return self._languages

    @languages.setter
    def languages(self, languages):
        for i in languages:
            if type(i) != str:
                raise ProjectLanguagesError("All languages must be of type: 'string'")
        self._languages = languages

    @property
    def contributors(self):
        return self._contributors

    @contributors.setter
    def contributors(self, contributors):
        for i in contributors:
            if type(i) != str:
                raise ProjectContributorsError("All contributors must be of type: 'string'")
        self._contributors = contributors

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        if not re.match(r"(http)(s?)://.+", link):
            raise ProjectLinkError("Link must contain full link, starting with 'http://' or 'https://'")
        self._link = link
