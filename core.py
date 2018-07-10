from random import randint


def new_gladiator(name, health, rage, damage_low, damage_high):
    '''(dict, dict, num, num) -> dict '''
    gladiator = {
        'name': name,
        'health': 100,
        'rage': 0,
        'damage_low': 5,
        'damage_high': 15
    }
    return gladiator


def attack(attacker, defender):
    crit_change = randint(0, 100)
    attack = randint(attacker['damage_low'], attacker['damage_high'])
    if crit_change <= attacker['rage']:
        crit_attack = attack * 2
        attacker['rage'] = attacker['rage'] * 0
        damage_dealt = defender['health'] - attack
        crit_damage_dealt = defender['health'] - crit_attack
        return defender['health']
    else:
        attacker['rage'] = attacker['rage'] + 15
    defender['health'] = defender['health'] - attack
    return defender['health']


def heal(gladiator):
    if gladiator['rage'] > 10 and gladiator['health'] <= 95:
        gladiator['rage'] = gladiator['rage'] - 10
        gladiator['health'] = gladiator['health'] + 5
        return gladiator['health']
    else:
        return None


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
