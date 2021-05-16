import pytest
import palindrone


# Correct working case for option 1
def test_palind_1(self):
    temp = "Racecar"
    ans = palindrone.palind(temp)
    assert ans == True

# Correct working case for option 2
def test_palind_2(self):
    temp = "car"
    ans = palindrone.palind(temp)
    assert ans == False

# Fail case
def test_palind_3(self):
    temp = "fail"
    ans = palindrone.palind(temp)
    assert ans == True