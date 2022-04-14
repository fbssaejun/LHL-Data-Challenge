'''
Challenge
Dot doesn't travel to Europe often, so they decide to take the most expensive option for each course as well as drink. Create a new dictionary called meals that will contain the names of the courses as the keys (starters, mains...), and the name of the food or drink item as the values.

starters = {
    "Potato Pancakes": 7.99,
    "Salami Platter": 10.29,
    "Brezel": 6.99,
    "Maultaschen": 9.99,
    "Fried Potatoes": 4.99
}

mains = {
    "Braised Beef Short Ribs": 18.99,
    "Paprika Beef Goulash": 15.5,
    "Jager Schnitzel": 16.99,
    "House-mase Bratwurst": 11.99,
    "Kasespatzle": 14.99,
    "German Ravioli": 12.79,
    "Curry Wurst": 10.99
}

desserts = {
    "Chilled Chocolate Fondant": 7.9,
    "Pepermint Crisp Tart": 5.9,
    "Ginger Cobbler": 6.9,

}

beers = {
    "Stigel Radler": 6.9,
    "Munich Lager": 7.9,
    "Kong Ludwig Weissbier": 8.9,
    "Warsteiner Punkel": 7.5,
}


After assembling the dictionary appropriately, when Dot gives a 10% tip on this meal, how much will the tip come out to?
'''

# Create nested dictionary
meals = {
    "starters" : {
        "Potato Pancakes": 7.99,
        "Salami Platter": 10.29,
        "Brezel": 6.99,
        "Maultaschen": 9.99,
        "Fried Potatoes": 4.99
    },

    "mains" : {
        "Braised Beef Short Ribs": 18.99,
        "Paprika Beef Goulash": 15.5,
        "Jager Schnitzel": 16.99,
        "House-mase Bratwurst": 11.99,
        "Kasespatzle": 14.99,
        "German Ravioli": 12.79,
        "Curry Wurst": 10.99
    },

    "desserts" : {
        "Chilled Chocolate Fondant": 7.9,
        "Pepermint Crisp Tart": 5.9,
        "Ginger Cobbler": 6.9,

    },

    "beers" : {
        "Stigel Radler": 6.9,
        "Munich Lager": 7.9,
        "Kong Ludwig Weissbier": 8.9,
        "Warsteiner Punkel": 7.5,
    }
}

# Create function that calculates tip amount of meal (with the most expensive menu in each course)
def calculate_tip(menu):
    total_price = 0

# Loop through each course in menu, find the most expensive menu and add it to total_price
    for course in menu:
        total_price += (menu[course][max(menu[course], key=menu[course].get)])
    # Return the tip amount (10 percent)
    return total_price * 0.10

print(calculate_tip(meals)) # => 4.608
