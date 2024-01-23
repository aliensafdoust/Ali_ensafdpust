fruits = {
    "banana": 110,
    "apple": 130,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "avocado": 50,
    "honeydew Melon": 50,
    "kiwifruit": 90,
    "pear": 100,
    "lemon": 15,
    "lime": 20,
    "orange": 80,
    "strawberries": 50,
    "peach": 60,
    "pineapple": 50,
    "nectarine": 60,
    "plums": 70,
    "cherries": 100,
    "watermelon": 80,
    "tangerine": 50,
    "sweet cherries": 100,
}

fru = input("Item: ").strip().lower()

if fru in fruits:
    print(f"Calories: {fruits[fru]}")
