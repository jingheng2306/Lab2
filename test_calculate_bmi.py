import pytest
from bmiexercise1 import calculate_bmi

def test_underweight():
    assert calculate_bmi(weight=50, height=1.7) == -1

def test_normal_weight():
    assert calculate_bmi(weight=70, height=1.75) == 0

def test_overweight():
    assert calculate_bmi(weight=90, height=1.75) == 1

if __name__ == "__main__":
    pytest.main()


