# coding: utf-8
import re

class ExtraCredit(object):
    def __init__(self, moviedb_movies):
        self.movies = moviedb_movies

    def create_synopsis_html(self, moviedb_movie):

        def create_genres_html():
            genre_template = u'<li>{genre}</li>'
            genres_html = ''
            for g in moviedb_movie.genres:
                genres_html += genre_template.format(genre=g)
            return u'<ul>' + genres_html + u'</ul>'

        return ExtraCredit.synopsis_template.format(title=moviedb_movie.title,
                                                    overview=moviedb_movie.storyline,
                                                    poster=moviedb_movie.poster_image_url,
                                                    trailer=moviedb_movie.trailer_youtube_url,
                                                    genres=create_genres_html(),
                                                    score=moviedb_movie.score,
                                                    certification=moviedb_movie.certification,
                                                    year=moviedb_movie.year,
                                                    backdrop=moviedb_movie.backdrop,
                                                    runtime=moviedb_movie.runtime)

    def create_trailer_html(self, moviedb_movie):
        return ExtraCredit.trailer_template.format(movieID=moviedb_movie.movie_id,
                                                   youtubeID=moviedb_movie.youtube_id)

    def create_modal_html(self, moviedb_movie):
        synopsis = self.create_synopsis_html(moviedb_movie)
        trailer = self.create_trailer_html(moviedb_movie)
        cast = self.create_cast_html(moviedb_movie)
        review = self.create_review_html(moviedb_movie)
        return ExtraCredit.modal_template.format(movie_id=moviedb_movie.movie_id,
                                                 synopsis_tab=synopsis,
                                                 trailer_tab=trailer,
                                                 cast_tab=cast,
                                                 review_tab=review)

    def create_modal_collection_html(self):
        modals_html = ''
        for movie in self.movies:
            modals_html += self.create_modal_html(movie)
        return ExtraCredit.modal_collection_template.format(style=ExtraCredit.style_template,
                                                            modals=modals_html,
                                                            script=ExtraCredit.script_template)

    modal_collection_template = u'''
    <div id="extraCreditModals">
        {style}
        {modals}
        {script}
    </div>
    '''

    style_template = u'''
    <style>

        .modal-dialog ::-webkit-scrollbar {
            width: 12px;
        }

        .modal-dialog ::-webkit-scrollbar-track {
            background-color:#191717;
        }

        .modal-dialog ::-webkit-scrollbar-thumb {
            background-color:#424242;
        }

        .modal-dialog {
          width: 80%;
          height: 90%;
          margin-right: auto;
          margin-left: auto;
          margin-top: 10%;
        }
        .modal-content {
          height:80%;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        .cnt a {
          text-decoration:none
        }
        .cnt ul{
          list-style-type: none;
          margin:0;
          padding: 0;
        }
        .cnt {
          position:absolute;
          width: 100%;
          height:100%;
          background:#333;
        }
        .cnt .top{
          position:relative;
          height:100%;
          width:100%;
          background:black;
          padding-bottom:50px;
        }
        .cnt .top .content {
          display:none;
          color: #fff;
          width:100%;
          height:100%;
        }
        .cnt .top .content.active {
          display:block;
        }
        .cnt .bottom{
          position:relative;
          height:50px;
          bottom:50px;
        }
        .cnt .bottom .menu {
          position:absolute;
          width: 100%;

        }
        .cnt .bottom .menu li{
          display:inline-block;
          width: 25%;
          margin:0;
          min-height:50px;
          padding:0;
          box-sizing: border-box;
          text-align:center;
          margin-right:-4px;
        }
        .cnt .bottom .menu a{
          display:block;
          color:#666;
          background:#191717;
          height:100%;
          min-height:50px;
          line-height:50px;
          font-size:14px;
        }
        .cnt .bottom .menu a:active,
        .cnt .bottom .menu a.active {
          background:#FFC917;
        }
        .cnt .bottom .menu a:hover {
          color: #FFC917;
        }
        .cnt .bottom .menu a:active{
          color:#666;
        }
        .cnt .bottom .menu a:hover.active {
          color:#666;
        }

        .synopsis {
          font-family: 'Open Sans', sans-serif;
          background-size: cover;
          background-repeat: no-repeat;
          background-position: top center;
          padding-left:20px;
          position: relative;
          width:100%;
          height:100%;
        }

        .synopsis .bg {
          position: absolute;
          width: 100%;
          height: 100%;
          left: 0;
          top: 0;
          background: -moz-linear-gradient(top, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.65) 100%); /* FF3.6+ */
          background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, rgba(0, 0, 0, 0)), color-stop(100%, rgba(0, 0, 0, 0.65))); /* Chrome,Safari4+ */
          background: -webkit-linear-gradient(top, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.65) 100%); /* Chrome10+,Safari5.1+ */
          background: -o-linear-gradient(top, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.65) 100%); /* Opera 11.10+ */
          background: -ms-linear-gradient(top, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.65) 100%); /* IE10+ */
          background: linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.65) 100%); /* W3C */
          filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#a6000000', GradientType=0); /* IE6-9 */
        }

        .synopsis .should-be-relative {
          position: relative;
          width:100%;
          height:100%;
          overflow-y:scroll;
        }

        .synopsis .title {
          font-size: 60px;
          color: #fff;
          margin: 60px 0 10px 0;

        }

        .synopsis .top-group {

        }

        .synopsis .top-group > div {
          display:inline-block;
          color:fff;
          line-height: 40px;
          margin: 0 10px;
          text-align: center;
          font-size:16px;
        }

        .synopsis .top-group .score {
          background:#8BC34A;
          font-weight:bold;
          border-radius:100%;
          width:40px;
          text-align: center;
        }

        .synopsis .top-group .certification {
          padding:0 10px;
          line-height: 21px;
          font-size:13px;
          font-weight:bold;
          border-radius:3px;
          border:solid 1px white;
        }

        .synopsis .hr {
          border-bottom: 1px solid rgba(238, 238, 238, 0.33);
          margin: 20px auto 40px auto;
        }

        .synopsis .overview {

        }

        .synopsis .overview .left {
          float: left;
          width: 100px;
        }

        .synopsis .overview .right {
          float: left;
          margin-left: 20px;
          width: 600px;
          display: inline-block;
          color: #E9E9E9;
          line-height: 22px;
        }

        .synopsis .overview .right .genres ul {
          padding: 0;
          margin-bottom:40px;
        }

        .synopsis .overview .right .genres li {
          list-style: none;
          display: inline-block;
          border: 1px solid #eee;
          padding: 2px 10px;
          margin-right: 10px;
          border-radius: 3px;
        }


        .scale-media {
            width:100%;
            height:100%;
            position:relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            width: 100%;
            position: absolute;
            left: 0;
            top: 0;
            background-color: black;
        }
        .cast-list {
            height: 100%;
            overflow-y: scroll;
        }
        .cast-list-actor {
            padding:20px;
            border-bottom:solid 1px #9E9E9E;
        }
        .cast-list-actor:last-child{
            border-bottom:none;
        }
        .actor-avatar-panel {
            float:left;
            margin-right:15px;
        }
        .actor-info-panel {
            float:left;
        }
        .actor-name {
            font-size:30px;
        }
        .actor-as {
            margin: 10px 0;
        }
        .review-list {
            height: 100%;
            padding:20px;
            overflow-y: scroll;
        }
        .review-section-header {
            margin-bottom:10px;
        }
        .review-movie-name {
            font-size:30px;
        }
        .review-movie-year {
            display:inline-block;
            margin-left:5px;
        }
        .review-item-header {
            margin-bottom:10px;
        }
    </style>
    '''

    modal_template = u'''
    <div class="modal" id="{movie_id}">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="cnt">
             <section class="top">
                <div id="{movie_id}-synopsis" class="content active">{synopsis_tab}</div>
                <div id="{movie_id}-trailer" class="content trailer trailer-need-init">{trailer_tab}</div>
                <div id="{movie_id}-cast" class="content">{cast_tab}</div>
                <div id="{movie_id}-review" class="content">{review_tab}</div>
             </section>
             <section class="bottom">
               <nav class="menu">
                 <ul>
                   <li><a class="active" href="#" data-content="synopsis">SYNOPSIS</a></li>
                   <li><a                href="#" data-content="trailer">TRAILER</a></li>
                   <li><a                href="#" data-content="cast">CAST</a></li>
                   <li><a                href="#" data-content="review">REVIEW</a></li>
                 </ul>
               </nav>
             </section>
          </div>
        </div>
      </div>
    </div>
    '''

    script_template = u'''
    <script type="text/javascript" charset="utf-8">

        // need to reset the modal active tab and remove trailer etc... when closed
        $(".modal").on("hidden.bs.modal", function(e) {

            var targetModal = $(e.target);
            var movieID = targetModal.attr("id");

            // reset the active tab and content
            $("#"+movieID+" .cnt .top .content").removeClass("active");
            $("#"+movieID+" .cnt .top .content").first().addClass("active");
            $("#"+movieID+" .cnt .bottom .menu a").removeClass("active");
            $("#"+movieID+" .cnt .bottom .menu a").first().addClass("active");

            // remove the trailer and reset trailer init state
            $("#"+movieID+"-trailer-video-container").empty();
            $("#"+movieID+" .cnt .top .content.trailer").first().addClass("trailer-need-init");

        });

        $(".cnt .bottom .menu").on("click", "a", function() {

            // find the correct modal first by looking at id
            var movieID = $(this).closest(".modal").attr("id");

            var contentID = $(this).attr("data-content");
            var targetTab = $("#"+movieID+"-"+contentID);
            $("#"+movieID+" .cnt .top .content").removeClass("active");
            targetTab.addClass("active");

            // if the tab is trailer, initialize the youtube player and play immediately
            if(targetTab.hasClass("trailer-need-init")) {
                setupYoutubeTrailer(movieID);
                targetTab.removeClass("trailer-need-init");
            }

            $("#"+movieID+" .cnt .bottom .menu a").removeClass("active");
            $(this).addClass("active");
        });

        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $(".trailer-video").empty();
        });

        // setup trailer youtube iframe
        function setupYoutubeTrailer(movieID) {
            var container = $("#"+movieID+"-trailer-video-container");
            var trailerYouTubeId = container.attr("data-content");
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            container.empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        }

    </script>
    '''

    synopsis_template = u'''
    <div class="synopsis" style="background-image:url('{backdrop}');">
      <div class="bg"></div>
      <div class="should-be-relative">
        <div class="title">{title}</div>
        <section class="top-group">
          <div class="score">{score}</div>
          <div class="certification">{certification}</div>
          <div class="year">{year}</div>
          <div class="runtime">{runtime} min</div>
        </section>
        <section class="hr"></section>
        <div class="overview clearfix">
          <div class="left">
            <img class="poster" src="{poster}" width="100"/>
          </div>
          <div class="right">
            <div style="min-height:100px">{overview}</div>
            <br/>
            <div class="genres">{genres}</div>
            <!--genres-->
          </div>
        </div>
        <!--.overview-->
      </div>
    </div>
    '''

    trailer_template = u'''
    <div class="scale-media trailer-video" id="{movieID}-trailer-video-container" data-content="{youtubeID}"></div>
    '''

    cast_template = u'''
    <div class="cast-list">{actor_list}</div>
    '''

    actor_template = u'''
    <div class="cast-list-actor clearfix">
        <div class="actor-avatar-panel">
            <img class="avatar" src="{avatar_url}" width="185">
        </div>
        <div class="actor-info-panel">
            <div class="actor-name">{actor_name}</div>
            <div class="actor-as">as</div>
            <div class="character-name">{character_name}</div>
        </div>
    </div>
    '''

    def create_cast_html(self, moviedb_movie):
        actors = ''
        for cast in moviedb_movie.moviedb_json['credits']['cast']:
            actors += ExtraCredit.actor_template.format(avatar_url=cast['profile_path'],
                                                        character_name=cast['character'],
                                                        actor_name=cast['name'])
        return ExtraCredit.cast_template.format(actor_list=actors)

    review_list_template = u'''
    <div class="review-list">
        <div class="review-section-header">
            <span class="review-movie-name">{movie_name}</span>
            <span class="review-movie-year">({movie_year})</span>
        </div>
        <div class="review-list-section">{review_list}</div>
    </div>
    '''

    review_template = u'''
    <div class="review">
        <div class="review-item-header">
            <span>by</span>
            <span class="reviewer-name">{reviewer_name}</span>
        </div>
        <div class="review-item-content">{review_content}</div>
    </div>
    '''

    def create_review_html(self, moviedb_movie):

        _paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

        def nl2br(content):
            # from http://flask.pocoo.org/snippets/28/
            return u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') for p in _paragraph_re.split(content))

        reviews = ''
        for review in moviedb_movie.moviedb_json['reviews']['results']:
            reviews += ExtraCredit.review_template.format(reviewer_name=review['author'],
                                                          review_content=nl2br(review['content']))
        if reviews == '':
            reviews = 'It appears that The Movie DB has no reviews for this movie :('
        return ExtraCredit.review_list_template.format(movie_name=moviedb_movie.title,
                                                       movie_year=moviedb_movie.year,
                                                       review_list=reviews)

