import webbrowser

class Movie:
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TheMovieDBMovie(Movie):
    def __init__(self, moviedb_json):
        Movie.__init__(self,
                       movie_title=moviedb_json['title'],
                       movie_storyline=moviedb_json['overview'],
                       poster_image=moviedb_json['poster_path'],
                       trailer_youtube='https://www.youtube.com/watch?v='+moviedb_json['videos']['results'][0]['key'])
        self.moviedb_json = moviedb_json
        self.genres = [g['name'] for g in moviedb_json['genres']]
        self.score = moviedb_json['vote_average']
        self.certification = [c for c in moviedb_json['releases']['countries'] if c['iso_3166_1'] == 'US'][0]['certification']
        self.year = moviedb_json['release_date'].split("-")[0]
        self.backdrop = moviedb_json['backdrop_path']
        self.runtime = moviedb_json['runtime']
        self.movie_id = moviedb_json['id']
        self.youtube_id = moviedb_json['videos']['results'][0]['key']
