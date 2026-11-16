import pytest
from bowling_alley import lane_cost, frame_score, lane_assignment

def test_weekday_booking():
    assert lane_cost("weekday", 2, 4, 2, False) == 900

def test_weekend_booking():
    assert lane_cost("weekend", 2, 4, 0, False) == 1200

def test_extra_players():
    assert lane_cost("weekday", 2, 5, 0, False) == 1000

def test_league_member_discount():
    assert lane_cost("weekday", 1, 4, 0, True) == 320

def test_unknown_day_type():
    with pytest.raises(ValueError, match="unknown day type"):
        lane_cost("holiday", 1, 2, 0, False)

@pytest.mark.parametrize("games, players", [(0, 2), (1, 0), (1, 7)])
def test_invalid_booking(games, players):
    with pytest.raises(ValueError, match="invalid booking"):
        lane_cost("weekday", games, players, 0, False)

def test_too_many_shoe_rentals():
    with pytest.raises(ValueError, match="too many shoe rentals"):
        lane_cost("weekday", 1, 2, 3, False)

def test_open_frame():
    assert frame_score(3, 4, []) == 7

def test_strike():
    assert frame_score(10, 0, [5, 3]) == 18

def test_spare():
    assert frame_score(6, 4, [5]) == 15

def test_invalid_negative_first_roll():
    with pytest.raises(ValueError, match="invalid roll"):
        frame_score(-1, 2, [])

def test_invalid_first_roll_above_ten():
    with pytest.raises(ValueError, match="invalid roll"):
        frame_score(11, 0, [])

def test_invalid_negative_second_roll():
    with pytest.raises(ValueError, match="invalid roll"):
        frame_score(5, -1, [])

def test_invalid_frame_total():
    with pytest.raises(ValueError, match="invalid frame"):
        frame_score(7, 5, [])

def test_no_lanes_available():
    assert lane_assignment(4, False, 0) == "wait"

def test_bumper_lane_for_children():
    assert lane_assignment(4, True, 2) == "bumper lane"

def test_two_lanes_for_large_group():
    assert lane_assignment(8, False, 2) == "two lanes"

def test_wait_for_large_group():
    assert lane_assignment(8, False, 1) == "wait"

def test_standard_lane():
    assert lane_assignment(4, False, 2) == "standard lane"