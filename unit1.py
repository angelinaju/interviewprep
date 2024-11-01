# def greeting(name):
#     print("Welcome to the Hundred Acre Wood " + name + "! My name is Christopher Robin.")

# greeting("Michael")
# greeting("Winnie the Pooh")

# def print_catchphrase(character):
#     if character == "Pooh":
#         print("Oh bother!")
#     elif character == "Tigger":
#         print("TFFN: Ta-ta for now!")
#     elif character == "Eeyore":
#         print("Thanks for noticing me.")
#     elif character == "Christopher Robin": 
#         print("Silly old bear.")
#     else:
#         print("Sorry! I don't know " + character + "'s catchphrase!")

# character = "Pooh"
# print_catchphrase(character)

# character = "Piglet"
# print_catchphrase(character)

# character = "Christopher Robin"
# print_catchphrase(character)
    

# def get_item(items, x):
#     if 0 <= x < len(items):
#         return items[x]
        
# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# print(get_item(items, x))

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# print(get_item(items, x))


# def sum_honey(hunny_jars):
#     total = 0
#     for i in hunny_jars:
#         total = total + i
#     return total

# hunny_jars = [2, 3, 4, 5] 
# print(sum_honey(hunny_jars))

# hunny_jars = []
# print(sum_honey(hunny_jars))

# Problem 6: Double Trouble

# def doubled(hunny_jars):
#     for i in hunny_jars:
#         hunny_jars[i-1] = hunny_jars[i-1] * 2

# hunny_jars = [1, 2, 3]
# doubled(hunny_jars)
# print(hunny_jars)


# Problem 7: Poohsticks

# def count_less_than(race_times, threshold):
#     number = 0
#     for i in race_times:
#         if race_times[i-1] < threshold:
#             number += 1
#     return number


# race_times = [1, 2, 3, 4, 5, 6]
# threshold = 4
# print(count_less_than(race_times, threshold))

# race_times = []
# threshold = 4
# print(count_less_than(race_times, threshold))
 

# Problem 8: Pooh's To Do's

# def print_todo_list(task):
#     length = len(task)
#     print("\nPooh's To Dos:")
#     for i in range(length):
#         print(str(i + 1) + ". " + task[i-1])

# task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)

# task = []
# print_todo_list(task)


# Problem 9: Pairs

# def can_pair(item_quantities):
#     for i in item_quantities:
#         if i % 2 == 1:
#             return False
#         else:
#             return True
    

# item_quantities = [2, 4, 6, 8]
# print(can_pair(item_quantities))

# item_quantities = [1, 2, 3, 4]
# print(can_pair(item_quantities))

# item_quantities = []
# print(can_pair(item_quantities))

