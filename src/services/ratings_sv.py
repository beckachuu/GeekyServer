from init_app import db
from src.const import *
from src.controller.auth import admin_only, get_current_user
from src.models.books_md import Books
from src.models.ratings_md import Ratings


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


def get_own_ratings():
    user = get_current_user()
    ratings = Ratings.query.filter_by(username=user.username)
    result = []
    for rating in ratings:
        result.append(rating.get_json())
    if len(result) > 0:
        return result, OK_STATUS
    return None, NOT_FOUND


def update_current_rating(username, book_id):
    average = db.session.query(db.func.avg(Ratings.stars)).filter_by(
        book_id=book_id, username=username)

    book = Books.query.filter_by(book_id=book_id).first()
    book.current_rating = average
    db.session.commit()


def post_my_rating(json):
    user = get_current_user()
    rating = Ratings(user.username)
    if rating.update_book_id(json[BOOK_ID]) and rating.update_content(json[CONTENT]) and rating.update_stars(json['stars']):
        try:
            db.session.add(rating)
            db.session.commit()

            update_current_rating(user.username, json[BOOK_ID])
            return OK_STATUS
        except:
            return CONFLICT
    return BAD_REQUEST


def edit_my_rating(json):
    user = get_current_user()

    try:
        rating = Ratings.query.filter_by(
            username=user.username, book_id=json[BOOK_ID]).first()
        if rating.update_content(json[CONTENT]) or rating.update_stars(json['stars']):
            db.session.commit()

            update_current_rating(user.username, json[BOOK_ID])
            return OK_STATUS
        return NO_CONTENT
    except:
        return BAD_REQUEST


@ admin_only()
def remove_rating():
    pass
