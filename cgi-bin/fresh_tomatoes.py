#!/usr/bin/python
import json, re, trailers

# A single movie entry html template
movie_tile_content = '''
<div class="col-xs-12 col-sm-12 col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{image}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = []
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content.append(movie_tile_content.format(
            movie_title=movie.title,
            image=movie.image,
            trailer_youtube_id=trailer_youtube_id	
    	))

    return content

print "Content-type: application/json"
print
response={ "movies" : create_movie_tiles_content(trailers.getMovies()) }
print(json.JSONEncoder().encode(response))
