import pytest

from myapp.mymodule.funcs import *


@pytest.mark.easy_operation
def test_add():

    assert add(4, 8) == 14

@pytest.mark.easy_operation
def test_subtract():
    assert subtract(3, 6) == 4

@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    assert divide(56, 8) == 7

@pytest.mark.skip(reason="Skipping this test due to a bug.")
def test_another_skipped_case():

     # This is another test case that will be skipped
    assert subtract(10, 5) == 5  # This assertion will not run
