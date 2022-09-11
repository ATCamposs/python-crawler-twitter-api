import os
import json
import csv
import logging as log
import pandas as pd

from src.TrackedAppRepository import TrackedAppRepository
from src.AppleStoreDFAnalyzer import AppleStoreDFAnalyzer


class TrackedAppService:
    output_path = None
    original_csv_file_path = None
    json_filename = "top_apps_by_total_quote.json"
    csv_filename = "top_apps_by_total_quote.csv"
    db_filename = "top_apps_by_total_quote.db"
    json_output_path = ""
    csv_output_path = ""
    db_output_path = ""
    apple_store_df_analyzer = None
    tracked_app_repo = None

    def __init__(self, output_path, original_csv_file_path):
        self.output_path = output_path
        self.original_csv_file_path = original_csv_file_path
        self.json_output_path = self.output_path + self.json_filename
        self.csv_output_path = self.output_path + self.csv_filename
        self.db_output_path = self.output_path + self.db_filename
        self.tracked_app_repo = TrackedAppRepository(self.db_output_path)

    def read_main_csv_file(self):
        log.info("Start reading main CSV file")
        df = pd.read_csv(self.original_csv_file_path)
        self.apple_store_df_analyzer = AppleStoreDFAnalyzer(df)

    def check_top_one_by_rating_count_tot(self):
        name = self.apple_store_df_analyzer.get_top_one_track_name_from_news()
        self.__check_top_ranking_track_name(name)

    def get_top_ten_from_music_and_book(self):
        return self.apple_store_df_analyzer.get_top_ten_from_music_and_book()

    def sort_track_list(self, track_list):
        return sorted(
            track_list,
            key=lambda track: track["n_citacoes"],
            reverse=True
        )

    def create_json_file_with_track_list(self, track_list):
        log.info("Creating JSON file with track_list")
        json_top_ten = json.dumps(track_list)
        with open(self.output_path + self.json_filename, "w") as outfile:
            outfile.write(json_top_ten)

    def create_csv_file_with_track_list(self, track_list):
        log.info("Creating CSV file with track_list")
        with open(self.output_path + self.csv_filename, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[
                                    "id",
                                    "track_name",
                                    "n_citacoes",
                                    "size_bytes",
                                    "price",
                                    "prime_genre"
                                    ])
            writer.writeheader()
            writer.writerows(track_list)

    def create_db_file_with_track_list(self, track_list):
        log.info("Creating sqlite DB file with track_list")
        self.tracked_app_repo.connect_to_db()
        self.tracked_app_repo.create_table_tracked_apps()
        self.tracked_app_repo.remove_old_data_from_tacked_apps_table()
        self.tracked_app_repo.insert_track_list_on_db(track_list)

    def create_output_folder(self):
        if not os.path.exists(self.output_path):
            log.info("Creating output folder")
            os.makedirs(self.output_path)

    def __check_top_ranking_track_name(self, name):
        if (name != "Twitter"):
            log.critical(
                """Only \"Twitter\" is accepted for API search on this version,
                but top one tracking name from news is: """ + name
            )
            exit()
