''' Module for testing 5 properties of python List instance '''
import random
import string
import pytest


@pytest.fixture(scope='session')
def element():
    '''Return random string with length k for testing'''
    my_str = ''.join(random.choices(string.ascii_letters, k=random.randint(0, 10)))
    return my_str


# ------------------------------------------------
def test1(element):
    """Check 'something' is a direct or inherited instance of str class"""
    assert isinstance(element, str)


# ------------------------------------------------
class Test:
    '''Class for test possible properties of str instance'''

    # ------------------------------------------------
    def test2(self, element):
        """Check slices"""
        assert element[:] or element[:] == ''

    # ------------------------------------------------
    def test3(self, element):
        """Check len method"""
        assert len(element) >= 0

    # ------------------------------------------------
    def test4(self, element):
        """Check unmutable property"""
        with pytest.raises(TypeError):
            if len(element) == 0:
                element += '0'
            element[0] = 'h'


# ------------------------------------------------
attr_lst = ['upper', 'title', 'isdigit', 'startswith', 'split', 'strip']


@pytest.mark.parametrize("value", attr_lst)
def test5(value, element):
    """Check str attributes on element instance"""
    assert hasattr(element, value)
