def encryption(value, start=5) -> str:
    """
    :param value: value to encrypt.
    :param start: how far
    :return: encrypt value
    """

    return ''.join([chr(ord(x) + start) for x in value])


def decryption(value, start=5) -> str:
    """
    :param value: value to decrypt.
    :param start: how far
    :return: decrypt value
    """
    return ''.join([chr(ord(x) - start) for x in value])
