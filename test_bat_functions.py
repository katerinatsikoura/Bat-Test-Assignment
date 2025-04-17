# test_bat_functions.py

import pytest
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

# Exercise 2: Tests using fixtures for get_bat_vehicle

# Fixture that returns a reusable dictionary of known Bat vehicles
@pytest.fixture
def bat_vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle_known(bat_vehicles):
    # Test known vehicles
    assert get_bat_vehicle('Batmobile') == bat_vehicles['Batmobile']
    assert get_bat_vehicle('Batwing') == bat_vehicles['Batwing']
    assert get_bat_vehicle('Batcycle') == bat_vehicles['Batcycle']

def test_get_bat_vehicle_unknown():
    # Test unknown vehicle
    with pytest.raises(ValueError, match="Unknown vehicle: Batplane"):
        get_bat_vehicle('Batplane')

# Exercise 3: Mocking for fetch_joker_info

def test_fetch_joker_info(mocker):
    # Mock the time.sleep function to avoid the delay
    mocker.patch("bat_functions.time.sleep", return_value=None)

    # Mock fetch_joker_info to return a custom dictionary
    mock_response = {'mischief_level': 0, 'location': 'captured'}
    mock_fetch = mocker.patch("bat_functions.fetch_joker_info", return_value=mock_response)

    # Call the function (returns the mocked data)
    result = fetch_joker_info()

     # Assert that the returned result is the mocked dictionary
    assert result == {'mischief_level': 0, 'location': 'captured'}

    # Verify fetch_joker_info was called exactly once
    mock_fetch.assert_called_once()
    