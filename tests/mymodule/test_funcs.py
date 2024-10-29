import pytest
from myapp.mymodule.funcs import *

@pytest.mark.easy_operation
def test_add():
    # This test will fail.
    assert add(4, 8) == 14

@pytest.mark.easy_operation
def test_subtract():
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    # This test will be skipped for demonstration purposes.
    pytest.skip("Skipping multiplication test due to known issue.")
    assert multiply(4, 5) == 20  # This assertion will not run

@pytest.mark.difficult_operation
def test_divide():
    assert divide(56, 8) == 7

@pytest.mark.skip(reason="Skipping this test for demonstration purposes.")
def test_skipped_case():
    # This test will be skipped
    assert add(10, 20) == 30  # This assertion will not run
