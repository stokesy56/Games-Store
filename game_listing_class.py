from db_connection import *

class Game_table(Connection_db):

    def print_all_entries(self):
        query_rows = self.filter_query(f"SELECT * FROM [Game Listings]")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(f"{record[0]} - Game: {record[1]} - Console: {record[2]} - Contact Number: {record[3]} - Price: {record[4]}")

    def find_print_entry(self,game_name):
        query_row = self.filter_query(f"SELECT * FROM [Game Listings] WHERE Game = '{game_name}'")
        while True:
            record = query_row.fetchone()
            if record is None:
                break
            print(f"{record[0]} - Game: {record[1]} - Console: {record[2]} - Contact Number: {record[3]} - Price: {record[4]}")

