import random


class Player:
    health = 10
    max_health = 10
    position = [2, 0]

    def was_hit(self, hid):
        # self.health -= hid
        self.health -= 1 + random.choice(range(hid))
        print(random.choice(range(hid)))

    def wait(self):
        if not self.health == self.max_health:
            self.health += 1
        print("player's health:", self.health)

# исправлен урон, так как задача была в том чтобы максимальный урон был как id, у нас был id+1
# (self.health -= 1 + random.choice(range(hid))
