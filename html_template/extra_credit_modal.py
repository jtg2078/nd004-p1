# coding: utf-8

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
        return ExtraCredit.modal_template.format(movie_id=moviedb_movie.movie_id,
                                                 synopsis_tab=synopsis,
                                                 trailer_tab=trailer)

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
        .modal-dialog {
          width: 80%;
          height: 80%;
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
        }
        .cnt .top .content {
          display:none;
          color: #fff;
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
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: black;
            padding-bottom:50px;
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
                <div id="{movie_id}-cast" class="content">cast</div>
                <div id="{movie_id}-review" class="content">review</div>
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
    <div class="synopsis">
        <div class="title">{title}</div>
        <div class="overview">{overview}</div>
        <div class="poster">{poster}</div>
        <div class="trailer">{trailer}</div>
        <div class="genres">{genres}</div>
        <div class="score">{score}</div>
        <div class="certification">{certification}</div>
        <div class="year">{year}</div>
        <div class="backdrop">{backdrop}</div>
        <div class="runtime">{runtime}</div>
    </div>
    '''

    trailer_template = u'''
    <div class="scale-media trailer-video" id="{movieID}-trailer-video-container" data-content="{youtubeID}"></div>
    '''
