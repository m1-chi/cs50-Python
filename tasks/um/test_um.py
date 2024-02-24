from um import count
import pytest


def test_correct_working():
    assert count("um, what's your name?") == 1

def test_um_in_word():
    assert count("album") == 0

def test_casesensitive():
    assert count("yeah, Um, no...") == 1


def test_space():
    assert count(" um ") == 1
