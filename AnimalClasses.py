from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes

    customer_name = None
    customer_id = None
    name = None
    color = None
    age = None
    weight = None
    pet_id = None
    visit_reason = None

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        self.pet_id = pet_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.petType = "Animal"
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.visit_reason = visit_reason

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
        return self.petType
    
    def grow(self):
        return "I am growing"
    
    def dead(self):
        self.isDead = True
        return self.isDead
    

class Mammal(Animal):
    #Attributes

    legs = None

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Mammal"

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
        return self.petType
    

class Cat(Mammal):
     #Attributes

    collar_color = None

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name,name, color, age, weight, visit_reason)
        self.petType = "Cat"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self):
        return "I eat mice"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
class Dog(Mammal):
     #Attributes

    collar_color = None

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name,name, color, age, weight, visit_reason)
        self.petType = "Dog"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self):
        return "I eat meat"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
class Bat(Mammal):
     #Attributes

    isFlying = False
    wings = None

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Bat"
    
    #Methods
    def type(self):
        return self.petType

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
    def __init__(self, name, color, age, weight, visit_reason):
        super().__init__(name, color, age, weight, visit_reason)
        self.petType = "Budgie"
    
    #Methods
    def type(self):
        return self.petType

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
    
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Bird"
        
    #Methods
    
    def reproduce(self):
        return "I lay eggs"
    
    def move(self):
        return "I fly, walk or run"
    
    def breathe(self):
        return "I breathe through my peak"   
    
    def type(self):
        return self.petType
        
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
        self.petType = "Grass"
        
    def eat(self, otherThing):
        return False, "Grass cannot eat " + str(otherThing.petType) + "!"
        
class Leaves():
    def __init__(self):
        self.petType = "Leaves"
        
    def eat(self, otherThing):
        return False, "Leaves cannot eat " + str(otherThing.petType) + "!"

# Antelope eats grass
class Antelope(Mammal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(name, pet_id, customer_id, customer_name, color, age, weight, visit_reason)
        self.petType = "Antelope"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self, otherThing):
        if otherThing.petType == "Grass":
            return True, "Antelope eats Grass"
        else:
            return False, "Antelope cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# Big-fish eats little-fish
class Bigfish(Animal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Big-fish"
    
    #Methods
    def type(self):
        return self.petType
    
    def reproduce(self):
        return "I reproduce in water"

    def eat(self, otherThing):
        if otherThing.petType == "Little-fish":
            return True, "Big fish eats Little-fish"
        else:
            return False, "Big fish cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I swim"
    
    def breathe(self):
        return "I breathe through my gills"
    
# little-fish eats nothing
class Littlefish(Animal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Little-fish"
    
    #Methods
    def type(self):
        return self.petType
    
    def reproduce(self):
        return "I reproduce in water"

    def eat(self, otherThing):
        return False, "Little-fish cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I swim"
    
    def breathe(self):
        return "I breathe through my gills"
    
# bug eats leaves
class Bug(Animal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Bug"
    
    #Methods
    def type(self):
        return self.petType
    
    def reproduce(self):
        return "I reproduce in water"

    def eat(self, otherThing):
        if otherThing.petType == "Leaves":
            return True, "Bug eats Leaves"
        else:
            return False, "Bug cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I crawl"
    
    def breathe(self):
        return "I breathe"
    
# bear eats alot!
class Bear(Mammal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Bear"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self, otherThing):
        if otherThing.petType == "Big-fish":
            return True, "Bear eats Big-Fish"
        elif otherThing.petType == "Bug":
            return True, "Bear eats Bug"
        elif otherThing.petType == "Leaves":
            return True, "Bear eats leaves"
        elif otherThing.petType == "Chicken":
            return True, "Bear eats Chicken"
        elif otherThing.petType == "Cow":
            return True, "Bear eats Cow"
        elif otherThing.petType == "Sheep":
            return True, "Bear eats Sheep"
        else:
            return False, "Bear cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# cow eats grass
class Cow(Mammal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Cow"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self, otherThing):
        if otherThing.petType == "Grass":
            return True, "Cow eats Grass"
        else:
            return False, "Cow cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# sheep eats grass
class Sheep(Mammal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Sheep"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self, otherThing):
        if otherThing.petType == "Grass":
            return True, "Sheep eats Grass"
        else:
            return False, "Sheep cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# chicken eats grass
class Chicken(Bird):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Chicken"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self, otherThing):
        if otherThing.petType == "Bug":
            return True, "Chicken eats Bug"
        else:
            return False, "Chicken cannot eat " + str(otherThing.petType) + "!"
        
# Fox eats chicken and sheep
class Fox(Mammal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Fox"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self, otherThing):
        if otherThing.petType == "Chicken":
            return True, "Fox eats Chicken"
        elif otherThing.petType == "Sheep":
            return True, "Fox eats Sheep"
        else:
            return False, "Fox cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"

# Giraffe eats leaves
class Giraffe(Mammal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Giraffe"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self, otherThing):
        if otherThing.petType == "Leaves":
            return True, "Giraffe eats Leaves"
        else:
            return False, "Girrafe cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"

# Lion eats antelope and cow
class Lion(Mammal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Lion"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self, otherThing):
        if otherThing.petType == "Antelope":
            return True, "Lion eats Antelope"
        elif otherThing.petType == "Cow":
            return True, "Lion eats Cow"
        else:
            return False, "Lion cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"
    
# Panda eats leaves
class Panda(Mammal):
     #Attributes

    #Constructors
    def __init__(self, pet_id, customer_id, customer_name, name, color, age, weight, visit_reason):
        super().__init__(pet_id, customer_id, customer_name, name, color, age, weight, visit_reason)
        self.petType = "Panda"
    
    #Methods
    def type(self):
        return self.petType

    def eat(self, otherThing):
        if otherThing.petType == "Leaves":
            return True, "Panda eats Leaves"
        else:
            return False, "Panda cannot eat " + str(otherThing.petType) + "!"
    
    def move(self):
        return "I walk or run"
    
    def breathe(self):
        return "I breathe through my nose"