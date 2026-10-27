"""Warm-up (pairs): Wordle hard mode.

In hard mode, every later guess must use all the hints revealed so far:
green letters must stay in place, and yellow letters must appear somewhere
in the guess.

Order of work:
  1. Write the spec for is_valid_hard_mode in plain English (in this docstring).
  2. Write three tests in test_hard_mode.py that you expect an AI draft to fail.
  3. Only then prompt your AI tool for the code. Run your tests. Commit.

score_guess(guess, answer) in wordle.py is correct and tested; you may use it.
"""

# history: list of (guess, colours) pairs, e.g. [("barge", ["green", "yellow", "yellow", "gray", "green"])]


def is_valid_hard_mode(guess: str, history: list[tuple[str, list[str]]]) -> bool:
    raise NotImplementedError("Write the spec and tests first.")
