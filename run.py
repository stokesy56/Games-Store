from game_listing_class import *

server = 'localhost,1433'
database = 'games_db'
username = 'SA'
password = 'Passw0rd2018'

games_table = Game_table(server,database,username,password)
games_table.read_all1()