import os
import sys
import random
import time
import datetime


def print_ig_menu():
    print(4 * '\t' + '║' + 22 * '═' + '║')
    print(4 * '\t' + '║' + 9 * '═' + 'MENU' + 9 * '═' + '║')
    print(4 * '\t' + '║' + 22 * ' ' + '║')
    print(4 * '\t' + '║' + 4 * ' ' + '[Back] to game' + 4 * ' ' + '║')
    print(4 * '\t' + '║' + 'Return to [Main] Menu ' + '║')
    print(4 * '\t' + '║' + 3 * ' ' + '[Save] and exit' + 4 * ' ' + '║')
    print(4 * '\t' + '║' + 5 * ' ' + '[Exit] game' + 6 * ' ' + '║')
    print(4 * '\t' + '║' + 22 * '═' + '║')


class Game:
    game_name = '''-
-
████████████████████████████████████████████
█▄─▄▄▀█▄─██─▄█─▄▄▄▄█▄─█─▄█▄─▄▄─█▄─▄▄▀█─▄▄▄▄█
██─██─██─██─██▄▄▄▄─██─▄▀███─▄█▀██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
-
-'''
    robot = '''      ░═███═░
      ░░█╬█░░
      ███████
      █░█░█░█
      █░█░█░█
      ░░███░░
      ░██░██░'''
    player_name = ''
    # menu_commands = ('[Play]', '[High] Scores', '[Help]', '[Exit]')
    menu_commands = ('[New] Game', '[Load] Game', '[High] Scores', '[Help]', '[Exit]')
    ig_locations = []
    locs = []
    titanium = 0
    save_dir = ''
    robots = 3
    titanium_scan = False
    enemy_scan = False

    def __init__(self, seed, animations, locations):
        self.seed = seed
        self.animations = animations
        self.locations = locations

    def print_name(self):
        for line in self.game_name.split('\n'):
            print(line)
            if line != '':
                time.sleep(0.1)

    def print_high_scores(self):
        print('HIGH SCORES\n')
        with open('./high_scores.txt', 'r') as file:
            for n, line in enumerate(file):
                line = line.split(',')
                if line[0] == 'enemy':
                    break
                print(f'({n + 1}) {line[0]} {line[1]}')

        print('\t[Back]')

        while True:
            user_input = input('Your_command:\n').lower()
            if user_input == 'back':
                Game.menu(self)
                break
            else:
                print('Invalid input')

    def menu(self):
        Game.print_name(self)
        for command in Game.menu_commands:
            print(command)
        while True:
            user_input = input('Your command:\n').lower()
            if user_input == 'exit':
                print('Thanks for playing, bye!')
                return
            if user_input == 'play':
                name = input("Enter your name:")
                print(f'Welcome, commander {name}!')
                print("Are you ready to begin?", "[Yes] [No] Return to Main[Menu]", end="\n")
                while True:
                    ready = input("Your command:").lower()
                    if ready == "yes":
                        Game.play_game(self)
                        return
                    elif ready == "menu":
                        Game.menu(self)
                        return
                        # break

            elif user_input == 'new':
                 break
            elif user_input == 'load':
                Game.load_game(self)
                Game.play_game(self)
                return
            elif user_input == 'high':
                # print("No Scores to display", "[back]", end="\n")
                # while True:
                #     cmd = input("Enter your command")
                #     if cmd == "back":
                #         Game.menu(self)
                #         return
                #     else: print("Invalid input")
                Game.print_high_scores(self)
                return
            elif user_input == 'help':
                print('Coming SOON! Thanks for playing!')
                return
            else:
                print('Invalid input!')

        Game.input_name(self)

        while True:
            print('Are you ready to begin?\n[Yes] [No] Return to Main[Menu]')
            play_input = input('Your command:\n').lower()
            if play_input == 'no':
                print('How about now.')
                continue
            elif play_input == 'yes':
                Game.play_game(self)
                return
            elif play_input == 'menu':
                Game.menu(self)
                break
            else:
                print('Invalid input!')

    def input_name(self):
        self.player_name = input('Enter your name:\n')
        print(f'Greetings, commander {self.player_name}')

    def print_board(self):
        print('+' "========" + '+')
        for line in self.robot.split('\n'):
            # print(line + " | " + line + " | " + line)
            print((self.robots - 1) * (line + " | ") + line)
        print('+' "========" + '+')
        print(f'Titanium: {self.titanium}')
        print('+|' + 80 * '═' + '|+')
        print('|' + '[Ex]plore\t\t[Up]grade' + 56 * ' ' + '|')
        print('|' + '[Save]\t\t\t[M]enu' + 59 * ' ' + '|')
        print('+|' + 80 * '═' + '|+')
    def animation(self):
        n = self.animations
        for i in range(n):
            print('.', end='')
            time.sleep(0.02)
        print('\n')

    def print_saves(self):
        print('\tSelect slot:')
        with open(self.save_dir + './save_file.txt', 'r') as file:
            saves = file.read().split('\n')

        for x in range(3):
            print(f'\t[{x + 1}] ', end='')
            if saves[x] == 'empty':
                print(saves[x])
            else:
                f = saves[x].split(';')
                nick = f[0].split(' = ')[1]
                titan = f[1].split(' = ')[1]
                robots = f[2].split(' = ')[1]
                last_save = f[-1].split(' = ')[1]
                print(f'{nick} Titanium: {titan} Robots: {robots} Last save: {last_save}')
        return saves

    def save_game(self):
        while True:
            saves = Game.print_saves(self)
            slot = input('Your command:\n')
            slots = ['1', '2', '3']
            if slot in slots:
                break
            else:
                print('Invalid input!')
                continue

        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M')
        ts = (1 if self.titanium_scan else 0)
        es = (1 if self.enemy_scan else 0)
        saves[int(slot) - 1] = f'nick = {self.player_name};titanium = {self.titanium};robots = {self.robots};' \
                               f'tscan = {ts};escan = {es};Last save = {now} '

        path = self.save_dir + './save_file.txt'
        with open(path, 'w+') as file:
            file.write('\n'.join(saves))
        print('\t║' + 30 * '═' + '║')
        print('\t║' + 3 * ' ' + 'GAME SAVED SUCCESSFULLY' + 4 * ' ' + '║')
        print('\t║' + 30 * '═' + '║')

    def load_game(self):
        while True:
            saves = Game.print_saves(self)
            slots = {}
            for n, s in enumerate(saves):
                if s:
                    slots[str(n + 1)] = s
            slot = input('Your command:\n')
            if slot in slots.keys():
                break
            else:
                print('Invalid input!')
                continue

        load = [x.split(' = ')[1] for x in slots[slot].split(';')]
        self.player_name = load[0]
        self.titanium = int(load[1])
        self.robots = int(load[2])
        self.titanium_scan = bool(int(load[3]))
        self.enemy_scan = bool(int(load[4]))
        print('\t║' + 30 * '═' + '║')
        print('\t║' + 3 * ' ' + 'GAME LOADED SUCCESSFULLY' + 3 * ' ' + '║')
        print('\t║' + 30 * '═' + '║')
        print(f' Welcome back, commander {self.player_name}!')

    def upgrade_shop(self):
        print('\t║' + 30 * '═' + '║')
        print('\t║' + 9 * ' ' + 'UPGRADE SHOP' + 9 * ' ' + '║')
        print('\t║' + 24 * ' ' + 'Price' + 1 * ' ' + '║')
        print('\t║' + '[1] Titanium Scan' + 9 * ' ' + '250' + 1 * ' ' + '║')
        print('\t║' + '[2] Enemy Encounter Scan' + 2 * ' ' + '500' + 1 * ' ' + '║')
        print('\t║' + '[3] New robot' + 12 * ' ' + '1000' + 1 * ' ' + '║')
        print('\t║' + 30 * ' ' + '║')
        print('\t║' + '[Back]' + 24 * ' ' + '║')
        print('\t║' + 30 * '═' + '║')
        while True:
            user_input = input('Your command:').lower()
            if user_input == '1':
                if self.titanium_scan:
                    print('You have Titanium Scan')
                elif self.titanium < 250:
                    print("You don't have titanium")
                else:
                    self.titanium -= 250
                    self.titanium_scan = True
                    print('Purchase successful. You can see how much titanium you can get from each found location.')
                    break
            elif user_input == '2':
                if self.enemy_scan:
                    print('You have Enemy Encounter Scan')
                elif self.titanium < 500:
                    print("You don't have titanium")
                else:
                    self.titanium -= 500
                    self.enemy_scan = True
                    print('Purchase successful. You will now see how likely you will encounter an enemy at each found '
                          'location.')
                    break
            elif user_input == '3':
                if self.titanium < 1000:
                    print("You don't have titanium")
                else:
                    self.titanium -= 1000
                    self.robots += 1
                    print('Purchase successful. You now have an additional robot.')
                    break
            elif user_input == 'back':
                break
            else:
                print('Invalid input!')

    def play_game(self):
        while True:
            Game.print_board(self)
            user_command = input('Your command:\n').lower()
            if user_command == 'm':
                print_ig_menu()
                user_menu_command = input('Your command:\n').lower()
                if user_menu_command == 'back':
                    continue
                elif user_menu_command == 'main':
                    Game.menu(self)
                    break
                elif user_menu_command == 'save':
                    Game.save_game(self)
                    print('Thanks for playing, bye!')
                    break
                elif user_menu_command == 'exit':
                    print('Thanks for playing, bye!')
                    break
                else:
                    print('Invalid input!')
            elif user_command == 'ex':
                n_locs = random.randint(1, 9)
                self.locs = []
                self.titan = []
                self.encounter_rate = []
                while True:
                    print('Searching')
                    # print('Searching', end='')
                    Game.animation(self)
                    self.locs.append(random.choice(self.locations))
                    self.titan.append(random.randint(10, 100))
                    self.encounter_rate.append(random.random())
                    for n, loc in enumerate(self.locs):
                        print(f'[{n + 1}] {loc}', end=' ')
                        if self.titanium_scan:
                            print(f'Titanium: {self.titan[n]}', end=' ')
                        if self.enemy_scan:
                            percent = round(self.encounter_rate[n] * 100)
                            print(f'Encounter rate: {percent}%', end=' ')
                        print()
                    print('\n[S] to continue searching')
                    while True:
                        user_input = input('Your command: ').lower()
                        if user_input == 'back':
                            Game.play_game(self)
                            return
                        if user_input == 's' and len(self.locs) == n_locs:
                            print('Nothing more to sight!\n\t[Back]')
                            continue
                        if user_input == 's':
                            break
                        elif user_input.isnumeric() and 0 < int(user_input) <= len(self.locs):
                            location = self.locs[int(user_input) - 1]
                            # print('Deploying robots')
                            print('Deploying robots', end='')
                            # Game.animation(self)
                            x = random.random()
                            if x < self.encounter_rate[int(user_input) - 1]:
                                print('Enemy encounter')
                                if self.robots > 1:
                                    self.robots -= 1
                                    print(f'{location} explored successfully, 1 robot lost....')
                                else:
                                    Game.game_over(self)
                                    exit()
                            else:
                                print(f'{location} was explored successfully, with no damage taken.')
                            titan = self.titan[int(user_input) - 1]
                            self.titanium += titan
                            print(f'Acquired {titan} lumps of titanium')
                            Game.play_game(self)
                            return
                        else:
                            print('Invalid input!')
                    if user_input == 's':
                        continue
                    break

                break
            elif user_command == 'up':
                Game.upgrade_shop(self)
                continue
            elif user_command == 'save':
                Game.save_game(self)
            else:
                print('Invalid input!')

    def game_over(self):
        print('\t║' + 30 * '═' + '║')
        print('\t║' + 10 * ' ' + 'GAME OVER!' + 10 * ' ' + '║')
        print('\t║' + 30 * '═' + '║')

        with open('./high_scores.txt', 'r') as file:
            hs = file.read().split('\n')
        hs.append(f'{self.player_name},{self.titanium},{datetime.datetime.now()}')
        hs = [x.split(',') for x in hs]
        hs = sorted(hs, key=lambda x: (-int(x[1]), datetime.datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S.%f')),
                    reverse=True)
        hs = [','.join(x) for x in hs]
        hs.reverse()
        with open('./high_scores.txt', 'w') as file:
            file.write('\n'.join(hs[:10]))
        Game.menu(self)


def main():
    if not os.path.isfile('./save_file.txt'):
        with open('./save_file.txt', 'w') as file:
            file.write('empty\nempty\nempty')

    if not os.path.isfile('./high_scores.txt'):
        with open('./high_scores.txt', 'w') as file:
            file.write(9 * f'enemy,0,{datetime.datetime.now()}\n' + f'enemy,0,{datetime.datetime.now()}')

    args = sys.argv[1:]
    if args and args[0]:
        seed = args[0]
        random.seed(seed)
    else:
        seed = ''

    if args and args[1]:
        min_animation = int(args[1])
    else:
        min_animation = 0

    if args and args[2]:
        max_animation = int(args[2])
    else:
        max_animation = 0

    if args and args[3]:
        locations = args[3]
        locations = locations.split(',')
        for n, loc in enumerate(locations):
            locations[n] = loc.replace('_', ' ')
    else:
        locations = ['High street', 'Green park', 'Destroyed Arch']

    if max_animation != 0:
        animation = int(time.time() * int(min_animation) % int(max_animation))
    else:
        animation = 0

    game = Game(seed, animation, locations)
    # game.print_board()
    game.menu()


if __name__ == '__main__':
    main()
