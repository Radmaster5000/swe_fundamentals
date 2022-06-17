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


class ProjectStartDateError(ProjectError):
    pass


class ProjectLastModifiedError(ProjectError):
    pass


class ProjectLanguagesError(ProjectError):
    pass


class ProjectContributorsError(ProjectError):
    pass


class ProjectLinkError(ProjectError):
    pass

