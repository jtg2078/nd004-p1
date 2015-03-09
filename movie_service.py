# coding: utf-8

import urllib
import urllib2
import urlparse
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

    def get_combined_movie_info(self, movie_Id):
        info_to_combine = ",".join(['releases',
                                    'videos',
                                    'credits',
                                    'reviews'])
        url = self._construct_api_url('movie/'+str(movie_Id),
                                      {'append_to_response': info_to_combine})
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

    def transform_all_images_to_full_path(self, movie_info_json):
        backdrop_sizes = "w780"
        logo_sizes = "w500"
        poster_sizes = "w780"
        profile_sizes = "w185"
        still_sizes = "w300"
        image_type_dict = {'backdrop_path': backdrop_sizes,
                           'logo_path': logo_sizes,
                           'poster_path': poster_sizes,
                           'profile_path': profile_sizes,
                           'still_path': still_sizes}

        def traverser(obj):
            if type(obj) is dict:
                for k, v in obj.iteritems():
                    if k in image_type_dict and v:
                        image_size = image_type_dict[k]
                        obj[k] = self.get_full_image_url(v, image_size)
                    if type(v) is dict or type(v) is list:
                        traverser(v)
            elif type(obj) is list:
                for i in obj:
                    traverser(i)

        traverser(movie_info_json)

    def get_full_image_url(self, url, size='original'):
        return urlparse.urljoin(self.configuration['images']['base_url'], size+url)

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
        # content = response.read()
        # data = json.loads(content)
        data = json.load(response)
        return data


if __name__ == '__main__':
    moviedb_api = TheMovieDBAPI(api_key='12f10a5ecdbefb9906e99116ad3abbc9')
    info = moviedb_api.get_combined_movie_info(movie_Id=550)
    moviedb_api.transform_all_images_to_full_path(movie_info_json=info)
    print info
