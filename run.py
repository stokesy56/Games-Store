from game_listing_class import *

server = 'localhost,1433'
database = 'games_db'
username = 'SA'
password = 'Passw0rd2018'

games_table = Game_table(server,database,username,password)

games_table.print_all_entries()
print('/////')
games_table.find_print_entry('Batman: Arkham Asylum')
games_table.create_entry(6,'The Elder Scrolls IV: Oblivion','PC', '07987234765', '9.99')
print('/////new table/////')
games_table.print_all_entries()
games_table.delete_entry(6)
print('/////new table/////')
games_table.print_all_entries()
print(games_table.get_long_and_lat('Wd3 8Hy'))
