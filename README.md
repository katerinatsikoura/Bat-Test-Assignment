# Bat-Test-Assignment

## Overview
This repository contains unit test examples using 'pytest' for some Batman inspired functions. It serves as an assignment for the "Software Engineering in Practice" course at the Department of Management Science and Technology, Athens University of Economics and Business.

## Tests Written
This repository includes a test suite for the following functions from `bat_functions.py`:

### Exercise 1: Basic Tests & Parametrization
- **Function tested**: `calculate_bat_power(level)`
- **Function tested**: `signal_strength(distance)`
- Used `@pytest.mark.parametrize` to test signal strength with different inputs.

### Exercise 2: Using Fixtures
- Created a fixture for known bat vehicle specs.
- Tested `get_bat_vehicle(vehicle_name)` for both valid and invalid input.

### Exercise 3: Mocking External Dependencies
- Tested `fetch_joker_info()` using `pytest-mock`.
- Mocked:
  - `time.sleep` to skip the 1-second delay.
  - The function return value to simulate a captured Joker.

### Exercise 4: Continuous Integration
- GitHub Actions workflow (`.github/workflows/pytest.yml`) runs tests automatically on:
  - `push`
  - `pull_request`
- Runs tests on **Ubuntu** with **Python 3.9** and **3.10**
- Uses `pytest` with coverage reporting.

## How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/gotham-pytest-assignment.git
cd gotham-pytest-assignment
