import pytest
from entities.monster import Monster

def test_save_monster():
    monster = Monster(name="Test Monster", power="Test Power")
    monster_id = monster.save()
    assert monster_id is not None