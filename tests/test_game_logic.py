from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"


def test_hard_range_harder_than_normal():
    from logic_utils import get_range_for_difficulty
    assert get_range_for_difficulty("Hard")[1] > get_range_for_difficulty("Normal")[1]


def test_hint_direction():
    _, msg = check_guess(60, 50)
    assert "LOWER" in msg
