### Port: 5000

---
---

### URL:
(Fields that aren't mandatory: still need to be included, values can be set to null)

- GET /login
- GET /logout
---
- GET /my_account
- POST /my_account
> JSON structure:
  { "username": string,
    "name": string,
    "phone": string,
    "profile_pic": string,
    "theme": int }
- DELETE /my_account
- GET /my_ratings
- POST /subscribe?author_id=<int>
- POST /change_role?username=<string>&user_role=<int> (0: normal user, 1: admin)
- POST /ban_user?username=<string>&restrict_due=<datetime> (restrict_due format: Year-Month-Day Hour:Minute:Second)
---
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
---
- GET /authors/search?query=<string>
- GET /authors?author_id=<int>
- POST /authors
> JSON structure:
  { "author_name": string (mandatory),
    "bio": string,
    "social_account": string,
    "website": string,
    "profile_pic": string }
