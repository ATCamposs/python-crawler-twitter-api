import logging as log

from src.TwitterAPIClient import TwitterAPIClient


class AppleStoreDFAnalyzer:
    df = None

    def __init__(self, dataframe):
        self.df = dataframe

    def get_top_one_track_name_from_news(self):
        log.info("Getting top one by rating_count_total from News")
        genre_news = self.df["prime_genre"] == "News"
        top_track = self.df.sort_values(
            "rating_count_tot", ascending=False).loc[genre_news].iloc[0:1]
        top_track_name = top_track["track_name"].values[0]
        return top_track_name

    def get_top_ten_from_music_and_book(self):
        log.info(
            "Getting top ten from music and book genre, " +
            "ordered by rating_count_total")
        genre_music_and_book = self.df["prime_genre"].isin(["Music", "Book"])
        top_ten_tracks = self.df.sort_values(
            "rating_count_tot",
            ascending=False
        ).loc[genre_music_and_book].iloc[0:10]
        tracks = []
        for index, row in top_ten_tracks.iterrows():
            twitter_client = TwitterAPIClient()
            tracks.append(self.__parse_row(
                row, twitter_client.get_total_quotes_from(row["track_name"])))
        return tracks

    def __parse_row(self, row, quotes_count):
        return {
            "id": row["id"],
            "track_name": row["track_name"],
            "n_citacoes": quotes_count,
            "size_bytes": row["size_bytes"],
            "price": row["price"],
            "prime_genre": row["prime_genre"]
        }
