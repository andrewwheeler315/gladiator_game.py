from core import *


def test_new_gladiator():
    result = new_gladiator(100, 0, 5, 15) 
     gladiator = {'Health': 100, 'Rage': 0, 'damage_low': 5, 'damage_high': 15}

def test_attack():
    gladiator_a = new_gladiator(100, 0, 5, 15)
    gladiator_b = new_gladiator(100, 15, 5, 15)
    
    result = attack(gladiator_a, gladiator_b)
    assert result == gladiator_b['Health']

def test_heal():
    


def test_is_dead():
    if gladiator['Health'] == 0:
        print('You are Dead')
