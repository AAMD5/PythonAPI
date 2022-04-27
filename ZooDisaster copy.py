from Animal import *

# creating all objects

grass = Grass()
leaves = Leaves()
#################### name, color, age, speed, isDead, weight
antelope = Antelope("Antelope", "black", 5, 20, False, 20)
bigfish = Bigfish("Big-fish", "black", 5, 20, False, 20)
littlefish = Littlefish("Little-fish", "black", 5, 20, False, 20)
bug = Bug("Bug", "black", 5, 20, False, 20)
chicken = Chicken("Chicken", "black", 5, 20, False, 20)
cow = Cow("Cow", "black", 5, 20, False, 20)
sheep = Sheep("Sheep", "black", 5, 20, False, 20)
bear = Bear("Bear", "black", 5, 20, False, 20)
fox = Fox("Fox", "black", 5, 20, False, 20)
giraffe = Giraffe("Giraffe", "black", 5, 20, False, 20)
lion = Lion("Lion", "black", 5, 20, False, 20)
panda = Panda("Panda", "black", 5, 20, False, 20)

def AnimalsToStrings(listOfAnimals):
    
    """ changes list of animal objects to list of animal names """
    
    ZooStrings = []
    for animal in listOfAnimals:
        ZooStrings.append(animal.value)
        
    return ZooStrings

def animalEat(zooList):
    
    """ function that dictates which animal eats which prey and returns output """
    
    output = [', '.join(AnimalsToStrings(zooList))]
    lastAnimal = False 
    print("Initial Zoo:", AnimalsToStrings(zooList))
    while not lastAnimal:
        for i in range(len(zooList)): 
            if zooList[i].eat(zooList[i-1])[0] == True and i != 0: # if animal can eat other item to the left
                ateAnimal = zooList[i].eat(zooList[i-1])[1] 
                output.append(ateAnimal)
                print("Eaten to the left:", ateAnimal)
                zooList.remove(zooList[i-1]) # remove left eaten item
                print("Updated Zoo:", AnimalsToStrings(zooList))
                break # resets loop to always start from LEFTMOST animal
            
            elif i < len(zooList) - 1: # to avoid list index out of range error
                if zooList[i].eat(zooList[i+1])[0] == True: # if animal can eat other item to the right
                    ateAnimal = zooList[i].eat(zooList[i+1])[1]
                    output.append(ateAnimal)
                    print("Eaten to the right:", ateAnimal) 
                    zooList.remove(zooList[i+1]) # remove right eaten item
                    print("Updated Zoo:", AnimalsToStrings(zooList))
                    break # resets loop to always start from LEFTMOST animal
            
            else: # if no edible items are present either to the left or right of the animal
                for i in range(len(zooList)):
                    print("no edible item left or right of the", zooList[i].value)
                    print("Unchanged Zoo:", AnimalsToStrings(zooList))
                output.append(', '.join(AnimalsToStrings(zooList)))
                lastAnimal = True
            
    return output
     
Zoo = [fox, bug, chicken, grass, sheep]
Zoo_2 = [bear, cow, fox, bug, chicken, grass, sheep] 
Zoo_3 = [cow, bear, cow, fox, cow, grass] 
Zoo_4 = [cow, leaves, giraffe, bear, fox, grass, sheep, bear, cow, fox, cow] 

print("First Scenario\n") 
print("\nFinal output is", animalEat(Zoo))
""" Uncomment to run other senarios """
# print("\nSecond Scenario\n")
# print("\nFinal output is", animalEat(Zoo_2))
# print("\nThird Scenario\n")
# print("\nFinal output is", animalEat(Zoo_3))
# print("\nFourth Scenario\n")
# print("\nFinal output is", animalEat(Zoo_4))