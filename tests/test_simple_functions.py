import pytest

from simple_functions import my_sum, factorial


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize("input, expected", [
        (0, 1),
        (3, 6)
    ])
    def test_my_factorial(self, input, expected):
        """Test my factorial function"""
        facs = factorial(input)
        print(facs)
        assert facs == expected
