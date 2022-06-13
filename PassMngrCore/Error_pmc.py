class Error(Exception):
    """Bazowe zwroty błędów"""
    ...


class EmptyUserInputError(Exception):
    """User just press enter, given '' """
    ...


class StringUserInpuError(Exception):
    """User input string, must be int"""
    ...


class ToHighUserOptionError(Exception):
    """User give to high int value"""
    ...


class ToLowUserOptionError(Exception):
    """User give to low int value"""
    ...