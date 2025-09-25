from prettytable import PrettyTable
pokemon=PrettyTable()
pokemon.add_column("Name", ["Pikachu", "Squirtle", "Charmander"])
pokemon.add_column("Type", ["Electric", "Water", "Fire"])
pokemon.align = "l"
print(pokemon)