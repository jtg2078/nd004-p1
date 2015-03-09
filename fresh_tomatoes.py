# coding: utf-8

import webbrowser
import os
import re

from html_template import default_modal, extra_credit_modal


# Styles and scripting for the page
main_page_head = u'''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = u'''
<!DOCTYPE html>
<html lang="en">
  {head}
  <body>
    <!-- Modal when click on movie -->
    {movie_modal}
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = u'''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

movie_tile_content_extra_credit = u'''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-toggle="modal" data-target="#{movie_id}">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def create_movie_tiles_content_extra_credit(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += movie_tile_content_extra_credit.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            movie_id=movie.movie_id
        )
    return content


def open_web_page(rendered_content):
    # Create or overwrite the output file
    output_file = open('output/fresh_tomatoes.html', 'w')

    # Output the file
    output_file.write(rendered_content.encode("UTF-8"))
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible


def open_movies_page(movies):
    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(head=main_page_head,
                                                movie_modal=default_modal.trailer_video_modal,
                                                movie_tiles=create_movie_tiles_content(movies))
    open_web_page(rendered_content)


def open_movie_page_extra_credit(moviedb_movies):
    extra_credit = extra_credit_modal.ExtraCredit(moviedb_movies=moviedb_movies)
    rendered_content = main_page_content.format(head=main_page_head,
                                                movie_modal=extra_credit.create_modal_collection_html(),
                                                movie_tiles=create_movie_tiles_content_extra_credit(moviedb_movies))
    open_web_page(rendered_content)
