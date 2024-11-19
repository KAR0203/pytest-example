import pytest
from myapp.mymodule.funcs import *

# Custom marker for regression tests
@pytest.mark.regression
@pytest.mark.easy_operation
def test_add():
    # Marked as both easy_operation and regression
    assert add(4, 8) == 16

@pytest.mark.regression
@pytest.mark.easy_operation
def test_subtract():
    # Marked as both easy_operation and regression
    assert subtract(3, 6) == -3

@pytest.mark.regression

def test_multiply():
    # Marked as both difficult_operation and regression
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    # Marked as both difficult_operation and regression
    assert divide(56, 8) == 8

@pytest.mark.skip(reason="Skipping this test due to a bug.")
def test_another_skipped_case():
    # This test will be skipped, so it will not be part of the regression suite.
    assert subtract(10, 5) == 8  # This assertion will not run
