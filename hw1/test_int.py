''' Module for testing 5 properties of python List instance '''

import random
import pytest


@pytest.fixture(scope='session')
def element():
    '''Return random number for testing'''
    return random.randint(-10, 10)


# ------------------------------------------------
def test1(element):
    """Check 'something' is a direct or inherited instance of int class"""
    assert isinstance(element, int)


# ------------------------------------------------
class Test(object):
    '''Class for test possible properties of int instance'''

    # ------------------------------------------------
    def test2(self, element):
        """Check slices not allowed"""
        with pytest.raises(TypeError):
            assert element[:]

    # ------------------------------------------------
    def test3(self, element):
        """Check convert to imaginary representation"""
        assert complex(element).imag == 0

    # ------------------------------------------------
    def test4(self, element):
        """Check abs method"""
        assert abs(element) == element or abs(element) == -element


# ------------------------------------------------
attr_lst = ['bit_length', 'as_integer_ratio', 'to_bytes']


@pytest.mark.parametrize("value", attr_lst)
def test5(value, element):
    """Check int attributes on element instance"""
    assert hasattr(element, value)
