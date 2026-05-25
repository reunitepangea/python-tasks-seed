"""
Unit tests for 02.Base85

TODO: Add more tests!
"""

import base85ed
import random
import base64
import pytest

def test_shorts_encode():
    """
    Test trivial short encodes
    """
    assert base85ed.encode(b"1") == b"F#"
    assert base85ed.encode(b"12") == b"F){"
    assert base85ed.encode(b"123") == b"F)}j"
    assert base85ed.encode(b"1234") == b"F)}kW"

def test_empty_encode():
    assert base85ed.encode(b"") == b""

def test_multiple_to_4_encode():
    data = [random.randint(0, 255) for i in range(1024)]
    data = bytes(data)
    assert base85ed.encode(data) == base64.b85encode(data)

def test_not_multiple_to_4_encode():
    data = [random.randint(0, 255) for i in range(1025)]
    data = bytes(data)
    assert base85ed.encode(data) == base64.b85encode(data)

def test_fatal_array_encode():
    data = [random.randint(0, 255) for i in range(3*(10**6))]
    data = bytes(data)
    assert base85ed.encode(data) == base64.b85encode(data)

def test_max_bytes_encode():
    data4 = [255 for i in range(1024)]
    data4 = bytes(data4)
    assert base85ed.encode(data4) == base64.b85encode(data4)
    datanot4 = [255 for i in range(1025)]
    datanot4 = bytes(datanot4)
    assert base85ed.encode(datanot4) == base64.b85encode(datanot4)

def test_shorts_decode():
    """
    Test trivial short decodes
    """
    assert base85ed.decode(b"F#") == b"1"
    assert base85ed.decode(b"F){") == b"12"
    assert base85ed.decode(b"F)}j") == b"123"
    assert base85ed.decode(b"F)}kW") == b"1234"

def test_empty_decode():
    assert base85ed.decode(b"") == b""

def test_multiple_to_5_decode():
    data = [random.randint(0, 255) for i in range(1025)]
    data = bytes(data)
    data = base64.b85encode(data)
    assert base85ed.decode(data) == base64.b85decode(data)

def test_not_multiple_to_5_decode():
    data = [random.randint(0, 255) for i in range(1024)]
    data = bytes(data)
    data = base64.b85encode(data)
    assert base85ed.decode(data) == base64.b85decode(data)

def test_fatal_array_decode():
    data = [random.randint(0, 255) for i in range(3*(10**6))]
    data = bytes(data)
    data = base64.b85encode(data)
    assert base85ed.decode(data) == base64.b85decode(data)

def test_unacceptable_decode():
    data = "привет".encode()
    with pytest.raises(ValueError):
        base85ed.decode(data)

def tests_invertibility():
    data1 = [random.randint(0, 255) for i in range(1025)]
    data1 = bytes(data1)
    data2 = [random.randint(0, 255) for i in range(1024)]
    data2 = bytes(data2)
    assert base85ed.decode(base85ed.encode(data1)) == data1
    assert base85ed.decode(base85ed.encode(data2)) == data2
