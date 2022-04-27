from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes

    name = None
    color = None
    age = None
    speed = None
    isDead = False
    weight = None

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        self.value = "Animal"
        self.name = name
        self.color = color
        self.age = age
        self.speed = speed
        self.isDead = isDead
        self.weight = weight

    #Methods
    @abstractmethod # so these are methods that will be defined later
    def reproduce(self):
        pass

    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def breathe(self):
        pass

    def sleep(self):
        return "I am sleeping"

    def type(self):
        return self.value
    
    def grow(self):
        return "I am growing"
    
    def dead(self):
        self.isDead = True
        return self.isDead
    

class Mammal(Animal):
    #Attributes

    legs = None

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Mammal"

    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def breathe(self):
        pass    
    
    def reproduce(self):
        return "I give birth"

    def type(self):
        return self.value
    

class Cat(Mammal):
     #Attributes

    collar_color = None

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Cat"
    
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat mice"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
class Bat(Mammal):
     #Attributes

    isFlying = False
    wings = None

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Bat"
    
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat meat"
    
    def move(self):
        return "I fly"
    
    def breathe(self):
        return "I breathe through my nose"
    
    def flying(self):
        self.isFlying = True
        return self.isFlying
    
    def landing(self):
        self.isFlying = False
        return self.isFlying
    
    
class Platypus(Mammal):
     #Attributes


    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Budgie"
    
    #Methods
    def type(self):
        return self.value

    def eat(self):
        return "I eat plants"
    
    def reproduce(self):
        return "I lay eggs"
    
    def move(self):
        return "I am amphibious"
    
    def breathe(self):
        return "I breathe through my nose"
    

class Bird(Animal):
    
    #Attributes
    
    wings = None
    legs = None
    isFlying = False
    
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Bird"
        
    #Methods
    
    def reproduce(self):
        return "I lay eggs"
    
    def move(self):
        return "I fly, walk or run"
    
    def breathe(self):
        return "I breathe through my peak"   
    
    def type(self):
        return self.value
        
    def eat(self):
        return "I eat worms"
    
    def flying(self):
        self.isFlying = True
        return self.isFlying
    
    def landing(self):
        self.isFlying = False
        return self.isFlying

class Grass():
    def __init__(self):
        self.value = "Grass"
        
    def eat(self, otherThing):
        return False, "Grass cannot eat " + str(otherThing.value) + "!"
        
class Leaves():
    def __init__(self):
        self.value = "Leaves"
        
    def eat(self, otherThing):
        return False, "Leaves cannot eat " + str(otherThing.value) + "!"

# Antelope eats grass
class Antelope(Mammal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Antelope"
    
    #Methods
    def type(self):
        return self.value

    def eat(self, otherThing):
        if otherThing.value == "Grass":
            return True, "Antelope eats Grass"
        else:
            return False, "Antelope cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# Big-fish eats little-fish
class Bigfish(Animal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Big-fish"
    
    #Methods
    def type(self):
        return self.value
    
    def reproduce(self):
        return "I reproduce in water"

    def eat(self, otherThing):
        if otherThing.value == "Little-fish":
            return True, "Big fish eats Little-fish"
        else:
            return False, "Big fish cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I swim"
    
    def breathe(self):
        return "I breathe through my gills"
    
# little-fish eats nothing
class Littlefish(Animal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Little-fish"
    
    #Methods
    def type(self):
        return self.value
    
    def reproduce(self):
        return "I reproduce in water"

    def eat(self, otherThing):
        return False, "Little-fish cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I swim"
    
    def breathe(self):
        return "I breathe through my gills"
    
# bug eats leaves
class Bug(Animal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Bug"
    
    #Methods
    def type(self):
        return self.value
    
    def reproduce(self):
        return "I reproduce in water"

    def eat(self, otherThing):
        if otherThing.value == "Leaves":
            return True, "Bug eats Leaves"
        else:
            return False, "Bug cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I crawl"
    
    def breathe(self):
        return "I breathe"
    
# bear eats alot!
class Bear(Mammal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Bear"
    
    #Methods
    def type(self):
        return self.value

    def eat(self, otherThing):
        if otherThing.value == "Big-fish":
            return True, "Bear eats Big-Fish"
        elif otherThing.value == "Bug":
            return True, "Bear eats Bug"
        elif otherThing.value == "Leaves":
            return True, "Bear eats leaves"
        elif otherThing.value == "Chicken":
            return True, "Bear eats Chicken"
        elif otherThing.value == "Cow":
            return True, "Bear eats Cow"
        elif otherThing.value == "Sheep":
            return True, "Bear eats Sheep"
        else:
            return False, "Bear cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# cow eats grass
class Cow(Mammal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Cow"
    
    #Methods
    def type(self):
        return self.value

    def eat(self, otherThing):
        if otherThing.value == "Grass":
            return True, "Cow eats Grass"
        else:
            return False, "Cow cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# sheep eats grass
class Sheep(Mammal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Sheep"
    
    #Methods
    def type(self):
        return self.value

    def eat(self, otherThing):
        if otherThing.value == "Grass":
            return True, "Sheep eats Grass"
        else:
            return False, "Sheep cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# chicken eats grass
class Chicken(Bird):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Chicken"
    
    #Methods
    def type(self):
        return self.value

    def eat(self, otherThing):
        if otherThing.value == "Bug":
            return True, "Chicken eats Bug"
        else:
            return False, "Chicken cannot eat " + str(otherThing.value) + "!"
        
# Fox eats chicken and sheep
class Fox(Mammal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Fox"
    
    #Methods
    def type(self):
        return self.value

    def eat(self, otherThing):
        if otherThing.value == "Chicken":
            return True, "Fox eats Chicken"
        elif otherThing.value == "Sheep":
            return True, "Fox eats Sheep"
        else:
            return False, "Fox cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"

# Giraffe eats leaves
class Giraffe(Mammal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Giraffe"
    
    #Methods
    def type(self):
        return self.value

    def eat(self, otherThing):
        if otherThing.value == "Leaves":
            return True, "Giraffe eats Leaves"
        else:
            return False, "Girrafe cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"

# Lion eats antelope and cow
class Lion(Mammal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Lion"
    
    #Methods
    def type(self):
        return self.value

    def eat(self, otherThing):
        if otherThing.value == "Antelope":
            return True, "Lion eats Antelope"
        elif otherThing.value == "Cow":
            return True, "Lion eats Cow"
        else:
            return False, "Lion cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# Panda eats leaves
class Panda(Mammal):
     #Attributes

    #Constructors
    def __init__(self, name, color, age, speed, isDead, weight):
        super().__init__(name, color, age, speed, isDead, weight)
        self.value = "Panda"
    
    #Methods
    def type(self):
        return self.value

    def eat(self, otherThing):
        if otherThing.value == "Leaves":
            return True, "Panda eats Leaves"
        else:
            return False, "Panda cannot eat " + str(otherThing.value) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"