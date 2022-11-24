import os

from flask_restful import Api

from init_app import app
from src.controller.authors_ctrl import *
from src.controller.books_ctrl import *
from src.controller.collections_ctrl import *
from src.controller.noti_ctrl import *
from src.controller.users_ctrl import *

# this is to set our environment to https because OAuth 2.0 only supports https environments
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api = Api(app)


api.add_resource(Login, '/login')
api.add_resource(Callback, '/callback')
api.add_resource(Logout, '/logout')


api.add_resource(MyAccount, '/my_account')
api.add_resource(ChangeRole, '/new_role')


api.add_resource(MainPage, '/')
api.add_resource(BooksSearch, '/books/search')
api.add_resource(BookDetail, '/books/<int:book_id>')

# api.add_resource(Authors, '/authors/all')
api.add_resource(AuthorsSearch, '/authors/search')
api.add_resource(AuthorInfo, '/authors/<int:book_id>')


if __name__ == '__main__':
    from src.utils import *

    app.run(debug=True)
