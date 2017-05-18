import webbrowser
from video import Video

class Movie(Video):
    
    """This class provides a way to store movie related information."""
    VALID_RATINGS = ["G","PG","PG-13","R","NC-17"] #Rating as given by the movie rating system.
    #Reference: https://en.wikipedia.org/wiki/Motion_Picture_Association_of_America_film_rating_system

    def __init__(self,movie_title, duration,rating,movie_storyline, 
    poster_image_url,trailer_youtube_url):
        Video.__init__(self,movie_title,duration)
        #self.title=movie_title
        #self.duration = duration
        if(rating in self.VALID_RATINGS):
            self.rating = rating
        else:
            self.rating = "Unrated"
        
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


    #The method to initiate the display of the YouTube hosted trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

        