import webbrowser

# The 'Movie' class provides the structure for our movie instances
# defined in entertainment_center.py.
# Each instance has a title, poster image, and trailer.
# The class includes a function to open trailers in a new browser window


class Movie:

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
