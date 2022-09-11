from urllib.request import Request, urlopen
import urllib
import json
import logging as log


class TwitterAPIClient:

    def get_total_quotes_from(self, track_name):
        log.info("Search from track name: " + track_name)
        json_response = self.__do_request('https://api.twitter.com/1.1/users/search.json?q=' +
                                          urllib.parse.quote(track_name))
        if (json_response == []):
            return self.get_total_quotes_from(track_name.split(" ")[0])
            # worst method to get right twitter profile
            # return self.get_total_quotes_from(' '.join(track_name.split(" ")[:-1]))
        username = json_response[0]["screen_name"]
        return self.__get_total_quotes_from_username(username)

    def __get_total_quotes_from_username(self, username):
        log.info("Search total quotes from username: " + username)
        json_response = self.__do_request(
            'https://api.twitter.com/1.1/users/show.json?screen_name=' + username)
        total_quotes = json_response["statuses_count"]
        return total_quotes

    def __do_request(self, url):
        req = Request(url)
        req.add_header('Authorization',
                       'Bearer AAAAAAAAAAAAAAAAAAAAAKORgwEAAAAATZQMI%2Bx5QpHkeKrXQvFAtMBKACY%3DIy9SDBsRkQ7OusRBVvFtUP8copJ0INjzmIDZBzDH0w1WfShn2F')
        return json.load(urlopen(req))
