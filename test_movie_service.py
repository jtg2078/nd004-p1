# coding: utf-8

import unittest
from movie_service import TheMovieDBAPI


class TestTheMovieDBAPIFunctions(unittest.TestCase):

    def setUp(self):
        self.moviedb_api = TheMovieDBAPI(api_key='12f10a5ecdbefb9906e99116ad3abbc9')

    def test_api_url_construction(self):
        actual = self.moviedb_api._construct_api_url(category='configuration')
        expected = 'http://api.themoviedb.org/3/configuration?api_key=12f10a5ecdbefb9906e99116ad3abbc9'
        self.assertEqual(expected, actual)
        actual = self.moviedb_api._construct_api_url(category='search/movie', params_dict={'query':'Fight Club'})
        expected = 'http://api.themoviedb.org/3/search/movie?query=Fight+Club&api_key=12f10a5ecdbefb9906e99116ad3abbc9'
        self.assertEqual(expected, actual)

    def test_search_movie_by_name(self):
        actual = self.moviedb_api.search_movie_by_name('Fight Club')['results'][0]['id']
        expected = 550
        self.assertEqual(expected, actual)

    def test_get_movie_info(self):
        actual = self.moviedb_api.get_movie_info(movie_id=550)['tagline']
        expected = "How much can you know about yourself if you've never been in a fight?"
        self.assertEqual(expected, actual)

    def test_get_movie_cast(self):
        actual = self.moviedb_api.get_movie_cast(movie_id=550)
        expected_id = 550
        expected_first_cast = 'Edward Norton'
        expected_first_cast_character = 'The Narrator'
        self.assertEqual(expected_id, actual['id'])
        self.assertEqual(expected_first_cast, actual['cast'][0]['name'])
        self.assertEqual(expected_first_cast_character, actual['cast'][0]['character'])

    def test_get_movie_images(self):
        actual = self.moviedb_api.get_movie_images(movie_id=550)
        expected_id = 550
        expected_backdrop_count_at_least = 1
        expected_poster_count_at_least = 1
        self.assertEqual(expected_id, actual['id'])
        self.assertGreaterEqual(len(actual['backdrops']), expected_backdrop_count_at_least)
        self.assertGreaterEqual(len(actual['posters']), expected_poster_count_at_least)

    def test_get_configuration(self):
        actual = self.moviedb_api._get_configuration()
        expected_base_url = 'http://image.tmdb.org/t/p/'
        self.assertEqual(expected_base_url, actual['images']['base_url'])

    def test_get_full_image_url(self):
        actual = self.moviedb_api.get_full_image_url(url='8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg')
        expected = 'http://image.tmdb.org/t/p/original/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()