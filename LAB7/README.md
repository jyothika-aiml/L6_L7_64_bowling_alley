# L6_L7_64 — Bowling Alley

## Lab 7: Fuzzing for Input Validation Bugs

### About

This lab uses Python's Hypothesis library for property-based fuzz testing to identify input validation bugs in a Bowling Alley Parser application.

Hypothesis generates unexpected and malformed inputs to test the application's robustness. The discovered bugs were fixed by adding input validation and safe handling of invalid data.

### Files

| File | Description |
|---|---|
| `bowling_alley_parser.py` | Fixed Bowling Alley Parser application |
| `test_bowling_alley_parser.py` | Hypothesis tests for all three functions |
| `README.md` | Lab 7 documentation |
| `screenshots/` | Evidence of original bugs, fuzz testing and successful fixes |

### Functions Tested

1. `format_player_name()` — Handles invalid player-name inputs and formats valid names.
2. `parse_frame()` — Handles valid bowling frame notation and safely handles invalid frames.
3. `parse_scoreboard()` — Parses valid player scores and skips malformed entries.

### Bugs Identified and Fixes

| Function | Bugs identified | Fix implemented |
|---|---|---|
| `format_player_name()` | Crashed when input was `None` | Added input type validation |
| `parse_frame()` | Crashed with empty, malformed and invalid frame inputs | Added length, type and pin-count validation |
| `parse_scoreboard()` | Crashed with `None`, empty and malformed entries | Added type checking and safe entry parsing |

### Testing Results

- Hypothesis version: 6.155.5
- Pytest version: 9.0.2
- Total Hypothesis tests: 3
- Tests passed after fixing: 3
- Tests failed after fixing: 0

**Final result: 3 passed in 1.35 seconds.**

### Screenshots

| Screenshot | Description |
|---|---|
| `01_original_application.png` | Original application execution |
| `02_hypothesis_failures.png` | Hypothesis identifying bugs in the original application |
| `03_final_hypothesis_tests.png` | All three Hypothesis tests passing after fixes |
| `04_fixed_application.png` | Successful execution of the corrected application |

### Deliverables

1. `bowling_alley_parser.py` — Fixed application.
2. `test_bowling_alley_parser.py` — Completed Hypothesis tests.
3. `SRN_NAME_LAB7.pdf` — Lab screenshots and answers to the reflection questions from the handout.

### Conclusion

Hypothesis fuzz testing successfully identified input validation bugs in all three functions. After implementing defensive input validation and safe error handling, all three property-based tests passed, demonstrating improved robustness against unexpected inputs.