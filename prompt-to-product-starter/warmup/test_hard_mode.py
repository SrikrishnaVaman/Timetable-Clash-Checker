"""Your tests for is_valid_hard_mode. Write them BEFORE prompting for code.

Remove the skip marker below when you start.
"""
import pytest

from hard_mode import is_valid_hard_mode
from wordle import score_guess

pytestmark = pytest.mark.skip(reason="warm-up not started yet")


def test_green_letter_must_stay_in_place():
    history = [("barge", score_guess("barge", "brave"))]
    assert is_valid_hard_mode("brave", history) is True
    assert is_valid_hard_mode("grace", history) is False  # 'b' not in position 1


# Add your own tests here. Think about repeated letters, and about a yellow
# letter that later turns green.
