import sqlalchemy as sql

from init_app import db
from src.models.ratings_md import Ratings


def get_book_ratings_by_stars(book_id, stars):
    ratings_query = Ratings.query.filter_by(book_id=book_id, stars=stars)
    ratings = {}
    for rating in ratings_query:
        ratings[rating.author_id] = rating.author_name

    if stars == 1:
        key = 'one_star'
    elif stars == 2:
        key = 'two_star'
    elif stars == 3:
        key = 'three_star'
    elif stars == 4:
        key = 'four_star'
    elif stars == 5:
        key = 'five_star'

    return {key: ratings, 'count': ratings.__len__}
