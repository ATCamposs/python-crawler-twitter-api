
import datetime
import logging as log
import os

from src.TrackedAppService import TrackedAppService

log.getLogger().setLevel(log.INFO)

FILENAME = "AppleStore.csv"
MAIN_PATH = os.path.dirname(__file__)
MAIN_CSV_PATH = MAIN_PATH + "/" + FILENAME
OUTPUT_PATH = MAIN_PATH + "/" + datetime.date.today().strftime("%Y-%m-%d") + "/"


def main():
    tracked_app_service = TrackedAppService(OUTPUT_PATH, MAIN_CSV_PATH)

    tracked_app_service.create_output_folder()

    tracked_app_service.read_main_csv_file()

    tracked_app_service.check_top_one_by_rating_count_tot()

    top_ten = tracked_app_service.get_top_ten_from_music_and_book()

    sorted_top_ten = tracked_app_service.sort_track_list(top_ten)

    tracked_app_service.create_json_file_with_track_list(sorted_top_ten)

    tracked_app_service.create_csv_file_with_track_list(sorted_top_ten)

    tracked_app_service.create_db_file_with_track_list(sorted_top_ten)

    print("\nList created in json, csv and db files in path: " + OUTPUT_PATH)


if __name__ == '__main__':
    main()
