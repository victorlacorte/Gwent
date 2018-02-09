from gwent.game_mechanics import duel


def test_duel():
    assert duel(1, 20) == 2
    assert duel(2, 1) == 1
    assert duel(2, 2) == 2
    assert duel(7, 10) == 13
    assert duel(7, 11) == 16
