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

    def create_entry(self, listing_id, game, console, contact_number, price):
        insert_row = self.filter_query(f"INSERT INTO [Game Listings] ([Listing ID], Game, Console, Phone, Price) Values ({listing_id}, '{game}', '{console}', '{contact_number}', '{price}')")
        insert_row.commit()

    def delete_entry(self, listing_id):
        delete_row = self.filter_query(f"DELETE FROM [Game Listings] WHERE [Listing ID] = {listing_id}")
        delete_row.commit()

    def update_entry(self, listing_id, column_name, new_value):
        update_row = self.sql_query((f"UPDATE [Game Listings] SET {column_name} = {new_value} WHERE [Listing ID] = {listing_id}"))
        update_row.commit()

    