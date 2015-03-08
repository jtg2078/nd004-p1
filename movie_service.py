import urllib
import urllib2
import json


class TheMovieDBAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.root_url = 'http://api.themoviedb.org/3/'
        self.configuration = self._get_configuration()

    def search_movie_by_name(self, movie_name):
        url = self._construct_api_url('search/movie', {'query': movie_name})
        result = self._get_json_result_from_api(full_url=url)
        return result

    def get_movie_info(self, movie_id):
        url = self._construct_api_url('movie/'+str(movie_id))
        result = self._get_json_result_from_api(full_url=url)
        return result

    def get_movie_cast(self, movie_id):
        # /movie/{id}/credits
        url = self._construct_api_url('movie/'+str(movie_id)+'/credits')
        result = self._get_json_result_from_api(full_url=url)
        return result

    def get_movie_images(self, movie_id):
        # /movie/{id}/images
        url = self._construct_api_url('movie/'+str(movie_id)+'/images')
        result = self._get_json_result_from_api(full_url=url)
        return result

    def get_full_image_url(self, url, size='original'):
        return self.configuration['images']['base_url'] + size + '/' + url

    def _get_configuration(self):
        url = self._construct_api_url('configuration')
        result = self._get_json_result_from_api(full_url=url)
        return result

    def _construct_api_url(self, category, params_dict=None):
        if not params_dict:
            params_dict = dict()
        params_dict['api_key'] = self.api_key
        params = urllib.urlencode(params_dict)
        full_url = self.root_url + category + '?' + params
        return full_url

    def _get_json_result_from_api(self, full_url):
        req = urllib2.Request(full_url)
        response = urllib2.urlopen(req)
        data = json.load(response)
        return data
