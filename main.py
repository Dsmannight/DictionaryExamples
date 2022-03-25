# We have 5 months with how many units where sold each month
the_dictionary = {
    "January": 200,
    "February": 150,
    "March": 160,
    "April": 200,
    "May": 250
}

# In Python you can just print whatever months where the units sold == 200
# month = key
# units_sold = value of key
for (month, units_sold) in the_dictionary.items():
    if units_sold == 200:
        print(month)

# If we want to create a dictionary to keep the months that have sold 200 units for later in our program
# I have come up with two methods

# Method #1: Loop and If statements
method_1_dict = {}
for (month, units_sold) in the_dictionary.items():
    if units_sold == 200:
        method_1_dict[month] = units_sold
print(method_1_dict)

# Method #2: Dictionary Comprehension
method_2_dict = {month: units_sold for (month, units_sold) in the_dictionary.items() if units_sold == 200}
print(method_2_dict)

# In Python we can also put dictionary items in a list to save for later

# Another version of Method #1: Loop and If statements
method_1_list = []
for (month, units_sold) in the_dictionary.items():
    if units_sold == 200:
        method_1_list.append({month: units_sold})
print(method_1_list)

# Another version of Method #2: List Comprehension
method_2_list = [{month: units_sold} for (month, units_sold) in the_dictionary.items() if units_sold == 200]
print(method_2_list)

# There are different use cases for using either a dictionary or list, it is up to preference.
# All methods are used in Pyhton but List and Dicitonary Comprehension is seen as more readable.
