
from player import Player
from hamsters import Hamster

hamsters_count = 4


class Game:
    happy_message = "WOW!!!!! You won!!!"
    map = """****\n****\n****\n****"""
    gameon = True
    hamsters = []

    def __init__(self):
        self.player = Player()
        self.hamsters = []
        for i in range(hamsters_count):
            self.hamsters.append(Hamster(i + 1, self.get_full_map()))

    def add_point(self, position, name, s):
        li = s.split("\n")
        row = li[position[1]]
        row = row[:position[0]] + name + row[position[0] + 1:]
        li[position[1]] = row
        return "\n".join(li)

    def render_map(self):
        s = self.map
        s = self.add_point(self.player.position, "x", s)
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)
        print(s)

    directions = {"w": "s", "s": "w", "a": "d", "d": "a"}

    def move_player(self, destination):
        """ destination = w,a,s,d """
        if destination == "s":
            self.player.position[1] += 1  # bottom
            if self.player.position[1] == len(self.map.split("\n")):
                self.player.position[1] -= 1
        if destination == "w":
            self.player.position[1] -= 1  # top
            if self.player.position[1] < 0:
                self.player.position[1] += 1
        if destination == "a":
            self.player.position[0] -= 1  # left
            if self.player.position[0] < 0:
                self.player.position[0] += 1
        if destination == "d":
            self.player.position[0] += 1  # right
            if self.player.position[0] == len(self.map.split("\n")):
                self.player.position[0] -= 1
        self.on_move(destination)

    def get_full_map(self):
        s = self.map
        s = self.add_point(self.player.position, "x", s)
        for h in self.hamsters:
            s = self.add_point(h.position, str(h.id), s)
        return s

    def get_on_position(self, coords):
        s = self.get_full_map()
        return s.split("\n")[coords[1]][coords[0]]

    def on_move(self, direction):
        point = self.get_on_position(self.player.position)
        if not point == 'x' and "*":
            self.player.was_hit(int(point))
            if self.player.health <= 0:
                self.gameon = False
                print("game over... sorry!")
                return False
            else:
                print("player's health: ", self.player.health)
            hamster_id = int(point)
            hamster = self.get_hamster_by_id(self.hamsters, hamster_id)
            killed = hamster.on_shot()
            if not killed:
                self.move_player(self.directions[direction])
            else:
                self.hamsters.remove(hamster)

    def get_hamster_by_id(self, hamsters, id):
        for hamster in hamsters:
            if hamster.id == id:
                return hamster

    def start(self):
        game.render_map()
        game.get_full_map()

        while self.gameon:
            if len(self.hamsters) == 0:
                print(self.happy_message)
                return True

            command = input("Insert command: ")
            if command in ["a", "s", "d", "w"]:
                self.move_player(command)
                self.render_map()
            if command == "e":
                self.player.wait()
            if command == "q":
                print("Game canceled because of you! >:-(")
                self.gameon = False


game = Game()

game.start()

# добавлены: s = self.add_point(self.player.position, "x", s) в get_full_map для того, чтобы робохомяк не появлялся
#            на герое
#            if not hamster == 'x': в on_move, чтобы хомяк не принимал значение героя
#
#            print("Game canceled because of you! >:-(") в command == "q": чтобы было понятно что мы вышли из игры
#
#            чтобы невидимые хомяки не лупили героя я их удаляю из массива хомяков. для удаления хомяков по id добавлен
#            метод get_hamster_by_id для использования вместо  killed = self.hamsters[int(hamster)-1] (так как масив
#            хомяков уменьшается)

#            изменена логика хождения по карте, чтобы не выходить за ее границы.

