def stone(month):
    stone_dictionary = {"January": "Garnet","February": "Amethyst","March" : "Aquamarine","April" : "Diamond","May" : "Emerald","June" :"Pearl","July" : "Ruby","August" : "Peridot","September" : "Sapphire","October" : "Opal","November" : "Topaz","December" : "Turquoise"}
    birthday_stone = stone_dictionary[month]
    return birthday_stone
 # call function to test it
stone1 = stone("February")
stone2 = stone("June")
stone3 = stone("January")
print(stone1)
print(stone2)
print(stone3)
