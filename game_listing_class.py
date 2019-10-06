from db_connection import *
import requests

class Game_table(Connection_db):

    def print_all_entries(self):
        query_rows = self.filter_query(f"SELECT * FROM [Game Listings]")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(f"{record[0]} - Game: {record[1]} - Console: {record[2]} - Contact Number: {record[3]} - Price: {record[4]}")

    def find_print_entry(self,listing_id):
        query_row = self.filter_query(f"SELECT * FROM [Game Listings] WHERE [Listing ID] = '{listing_id}'")
        while True:
            record = query_row.fetchone()
            if record is None:
                break
            print(f"{record[0]} - Game: {record[1]} - Console: {record[2]} - Contact Number: {record[3]} - Price: {record[4]}")

    def create_entry(self, listing_id, game, console, contact_number, price, location):
        insert_row = self.filter_query(f"INSERT INTO [Game Listings] ([Listing ID], Game, Console, Phone, Price, Location) Values ({listing_id}, '{game}', '{console}', '{contact_number}', '{price}', '{location}')")
        insert_row.commit()

    def delete_entry(self, listing_id):
        delete_row = self.filter_query(f"DELETE FROM [Game Listings] WHERE [Listing ID] = {listing_id}")
        delete_row.commit()

    def update_entry(self, listing_id, column_name, new_value):
        update_row = self.filter_query(f"UPDATE [Game Listings] SET {column_name} = '{new_value}' WHERE [Listing ID] = {listing_id}")
        update_row.commit()

    def get_seller_location(self,listing_id):
        query_row = self.filter_query(f"SELECT Location FROM [Game Listings] WHERE [Listing ID] = {listing_id}")
        return query_row.fetchone()[0]

    def get_seller_phone(self,listing_id):
        query_row = self.filter_query(f"SELECT Phone FROM [Game Listings] WHERE [Listing ID] = {listing_id}")
        return query_row.fetchone()[0]

    def get_long(self,listing_id):
        location = self.get_seller_location(listing_id)
        lat_long = requests.get(
            f"https://eu1.locationiq.com/v1/search.php?key=bbd9cdd1dc6146&q={location}&format=json".lower().strip())
        lat_long_dict = lat_long.json()
        longitude = str(lat_long_dict[0]['lon'])
        return longitude

    def get_lat(self,listing_id):
        location = self.get_seller_location(listing_id)
        lat_long = requests.get(
            f"https://eu1.locationiq.com/v1/search.php?key=bbd9cdd1dc6146&q={location}&format=json".lower().strip())
        lat_long_dict = lat_long.json()
        latitude = str(lat_long_dict[0]['lat'])
        return latitude

    def get_long_and_lat(self,listing_id):
        latitude = self.get_lat(listing_id)
        longitude = self.get_long(listing_id)
        return 'Latitude: ' + latitude + ', Longitude: ' + longitude

    def listing_id_generator(self):
        rows = self.filter_query("SELECT * FROM [Game Listings]").fetchall()
        return len(rows) + 1

