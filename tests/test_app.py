import pytest
from myapp.app import multiply_by_two, divide_by_two

@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a, b]

class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    @pytest.mark.skip(reason="Skipping this test for demonstration purposes.")
    def test_skipped_case(self, numbers):
        # This test will be skipped
        assert multiply_by_two(numbers[0]) == 100  # This assertion will not run
