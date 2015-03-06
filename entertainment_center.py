import media
import fresh_tomatoes

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


fresh_tomatoes.open_movies_page([birdman, the_grand_budapest_hotel, whiplash, gone_girl, john_wick, five_armies, galaxy])


