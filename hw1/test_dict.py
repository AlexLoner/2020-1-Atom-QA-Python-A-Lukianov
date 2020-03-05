''' Module for testing 5 properties of python Set instance '''
import pytest


@pytest.fixture()
def element():
    """Return constant dictionary for futher testing"""
    return {'vector': [1, 5, 10],
            'integer': 45,
            'set': set([45, '123', 'ad']),
            'dict': {}}


# ------------------------------------------------
def test1(element):
    """Check 'something' is a direct or inherited instance of dict class"""
    assert isinstance(element, dict)


# ------------------------------------------------
class Test:
    '''Class for test possible properties of dict instance'''

    # ------------------------------------------------
    def test2(self, element):
        """Check len method"""
        assert len(element) >= 0

    # ------------------------------------------------
    def test3(self, element):
        """Check unhashable key"""
        with pytest.raises(TypeError):
            assert element[list()]

    # ------------------------------------------------
    def test4(self, element):
        """Check '+' operand """
        with pytest.raises(TypeError):
            assert element + element


# ------------------------------------------------
attr_lst = ['keys', 'values', 'update', 'items', 'get']


@pytest.mark.parametrize("value", attr_lst)
def test5(value, element):
    """Check dict attributes on element instance"""
    assert hasattr(element, value)