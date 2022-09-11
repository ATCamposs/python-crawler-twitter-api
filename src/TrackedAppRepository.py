import sqlite3
import logging as log


class TrackedAppRepository:
    conn = None

    def __init__(self, path):
        log.info(path)
        self.conn = sqlite3.connect(path)

    def __del__(self):
        self.conn.close()

    def insert_track_list_on_db(self, track_list):
        log.info("Starting data insertion")
        for track in track_list:
            values = ", ".join(
                '"' + str(v) + '"' for v in list(track.values()))
            insert_base_query = "INSERT INTO tracked_apps (id,track_name,n_citacoes,size_bytes,price,prime_genre)"
            query = f'{insert_base_query} VALUES ({values});'
            print(query)
            self.conn.execute(query)
        self.conn.commit()
        log.info("Data insertion finished successfully")

    def create_table_tracked_apps(self):
        log.info("Creating table tracked_apps")
        self.conn.execute("""CREATE TABLE IF NOT EXISTS tracked_apps
                (id           INT,
                track_name    TEXT,
                n_citacoes    TEXT,
                size_bytes    INT,
                price         REAL,
                prime_genre   TEXT);""")

    def remove_old_data_from_tacked_apps_table(self):
        if (self.__check_if_data_exists()):
            log.warning("Removing old data from table tracked_apps")
            self.conn.execute("DELETE FROM tracked_apps")

    def __check_if_data_exists(self):
        cur = self.conn.cursor()
        cur.execute("SELECT count(*) FROM tracked_apps")
        total = cur.fetchone()
        return total[0] > 0
