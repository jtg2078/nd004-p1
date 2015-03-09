import media
import json
import fresh_tomatoes
import movie_service
import os.path

birdman = media.Movie("Birdman",
                      "A washed-up actor, battles his ego and attempts to recover his family, his career",
                      "http://upload.wikimedia.org/wikipedia/en/a/a3/Birdman_poster.jpg",
                      "https://www.youtube.com/watch?v=uJfLoE6hanc")

the_grand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
                                       "GRAND BUDAPEST HOTEL recounts the adventures of Gustave H, a legendary concierge at a famous European hotel",
                                       "http://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
                                       "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

whiplash = media.Movie("Whiplash",
                       "A promising young drummer enrolls at a cut-throat music conservatory",
                       "http://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

gone_girl = media.Movie("Gone Girl",
                        "The movie is about dishonesty and the effects of recession on a marriage",
                        "http://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
                        "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")

john_wick = media.Movie("John Wick",
                        "The story of John Wick forced to say he is back",
                        "http://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
                        "https://www.youtube.com/watch?v=RllJtOw0USI")

five_armies = media.Movie("The Hobbit: The Battle of the Five Armies",
                          "Men(Lake Town) vs Elves(Mirkwood) vs Dwarves(Iron Hills) vs Orcs(Dol Guldur) vs Orcs/goblins(Gundabad)",
                          "http://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
                          "https://www.youtube.com/watch?v=ZSzeFFsKEt4")

galaxy = media.Movie("Guardians of the Galaxy",
                     "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe",
                     "http://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                     "https://www.youtube.com/watch?v=Y2bj8e9_zjo")


def extra_credit_version():
    moviedb_api = movie_service.TheMovieDBAPI(api_key='12f10a5ecdbefb9906e99116ad3abbc9')
    favorite_movies = ['Birdman', 'The Grand Budapest Hotel', 'Whiplash', 'John Wick']
    # favorite_movies = ['Birdman']

    def save_cache(movie_name, movie_json):
        with open("themoviedb_cached_data/" + movie_name + ".json", "w") as outfile:
            json.dump(movie_json, outfile)
        print "cached saved"

    def load_cache(movie_name):
        if os.path.exists("themoviedb_cached_data/" + movie_name + ".json"):
            with open("themoviedb_cached_data/" + movie_name + ".json", "r") as infile:
                return json.load(infile)
        return None

    def fetch_content(movie_name):
        print "fetching movie data for {0}...".format(movie_name)
        movie_json = load_cache(movie_name)
        if movie_json:
            print "will load movie data from cache"
        else:
            print "will load movie data from the movie db api"
            movie_id = moviedb_api.search_movie_by_name(movie_name)['results'][0]['id']
            movie_json = moviedb_api.get_combined_movie_info(movie_Id=movie_id)
            save_cache(movie_name, movie_json)
        print "movie data loaded"
        moviedb_api.transform_all_images_to_full_path(movie_info_json=movie_json)
        return media.TheMovieDBMovie(moviedb_json=movie_json)

    print "welcome to jason's movie list"
    movies = []
    for name in favorite_movies:
        movies.append(fetch_content(name))

    print "generating html...",
    fresh_tomatoes.open_movie_page_extra_credit(movies)
    print "done"


def default_version():
    fresh_tomatoes.open_movies_page([birdman,
                                     the_grand_budapest_hotel,
                                     whiplash, gone_girl,
                                     john_wick,
                                     five_armies,
                                     galaxy])


use_extra_credit_version = True

if __name__ == '__main__':
    if use_extra_credit_version:
        extra_credit_version()
    else:
        default_version()
