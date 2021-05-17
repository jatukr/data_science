def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for groups, users in group_dictionary.items():
        print('-'+groups)
        for user in users:
            print(user)
            if user not in user_groups:
                user_groups[user] = [groups]
            else:
                user_groups[user].append(groups)
    return user_groups


print(groups_per_user({"local": ["admin", "userA"], 
                        "public":  ["admin", "userB"], 
                        "administrator": ["admin"]}))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

def add_prices(basket):
    # Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item_value in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += item_value
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44