#!/usr/bin/env python

import webbrowser

class Movie():
	"""Movie class

	Attributes:
		title (str): the title of the movie
		storyline (str): summary of the movie's plot
		poster_image_url (str): link to image of movie's poster
		trailer_youtue_url (str): link to movie's trailer on YouTube
	"""
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url 
        self.trailer_youtube_url = trailer_youtube_url 

    def show_trailer(self):
    	"""Method to open movie's YouTube trailer
    	"""
        webbrowser.open(self.trailer_youtube_url)
