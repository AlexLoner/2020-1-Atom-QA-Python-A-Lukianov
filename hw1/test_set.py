''' Module for testing 5 properties of python Set instance '''

import pytest

@pytest.fixture()
def element():
    """Return constant set for futher testing"""
    return set(['dfa', 190, 1, 'pwqr'])


# ------------------------------------------------
def test1(element):
    """Check 'something' is a direct or inherited instance of set class"""
    assert isinstance(element, set)


# ------------------------------------------------
class Test:
    '''Class for test possible properties of set instance'''

    # ------------------------------------------------
    def test2(self, element):
        """Check slices not allowed"""
        with pytest.raises(TypeError):
            assert element[:]

    # ------------------------------------------------
    def test3(self, element):
        """Check len method"""
        assert len(element) >= 0

    # ------------------------------------------------
    def test4(self, element):
        """Check '+' operand """
        with pytest.raises(TypeError):
            assert element + element


# ------------------------------------------------
attr_lst = ['intersection', 'union', 'add', 'issubset']


@pytest.mark.parametrize("value", attr_lst)
def test5(value, element):
    """Check set attributes on element instance"""
    assert hasattr(element, value)
