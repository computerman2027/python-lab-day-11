#Creatures package includes various modules
import Creatures
print("Find your information about creatures:examples and characteristics")
while(1):
    print("Press\n1 for fish\n2 for birds\n3 for amphibians\n4 for mammals\n5 for reptiles\n6 to exit:")
    c=int(input())
    if c==1:
        Creatures. fish.examples()
        Creatures. fish.chars()
    elif c==2:
        Creatures. birds.examples()
        Creatures. birds.chars()
    elif c==3:
        Creatures. amphibians.examples()
        Creatures. amphibians.chars()
    elif c==4:
        Creatures. mammals.examples()
        Creatures. mammals.chars()
    elif c==5:
        Creatures. reptiles.examples()
        Creatures. reptiles.chars()
    elif c==6:
        print("Thank You!!!")
        break
    else:
        print("Wrong input")
