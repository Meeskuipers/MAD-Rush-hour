# 07-11-2018
# Mees Kuipers
# 11288477
"""
This script scrapes IMDB and outputs a CSV file with highest rated movies.
"""

import csv
import re
from requests import get
from self import self
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

TARGET_URL = "https://www.imdb.com/search/title?title_type=feature&release_date=2008-01-01,2018-01-01&num_votes=5000,&sort=user_rating,desc"
BACKUP_HTML = 'movies.html'
OUTPUT_CSV = 'test.csv'


def extract_movies(dom):
    """
    Extract a list of highest rated movies from DOM (of IMDB page).
    Each movie entry should contain the following fields:
    - Title
    - Rating
    - Year of release (only a number!)
    - Actors/actresses (comma separated if more than one)
    - Runtime (only a number!)
    """

    movies = dom.find_all(class_='lister-item-content')
    self.movie_list = []
    for movie in movies:
        acteur_list = []
        one_movie = []
        title = movie.h3.a.string
        year = movie.find(class_='lister-item-year text-muted unbold').string.strip(")").replace("(", "")
        if ' ' in year:
            year = year.split(" ")[1]
        rating = movie.find(class_='inline-block ratings-imdb-rating').strong.string
        for acteur in movie.find_all('a', attrs={'href': re.compile("ref_=adv_li_st_")}):
            acteur_list.append(acteur.string)
        runtime = movie.find(class_='runtime').string
        one_movie.extend([title, rating, year, acteur_list, runtime])
        self.movie_list.append(one_movie)

    #print(actors[number].string)
    # ADD YOUR CODE HERE TO EXTRACT THE ABOVE INFORMATION ABOUT THE
    # HIGHEST RATED MOVIES
    # NOTE: FOR THIS EXERCISE YOU ARE ALLOWED (BUT NOT REQUIRED) TO IGNORE
    # UNICODE CHARACTERS AND SIMPLY LEAVE THEM OUT OF THE OUTPUT.

    return [self.movie_list]   # REPLACE THIS LINE AS WELL IF APPROPRIATE


def save_csv(outfile, movies):
    """
    Output a CSV file containing highest rated movies.
    """
    writer = csv.writer(outfile, delimiter=';')
    writer.writerow(['Title', 'Rating', 'Year', 'Actors', 'Runtime'])
    for movie in self.movie_list:
        acteurs = ", ".join(map(str, movie[3]))
        writer.writerow([movie[0], movie[1], movie[2], acteurs, movie[4]])
    # ADD SOME CODE OF YOURSELF HERE TO WRITE THE MOVIES TO DISK


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('The following error occurred during HTTP GET request to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


if __name__ == "__main__":

    # get HTML content at target URL
    html = simple_get(TARGET_URL)

    # save a copy to disk in the current directory, this serves as an backup
    # of the original HTML, will be used in grading.
    with open(BACKUP_HTML, 'wb') as f:
        f.write(html)

    # parse the HTML file into a DOM representation
    dom = BeautifulSoup(html, 'html.parser')

    # extract the movies (using the function you implemented)
    movies = extract_movies(dom)

    # write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'w', newline='') as output_file:
        save_csv(output_file, movies)
