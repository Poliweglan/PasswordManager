class Error(Exception):
    """Bazowe zwroty błędów"""
    ...


class EmptyUserInputError(Exception):
    """User just press enter, given '' """
    ...


class StringUserInputError(Exception):
    """User input string, must be int"""
    ...


class ToHighUserOptionError(Exception):
    """User give to high int value"""
    ...


class ToLowUserOptionError(Exception):
    """User give to low int value"""
    ...


class AllDataIsNoneError(Exception):
    """if all data is None: name==None, login==None and pass==None"""
    ...


class AddProfileEmptyError(Exception):
    """When give name, login, password is empty input"""
    ...
