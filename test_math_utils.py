import pytest
from MathUtils import MathUtils
from tests_data import TestsData


class TestMathUtils:
    test_case = 0

    def setup_method(self, method):
        print(f"\nSetting up the resources for the method: {method.__name__}")

    def teardown_method(self):
        TestMathUtils.test_case += 1
        print(f"\nTest case {TestMathUtils.test_case} completed")

    # Addition
    @pytest.mark.parametrize("a, b, result", TestsData.testDataAddition)
    def test_add(self, a, b, result):
        print(f"Adding two numbers: {a} + {b}; Expected result: {result}")
        assert MathUtils.add(a, b) == result

    # Subtraction
    @pytest.mark.parametrize("a, b, result", TestsData.testDataSubtraction)
    def test_subtract(self, a, b, result):
        print(f"Subtracting two numbers: {a} - {b}; Expected result: {result}")
        assert MathUtils.subtract(a, b) == result

    # Multiplication
    @pytest.mark.parametrize("a, b, result", TestsData.testDataMultiplication)
    def test_multiply(self, a, b, result):
        print(f"Multiplying two numbers: {a} * {b}; Expected result: {result}")
        assert MathUtils.multiply(a, b) == result

    # Division
    @pytest.mark.parametrize("a, b, result", TestsData.testDataDivision)
    def test_divide(self, a, b, result):
        print(f"Dividing two numbers: {a} / {b}; Expected result: {result}")
        assert MathUtils.divide(a, b) == result
