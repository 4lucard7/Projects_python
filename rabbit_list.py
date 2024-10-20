list = [['🥕', '🥕', '🥕'], ['🥕', '🥕', '🥕'], ['🥕', '🥕', '🥕']]

print("Welcome to palce the rabbit")
 
print(f" {list[0]} \n {list[1]} \n {list[2]}")

print("Where should teh rabbit go 🐇?")

choice = input(print("Please choose a row and column: "))

row = int(choice[0])
column = int(choice[1])

list[row-1][column-1]='🐇'

print("\n Success...")

print(f" {list[0]} \n {list[1]} \n {list[2]}")




