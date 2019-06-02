from hashlib import md5

_md5 = md5()


def md5sum(content: bytes) -> str:
    """
    :param content:  content to caculate
    :return: md5sum of input content
    """
    _md5.update(content)
    return _md5.hexdigest()
