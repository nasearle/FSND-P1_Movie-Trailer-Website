import fresh_tomatoes
import media

# Below are several instances of the class 'Movie' defined in media.py.
# Each instance has a title, link to poster, and link to its trailer
# on YouTube.

toy_story = media.Movie("Toy Story",
                        ("https://upload.wikimedia.org/wikipedia"
                         "/en/1/13/Toy_Story.jpg"),
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     ("https://upload.wikimedia.org/wikipedia"
                      "/en/b/b0/Avatar-Teaser-Poster.jpg"),
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

lotr = media.Movie("Lord of the Rings",
                   ("https://upload.wikimedia.org/wikipedia"
                    "/en/0/0c/The_Fellowship_Of_The_Ring.jpg"),
                   "https://www.youtube.com/watch?v=V75dMMIW2B4")

district_9 = media.Movie("District 9",
                         ("https://upload.wikimedia.org/wikipedia"
                          "/en/d/d7/District_nine_ver2.jpg"),
                         "https://www.youtube.com/watch?v=DyLUwOcR5pk")

spirited_away = media.Movie("Spirited Away",
                            ("http://www.onlineghibli.com/spirited_away"
                             "/article-pics/sw-us-poster.jpg"),
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

mip = media.Movie("Midnight in Paris",
                  ("https://upload.wikimedia.org/wikipedia/en"
                   "/9/9f/Midnight_in_Paris_Poster.jpg"),
                  "https://www.youtube.com/watch?v=FAfR8omt-CY")

# The movies are put into an array to pass into open_movies_page()

movies = [toy_story, avatar, lotr, district_9,
          spirited_away, mip]

fresh_tomatoes.open_movies_page(movies)
