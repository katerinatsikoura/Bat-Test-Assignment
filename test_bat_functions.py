# test_bat_functions.py

import pytest
from unittest.mock import patch
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle, fetch_joker_info

# Exercise 1: Basic tests for calculate_bat_power & parametrized tests for signal_strength

def test_calculate_bat_power():
    # Test with a positive level
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(5) == 210

    # Test with level 0
    assert calculate_bat_power(0) == 0

    # Test with a negative level
    assert calculate_bat_power(-3) == -126

@pytest.mark.parametrize("distance ,expected", [
    (0, 100), 
    (5, 50), 
    (10, 0), 
    (12, 0) # should not go below 0
    ])

def test_signal_strength(distance, expected):
    assert signal_strength(distance) == expected

