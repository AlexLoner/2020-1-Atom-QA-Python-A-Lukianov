''' Module for testing 5 properties of python List instance '''
import pytest


@pytest.fixture()
def element():
    """Return constant list for futher testing"""
    return ['dfa', 190, [[10]], {0, 23, 1}]

# ------------------------------------------------
def test1(element):
    """Check 'something' is a direct or inherited instance of list class"""
    assert isinstance(element, list)

# ------------------------------------------------
class Test:
    '''Class for test possible properties of list instance'''

    # ------------------------------------------------
    def test2(self, element):
        """Check that lists can't be multiplied by non-int"""
        with pytest.raises(TypeError):
            assert element * element

    # ------------------------------------------------
    def test3(self, element):
        """Check len method"""
        assert len(element) >= 0

    # ------------------------------------------------
    def test4(self, element):
        """Check mutable property"""
        try:
            element[-1] = 100

        except TypeError:
            raise


# ------------------------------------------------
attr_lst = ['copy', 'append', 'count', 'extend']


@pytest.mark.parametrize("value", attr_lst)
def test5(value, element):
    """Check list attributes on element instance"""
    assert hasattr(element, value)
