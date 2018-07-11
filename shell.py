import core


def get_choice():
    while True:
        choice = input('''
        1...Attack
        2...Pass
        3...Heal
        4...Quit
        ??? >>> ''').strip()
        if choice == '1':
            return 'Attack'
        elif choice == '2':
            return 'Pass'
        if choice == '3':
            return 'Heal'
        if choice == '4':
            return 'Quit'
        else:
            print('invalid input')


def show_classes():
    'Assassin' = new_gladiator(150, 0, 5, 25)
    'Barbarian' = new_gladiator(300, 50, 15, 25)
    'Samurai' = new_gladiator(200, 0, 15, 35)
    'Archer' = new_gladiator(200, 25, 20, 25)
    'White Mage' = new_gladiator(220, 22, 15, 20)
    'Dovakiin' = new_gladiator(400, 50, 25, 50)
    'Black Mage' = new_gladiator(250, 30, 15, 30)
    class_choice = ['Assassin', 'Barbarian', 'Samurai', 'Archer', 
    'White Mage', 'Dovakiin', 'Black Mage']

def choose_class():
    if user_a


def show_weapons():
    'Deadric Dagger' 
    'Leviathan Axe'
    'Meteorite Katana'
    "Auriel's Bow"
    'Mythril Staff'
    'Mehrunes Razor'
    'Materia'
    weapon_choice = ['Deadric Dagger', 'Leviathan', 'Meteorite Katana', 
    "Auriel's Bow", 'Mythril Staff', 'Mehrunes Razor', 'Materia']

def show_gladiators(attacker, defender):
    print('''ATTACKER: {}, Health: {}, Rage: {}
    DEFENDER: {}, Health: {}, Rage: {}'''
          .format(attacker['name'], attacker['health'], attacker['rage'],
                  defender['name'], defender['health'], defender['rage']))


def battle(name_1, gladiator_1, name_2, gladiator_2):
    while True:
        if is_dead(gladiator_1) == True:
            print(name_2.upper(), 'Wins... Fatality!')
            break
            exit()

        if is_dead(gladiator_2) == True:
            print(name_1.upper(), 'Wins... Fatality!')
            break
            exit()


def main():
    name_1 = input('Name your fighter Player 1. ')
    gladiator_1 = core.new_gladiator(name_1, 100, 10, 15, 25)
    print('Welcome to Mortal Kombat,', (name_1))

    name_2 = input('Name your fighter Player 2. ')
    gladiator_2 = core.new_gladiator(name_2, 100, 10, 15, 25)
    print('Welcome to Mortal Kombat,', (name_2))

    while not (core.is_dead(gladiator_1) or core.is_dead(gladiator_2)):
        show_gladiators(gladiator_1, gladiator_2)
        player_1_choice = get_choice()
        if player_1_choice == 'Attack':
            print(gladiator_1['name'], 'ATTACKS!')
            core.attack(gladiator_1, gladiator_2)
        elif player_1_choice == 'Pass':
            print(gladiator_1['name'], 'Passes!')
        elif player_1_choice == 'Heal':
            print(gladiator_1['name'], 'Heals!')
            core.heal(gladiator_1)
        elif player_1_choice == 'Quit':
            print(gladiator_2['name'], 'Wins... Quitality.')
            exit()

        show_gladiators(gladiator_2, gladiator_1)
        player_2_choice = get_choice()
        if player_2_choice == 'Attack':
            print(gladiator_2['name'], 'ATTACKS!')
            core.attack(gladiator_2, gladiator_1)
        elif player_2_choice == 'Pass':
            print(gladiator_2['name'], 'Passes!')
        elif player_2_choice == 'Heal':
            print(gladiator_2['name'], 'Heals!')
            core.heal(gladiator_2)
        elif player_2_choice == 'Quit':
            print(gladiator_1['name'], 'Wins... Quitality.')
            exit()


if __name__ == '__main__':
    main()
