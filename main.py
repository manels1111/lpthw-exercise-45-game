import characters
import items

#name = input("Enter your character name")
mainchar = characters.MainChar("Manel")
#firstmonster = characters.Monsters("Rabid Mouse", "It's frothing at the mouth", 50, 5, 5, 5, 1, 50)
#print(mainchar)
#print(firstmonster)
mainchar.inventory_look()
mainchar.add_inv("helmet")
mainchar.inventory_look()
