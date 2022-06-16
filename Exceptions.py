class UIError(Exception):
    pass


class UIInputError(UIError):
    pass


class ProjectError(Exception):
    pass


class ProjectNameError(ProjectError):
    pass


class ProjectVersionError(ProjectError):
    pass


class ProjectDescriptionError(ProjectError):
    pass