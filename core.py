from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    '''(dict, dict, num, num) -> dict '''
    gladiator = {'Health': 100, 'rage': 0, 'damage_low': 5, 'damage_high': 15}
    return gladiator


def attack(attacker, defender):
    crit_change = randint(0, 100)
    attack = randint(attacker['damage_low'], attacker['damage_high'])
    if crit_change <= attacker['rage']:
        crit_attack = attack * 2
        attacker['rage'] = attacker['rage'] * 0
        damage_dealt = defender['Health'] - crit_attack
        return defender['Health']
    else:
        attacker['rage'] = attacker['rage'] + 15
    defender['Health'] = defender['Health'] - attack
    return defender['Health']


def heal(gladiator):
    if gladiator['rage'] > 10 and gladiator['Health'] <= 95:
        gladiator['rage'] = gladiator['rage'] - 10
        gladiator['Health'] = gladiator['Health'] + 5
        return gladiator['Health']
    else:
        return None


def is_dead(gladiator):
    if gladiator['Health'] == 0:
        return True
