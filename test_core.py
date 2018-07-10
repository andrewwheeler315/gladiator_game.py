from core import *


def test_new_gladiator():
    result = new_gladiator(100, 0, 5, 15)
    assert result == {
        'Health': 100,
        'rage': 0,
        'damage_low': 5,
        'damage_high': 15
    }


def test_attack():
    gladiator_a = new_gladiator(75, 0, 5, 15)
    gladiator_b = new_gladiator(100, 15, 5, 15)
    result = attack(gladiator_a, gladiator_b)
    assert result == gladiator_b['Health']


def test_heal():
    gladiator_a = new_gladiator(75, 0, 15, 30)
    result = heal(gladiator_a)
    assert result == None


def test_is_dead():
    assert is_dead({
        'Health': 0,
        'rage': 30,
        'damage_low': 70,
        'damage_high': 80
    }) == True
