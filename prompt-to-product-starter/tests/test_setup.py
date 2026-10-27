"""Setup check: if this test passes, your environment works.

Delete this file once your own tests are in place.
"""
from project import setup_check


def test_environment_is_ready():
    assert setup_check() == "ready"
