from wordle import score_guess


def test_happy_path():
    assert score_guess("barge", "brave") == ["green", "yellow", "yellow", "gray", "green"]


def test_duplicate_letter_in_guess():
    assert score_guess("aroma", "amber") == ["green", "yellow", "gray", "yellow", "gray"]
