import sqlalchemy as sql

from init_app import db
from src.models.ratings_md import Ratings
from src.const import *


def get_ratings_by_stars(book_id, stars):
    ratings_query = Ratings.query.filter_by(book_id=book_id, stars=stars)
    ratings = []
    for rating in ratings_query:
        ratings.append(rating.get_json())

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
    else:
        return {}

    result = {}
    result[key] = {'ratings': None, 'count': None}
    result[key]['ratings'] = ratings
    result[key]['count'] = len(ratings)

    return result


def get_user_ratings(username):
    ratings = Ratings.query.filter_by(username=username)
    result = []
    for rating in ratings:
        result.append(rating.get_json())
    if len(result) > 0:
        return result, OK_STATUS
    return None, NOT_FOUND


def post_user_rating(username, rating_json):
    rating = Ratings()
    valid = False
