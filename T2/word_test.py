import pytest
import wordCount

# Correct working case 1
def test_word_1():
    temp = "This is an activity"
    ans = wordCount.lengthSent(temp)
    assert ans == 4
# Correct working case 2
def test_word_2():
    temp = "Testing a longer senctence than four words long."
    ans = wordCount.lengthSent(temp)
    assert ans == 8
# Fail Case
def test_word_3():
    temp = "Fail case"
    ans = wordCount.lengthSent(temp)
    assert ans == 1
