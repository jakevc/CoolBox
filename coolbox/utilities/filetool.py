
def opener(filename):
    """
    Determines if a file is compressed or not

    >>> import gzip
    >>> msg = "hello blablabla"
    >>> tmp_f_raw  = open("/tmp/test_opener.txt", 'w')
    >>> tmp_f_raw.write(msg)
    15
    >>> tmp_f_raw.close()
    >>> tmp_f_gzip = gzip.open('/tmp/test_opener.txt.gz', 'wb')
    >>> tmp_f_gzip.write(to_bytes(msg))
    15
    >>> tmp_f_gzip.close()

    >>> test_raw = opener(tmp_f_raw.name)
    >>> type(test_raw)
    <class '_io.BufferedReader'>
    >>> test_gzip = opener(tmp_f_gzip.name)
    >>> type(test_gzip)
    <class 'gzip.GzipFile'>

    >>> test_raw.close()
    >>> test_gzip.close()

    >>> import os
    >>> os.remove(test_raw.name)
    >>> os.remove(test_gzip.name)

    """
    import gzip
    f = open(filename, 'rb')
    if f.read(2) == b'\x1f\x8b':
        f.seek(0)
        return gzip.GzipFile(fileobj=f)
    else:
        f.seek(0)
        return f


def to_string(s):
    """
    Convert bytes, bytes list to string, string list.

    >>> to_string("hello")
    'hello'
    >>> to_string(b"hello")
    'hello'
    >>> to_string([b'hello', b'world'])
    ['hello', 'world']
    """
    if isinstance(s, str):
        return s
    if isinstance(s, bytes):
        return s.decode('ascii')
    if isinstance(s, list):
        return [to_string(x) for x in s]
    return s


def to_bytes(s):
    """
    Like toString, to bytes.

    >>> to_bytes('hello')
    b'hello'
    >>> to_bytes(['hello', 'world'])
    [b'hello', b'world']
    """
    if isinstance(s, bytes):
        return s
    if isinstance(s, str):
        return bytes(s, 'ascii')
    if isinstance(s, list):
        return [to_bytes(x) for x in s]
    return s
