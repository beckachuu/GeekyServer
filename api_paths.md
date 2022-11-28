### Port: 5000

---

Database diagram:

![db_diagram](https://user-images.githubusercontent.com/78261243/204224617-d6a3726a-2421-40bf-8246-d8ccf496d670.png)

---

### URLs:
(Fields that aren't mandatory: still need to be included, values can be set to null)

- GET /login
- GET /logout

---

#### Account APIs
- GET /my_account
- POST /my_account
> JSON structure:
  { "username": string,
    "name": string,
    "phone": string,
    "profile_pic": string,
    "theme": int }

- DELETE /my_account
- GET /my_notification

#### Ratings APIs
- GET /my_ratings
- POST /my_ratings
> JSON structure:
  { "book_id": int (mandatory),
    "stars": int (mandatory),
    "content": string }
- PUT /my_ratings : edit rating
> JSON structure: same as above

#### Collections APIs (NOT TESTED lol sorry my back hurts so bad at this point...)
- POST /my_collections/<string:collname>
- PATCH /my_collections/<string:collname>?new_name=<string> : rename collection
- PATCH /books?book_id=<int>&coll_name=<string> : add book to collection
- PUT /my_collections/<string:collname>?book_id=<string> : remove book from collection
- DELETE /my_collections/<string:collname>

#### Admin APIs
- POST /change_role?username=<string>&user_role=<int> (0: normal user, 1: admin)
- POST /ban_user?username=<string>&restrict_due=<datetime> (restrict_due format: Year-Month-Day Hour:Minute:Second)

---

#### Books APIs
- GET / : main page (not finished)
- GET /books/search?query=<string> : search books by authors or books name
- GET /books?book_id=<int> : get detail info of a book
- POST /books : post a new book (admin only)
> JSON structure:
  { "title": string (mandatory),
    "translator": string,
    "cover": string,
    "page_count": int (mandatory),
    "public_year": int (mandatory),
    "content": string (mandatory),
    "descript": string (mandatory),
    "republish_count": int,
    "genres": string LIST (mandatory),
    "authors": int LIST (for author_id) (mandatory) }

- PUT /books : change detail for a book (admin only)
> JSON structure: same as above, plus "book_id" (POST /books)
- DELETE /books?book_id=<int>

---

#### Authors APIs
- GET /authors/search?query=<string>
- GET /authors?author_id=<int>
- POST /authors
> JSON structure:
  { "author_name": string (mandatory),
    "bio": string,
    "social_account": string,
    "website": string,
    "profile_pic": string }
- POST /subscribe?author_id=<int>