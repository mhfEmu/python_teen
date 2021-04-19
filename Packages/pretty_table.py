from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Pokemon Master", ["Pikachu", "Sharpedo", "Charizard"])
my_table.add_column("Attributes", ["Electric", "Water", "Fire"])
# print(my_table.align)

my_table.align = "l"

print(my_table)
