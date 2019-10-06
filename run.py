from game_listing_class import *

server = 'localhost,1433'
database = 'games_db'
username = 'SA'
password = 'Passw0rd2018'

games_table = Game_table(server,database,username,password)

# games_table.print_all_entries()
# print('/////')
# games_table.find_print_entry('Batman: Arkham Asylum')
# games_table.create_entry(6,'The Elder Scrolls IV: Oblivion','PC', '07987234765', '9.99')
# print('/////new table/////')
# games_table.print_all_entries()
# games_table.delete_entry(6)
# print('/////new table/////')
# games_table.print_all_entries()
#print(games_table.get_long_and_lat('125 London Wall'))
#games_table.update_entry(1,'Location','wd3 8hy')
#print(type(games_table.get_seller_location(1)))

user_input = input("Welcome to Filipe Paiva's second hand games store. \nYou can: \n1) List all games for sale. \n2) Buy a game. \n3) Sell a game \n4) Update listing details. \nType exit to leave.\n").lower()
while user_input != 'exit':
    if user_input == '1':
        games_table.print_all_entries()

    elif user_input == '2':
        user_input2 = input('Enter game listing ID...')
        games_table.find_print_entry(user_input2)
        user_input3 = input('Would you like to buy this game?').lower()
        if user_input3.__contains__('yes'):
            print(f'Congratulations! You have purchased the game.')
            user_input4 = input('Would you like to receive the coordinates of where to pick up your game?')
            if user_input4.__contains__('yes'):
                if games_table.get_seller_location(user_input2) is None:
                    print(f'Unfortunately the seller has not provided a location. Please call them on {games_table.get_seller_phone(user_input2)} to find out.')
                    user_input5 = input('Please tell us the location')
                    games_table.update_entry(user_input2,'Location',user_input5)
                    print(games_table.get_long_and_lat(user_input2))
                else:
                    print(games_table.get_long_and_lat(user_input2))
            else:
                ('Ok no problem')
        else:
            ('Ok no problem')

    elif user_input2 == '3':



    else:
        print('Sorry, your input was invalid. Please Try again')
    user_input = input("\nWhat would you like to do now? \nYou can: \n1) List all games for sale. \n2) Buy a game. \n3) Sell a game \n4) Update listing details. \nType exit to leave\n").lower()

else:
    print('You have exited the store')
