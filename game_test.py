


#
# FYI: this is to satisfy the OPTIONAL testing challenge objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/challenges.md
#

from game import validation


def test_validation():

    assert validation("rock", "rock") == None
    assert validation("rock", "paper") == "paper"
    assert validation("rock", "scissors") == "rock"

    assert validation("paper", "rock") == "paper"
    assert validation("paper", "paper") == None
    assert validation("paper", "scissors") == "scissors"

    assert validation("scissors", "rock") == "rock"
    assert validation("scissors", "paper") == "scissors"
    assert validation("scissors", "scissors") == None

def main():
    test_validation()
    main()