# L6_L7_64 — Bowling Alley

# Lab 6: Code and Branch Coverage

## About

A Python module that prices bowling lane bookings, scores a single bowling frame including strikes and spares, and assigns parties to bowling lanes.

The objective of Lab 6 is to develop test cases that achieve at least 90% code coverage and branch coverage using `pytest` and `coverage.py`.

## Project Files

| File | Description |
|---|---|
| `bowling_alley.py` | Application module under test |
| `test_bowling_alley.py` | Expanded test suite for the bowling alley application |
| `CodeCoverageTest_bowling_alley.py` | Test cases for code coverage |
| `BranchCoverageTest_bowling_alley.py` | Test cases targeting conditional branches |
| `screenshots/` | Screenshots showing test execution and coverage results |

## Testing Tools

- Python 3.11.9
- pytest 9.0.2
- coverage.py 7.17.3

## Test Execution

Run the expanded test suite:

```bash
python -m pytest test_bowling_alley.py -v
```

Run code coverage tests:

```bash
python -m coverage erase
python -m coverage run --branch -m pytest CodeCoverageTest_bowling_alley.py
python -m coverage report -m
```

Run branch coverage tests:

```bash
python -m coverage erase
python -m coverage run --branch -m pytest BranchCoverageTest_bowling_alley.py
python -m coverage report -m
```

## Results

| Test Suite | Tests Passed | Application Coverage |
|---|---:|---:|
| Expanded test suite | 21 | 100% |
| Code coverage suite | 15 | 100% |
| Branch coverage suite | 23 | 100% |

**Final application coverage:**
- Statements covered: 35/35
- Branches covered: 26/26
- Missed statements: 0
- Partial branches: 0
- Total coverage: 100%

## Screenshots

The `screenshots/` directory contains:

1. `01_initial_coverage.png` — Initial coverage results.
2. `02_final_pytest.png` — Expanded test suite execution.
3. `03_final_coverage.png` — Final coverage results.
4. `04_code_coverage_stage.png` — Code coverage test results.
5. `05_branch_coverage_stage.png` — Branch coverage test results.

## Git Commits

The Lab 6 work was committed in three stages:

1. `Add Lab 6 code coverage test cases`
2. `Add Lab 6 branch coverage test cases`
3. `Add Lab 6 test coverage evidence`

## Submission

All Lab 6 implementation, test files, and screenshot evidence are maintained in this `LAB6` directory.

Refer to the official lab handout for the complete requirements.