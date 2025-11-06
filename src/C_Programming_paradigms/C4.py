import random
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class FourLegged(ABC):
    @abstractmethod
    def run(self, destination):
        pass

class OxygenBreather(ABC):
    @abstractmethod
    def breath(self):
        pass


class Animal:
    def __init__(self, lives: int, currentFood: int):
        self._lives = lives
        self._currentFood = currentFood

    def eat(self, food: int):
        self._currentFood += food


class Cat(Animal, OxygenBreather, FourLegged): 
    def __init__(self, lives=7, currentFood=0):
        super().__init__(lives, currentFood)

    def getLivesLeft(self) -> int:
        #print(f"Lives left: {self._lives}")
        return self._lives

    def getCurrentAmountofFood(self) -> int:
        #print(f"Current Amount of Food: {self._currentFood}")
        return self._currentFood
    
    def _decreaseLives(self) -> None:
        if self._lives > 0:
            self._lives -= 1

    def check_food(self) -> None:
        if self._currentFood <= 0:
            self._decreaseLives()

    def run(self, destination: str) -> None:
        print(f"is running to {destination}")

    def breath(self) -> None:
        print("is brathing Oxygen")


def simulation_cat_lifs(initial_food, max_rounds=1000) -> int:
    cat = Cat(lives=7, currentFood=initial_food)

    rounds = 0
    while cat.getLivesLeft() > 0 and rounds < max_rounds:
        cat.eat(random.randint(-10, 10))
        cat.check_food()

        rounds += 1

    return rounds
        


def main() -> None:
    
    # Test for different initial food levels
    initial_food_values = list(range(0, 51, 5))  # from 0 to 50 in steps of 5
    results = [simulation_cat_lifs(f) for f in initial_food_values]

    # --- Plot ---
    plt.figure(figsize=(8, 5))
    plt.plot(initial_food_values, results, marker='o')
    plt.title("Cat survival (number of feedings) vs. initial food level")
    plt.xlabel("Initial currentFood")
    plt.ylabel("Feedings until cat dies (7 lives lost)")
    plt.grid(True)
    plt.show()


    
if __name__ == "__main__":
    main()