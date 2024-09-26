import random


# Класс Hero
class Hero:
    def __init__(self, name, attack_power=20, health=100):
        self.name = name
        self.attack_power = attack_power
        self.health = health

    def attack(self, other):
        """Атакует другого героя, нанося ему урон в размере силы удара"""
        damage = random.randint(0, self.attack_power)  # Генерируем случайный урон от 0 до attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} на {damage} урона!")

    def is_alive(self):
        """Проверяет, жив ли герой (здоровье больше 0)"""
        return self.health > 0

    def __str__(self):
        """Возвращает строковое представление состояния героя"""
        return f"{self.name}: здоровье = {self.health}"


# Класс Game
class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        """Запускает игру"""
        print("Начинаем битву героев!")
        print(f"Игрок: {self.player}")
        print(f"Противник: {self.computer}")

        # Чередуем ходы, пока один из героев не погибнет
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            print(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} побеждает!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} побеждает!")
                break

        print("Игра окончена.")


# Запуск игры
if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
