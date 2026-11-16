import pytest
from bowling_alley import lane_cost, frame_score, lane_assignment


# BRANCH COVERAGE TESTS

# lane_cost() branches
def test_weekday_branch():
    assert lane_cost("weekday", 1, 4, 0, False) == 400


def test_weekend_branch():
    assert lane_cost("weekend", 1, 4, 0, False) == 600


def test_unknown_day_branch():
    with pytest.raises(ValueError):
        lane_cost("holiday", 1, 2, 0, False)


def test_invalid_games_branch():
    with pytest.raises(ValueError):
        lane_cost("weekday", 0, 2, 0, False)


def test_invalid_players_branch():
    with pytest.raises(ValueError):
        lane_cost("weekday", 1, 0, 0, False)


def test_more_than_six_players_branch():
    with pytest.raises(ValueError):
        lane_cost("weekday", 1, 7, 0, False)


def test_extra_player_charge_branch():
    assert lane_cost("weekday", 1, 5, 0, False) == 500


def test_no_extra_player_charge_branch():
    assert lane_cost("weekday", 1, 4, 0, False) == 400


def test_too_many_shoes_branch():
    with pytest.raises(ValueError):
        lane_cost("weekday", 1, 2, 3, False)


def test_league_member_branch():
    assert lane_cost("weekday", 1, 4, 0, True) == 320


def test_non_league_member_branch():
    assert lane_cost("weekday", 1, 4, 0, False) == 400


# frame_score() branches
def test_invalid_first_roll_negative():
    with pytest.raises(ValueError):
        frame_score(-1, 0, [])


def test_invalid_first_roll_above_ten():
    with pytest.raises(ValueError):
        frame_score(11, 0, [])


def test_invalid_second_roll():
    with pytest.raises(ValueError):
        frame_score(5, -1, [])


def test_strike_branch():
    assert frame_score(10, 0, [5, 3]) == 18


def test_invalid_frame_branch():
    with pytest.raises(ValueError):
        frame_score(7, 5, [])


def test_spare_branch():
    assert frame_score(6, 4, [5]) == 15


def test_open_frame_branch():
    assert frame_score(3, 4, []) == 7


# lane_assignment() branches
def test_no_lanes_branch():
    assert lane_assignment(4, False, 0) == "wait"


def test_kids_bumper_lane_branch():
    assert lane_assignment(4, True, 2) == "bumper lane"


def test_large_group_two_lanes_branch():
    assert lane_assignment(8, False, 2) == "two lanes"


def test_large_group_wait_branch():
    assert lane_assignment(8, False, 1) == "wait"


def test_standard_lane_branch():
    assert lane_assignment(4, False, 2) == "standard lane"