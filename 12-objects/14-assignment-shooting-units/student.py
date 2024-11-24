class Unit:
    def __init__(self, health, firepower, armor):
        self.__health = health
        self.__firepower = firepower
        self.__armor = armor

        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError("Heath, firepower and armor are negative !")
        
    @property
    def health(self):
        return self.__health
        
    @property
    def firepower(self):
        return self.__firepower
        
    @property
    def armor(self):
        return self.__armor
        
    def shot_by(self, other):
        demage = other.firepower - self.__armor
        if demage > 0:
            self.__health -= demage
            
        if self.__health < 0:
            self.__health = 0

unitA = Unit(100, 50, 20)
unitB = Unit(80, 30, 10)

unitA.shot_by(unitB)
print(unitA.health)

unitB.shot_by(unitA)
print(unitB.health)