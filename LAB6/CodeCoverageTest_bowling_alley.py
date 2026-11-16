
import pytest
from bowling_alley import lane_cost, frame_score, lane_assignment


# CODE COVERAGE TESTS

def test_weekday_booking():
    assert lane_cost("weekday", 2, 4, 2, False) == 900


def test_weekend_large_booking_with_discount():
    assert lane_cost("weekend", 2, 5, 1, True) == 1160


def test_unknown_day():
    with pytest.raises(ValueError):
        lane_cost("holiday", 1, 2, 0, False)


def test_invalid_booking():
    with pytest.raises(ValueError):
        lane_cost("weekday", 0, 2, 0, False)


def test_excessive_shoe_rentals():
    with pytest.raises(ValueError):
        lane_cost("weekday", 1, 2, 3, False)


def test_strike():
    assert frame_score(10, 0, [5, 3]) == 18


def test_spare():
    assert frame_score(6, 4, [5]) == 15


def test_open_frame():
    assert frame_score(3, 4, []) == 7


def test_invalid_roll():
    with pytest.raises(ValueError):
        frame_score(-1, 2, [])


def test_invalid_frame():
    with pytest.raises(ValueError):
        frame_score(7, 5, [])


def test_no_lanes():
    assert lane_assignment(4, False, 0) == "wait"


def test_bumper_lane():
    assert lane_assignment(4, True, 2) == "bumper lane"


def test_two_lanes():
    assert lane_assignment(8, False, 2) == "two lanes"


def test_large_group_wait():
    assert lane_assignment(8, False, 1) == "wait"


def test_standard_lane():
    assert lane_assignment(4, False, 2) == "standard lane"
