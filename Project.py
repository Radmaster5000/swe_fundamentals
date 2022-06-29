from Exceptions import *
import re


class Project:
    """
    A class to create Project objects that contain all the required information.
    Setters are used to validate the data being inputted. Custom errors are raised if data is invalid and the user is
    prompted to retry.

    Default values are given if the object is created without any inputs, however validation requires the user to
    give inputs for all the fields.
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
        """
        Overview of projects (Used during development)
        """
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
        if len(contributors) <= 0 or (len(contributors) == 1 and contributors[0] == ''):
            raise ProjectContributorsError("Contributors needs at least one person. Like, you!")
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


def create_project():
    """
    Takes input from the user, validating the data as it is inputted. A Project Object is then created using the
    inputted data.

    Returns:
         new_project (Project Object): A completed Project Object that can be added to the Project Manager DataFrame
    """
    _languages = []
    _contributors = []
    _lang = None
    _cont = None

    print("Create your project...")

    attr = False
    while not attr:
        _name = input("\nPlease enter the Project's name: ")
        attr = check_name(_name)

    attr = False
    while not attr:
        try:
            _version = float(input("\nPlease enter the Project's version: "))
        except ValueError:
            _version = ''
            pass
        attr = check_version(_version)

    attr = False
    while not attr:
        _description = input("\nPlease enter the Project's description: ")
        attr = check_description(_description)

    attr = False
    while not attr:
        _start_date = input("\nPlease enter the Project's start date: ")
        attr = check_start_date(_start_date)

    attr = False
    while not attr:
        _last_modified = input("\nPlease enter the Project's last modified date: ")
        attr = check_last_modified(_last_modified)

    while _lang != '':
        attr = False
        while not attr:
            print("\nPress Enter without entering a language to move on")
            _lang = input("Please enter a programming language used in the Project: ")
            if _lang != '':
                _languages.append(_lang)
                attr = check_lang(_languages)
            else:
                attr = True

    while _cont != '':
        attr = False
        while not attr:
            print("\nPress Enter without entering a team member to move on")
            _cont = input("Please enter a team member who worked on the Project: ")
            if _cont != '':
                _contributors.append(_cont)
                attr = check_cont(_contributors)
            else:
                attr = True

    attr = False
    while not attr:
        _link = input("\nPlease enter the link to the Project's repository: ")
        attr = check_link(_link)

    new_project = Project(name=_name, version=_version, description=_description, start_date=_start_date,
                          last_modified=_last_modified, languages=_languages, contributors=_contributors,
                          link=_link)

    return new_project


def check_name(attribute):
    """
    Checks the validity of the given data

    Args:
        attribute (string): Name input from user

    Returns:
        attr (bool): True if given attribute is valid, False otherwise
    """
    attr = True
    try:
        Project(name=attribute)
    except ProjectNameError as error:
        print(error)
        attr = False
    finally:
        return attr


def check_version(attribute):
    """
    Checks the validity of the given data

    Args:
        attribute (string): Version input from user

    Returns:
        attr (bool): True if given attribute is valid, False otherwise
    """
    attr = True
    try:
        Project(version=attribute)
    except ProjectVersionError as error:
        print(error)
        attr = False
    finally:
        return attr


def check_description(attribute):
    """
    Checks the validity of the given data

    Args:
        attribute (string): Description input from user

    Returns:
        attr (bool): True if given attribute is valid, False otherwise
    """
    attr = True
    try:
        Project(description=attribute)
    except ProjectDescriptionError as error:
        print(error)
        attr = False
    finally:
        return attr


def check_start_date(attribute):
    """
    Checks the validity of the given data

    Args:
        attribute (string): Start Date input from user

    Returns:
        attr (bool): True if given attribute is valid, False otherwise
    """
    attr = True
    try:
        Project(start_date=attribute)
    except ProjectStartDateError as error:
        print(error)
        attr = False
    finally:
        return attr


def check_last_modified(attribute):
    """
    Checks the validity of the given data

    Args:
        attribute (string): Last Modified Date input from user

    Returns:
        attr (bool): True if given attribute is valid, False otherwise
    """
    attr = True
    try:
        Project(last_modified=attribute)
    except ProjectLastModifiedError as error:
        print(error)
        attr = False
    finally:
        return attr


def check_lang(attribute):
    """
    Checks the validity of the given data

    Args:
        attribute (string): Programming Language input from user

    Returns:
        attr (bool): True if given attribute is valid, False otherwise
    """
    attr = True
    try:
        Project(languages=attribute)
    except ProjectLanguagesError as error:
        print(error)
        attr = False
    finally:
        return attr


def check_cont(attribute):
    """
    Checks the validity of the given data

    Args:
        attribute (string): Contributor input from user

    Returns:
        attr (bool): True if given attribute is valid, False otherwise
    """
    attr = True
    try:
        Project(contributors=attribute)
    except ProjectContributorsError as error:
        print(error)
        attr = False
    finally:
        return attr


def check_link(attribute):
    """
    Checks the validity of the given data

    Args:
        attribute (string): Hyperlink input from user

    Returns:
        attr (bool): True if given attribute is valid, False otherwise
    """
    attr = True
    try:
        Project(link=attribute)
    except ProjectLinkError as error:
        print(error)
        attr = False
    finally:
        return attr
