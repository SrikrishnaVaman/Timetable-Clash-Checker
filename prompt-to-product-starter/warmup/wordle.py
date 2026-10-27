"""Wordle guess scorer, corrected.

Each letter of the answer can be matched at most once. Greens are assigned
first, then yellows from the letters that remain.
"""


def score_guess(guess: str, answer: str) -> list[str]:
    result = ["gray"] * len(guess)
    remaining = list(answer)

    for i, letter in enumerate(guess):          # pass 1: greens
        if letter == answer[i]:
            result[i] = "green"
            remaining[i] = None

    for i, letter in enumerate(guess):          # pass 2: yellows
        if result[i] == "gray" and letter in remaining:
            result[i] = "yellow"
            remaining[remaining.index(letter)] = None

    return result
