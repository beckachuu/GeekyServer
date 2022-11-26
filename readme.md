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
    "theme": number }
- GET /my_ratings
- POST /subscribe?author_id=...
- POST /change_role?username=...&user_role=... (0: normal user, 1: admin)
- POST /ban_user?user_name=...&restrict_due=... (restrict_due format: Year-Month-Day Hour:Minute:Second)
---
- GET / : main page (not finished)
- GET /books/search?query=... : search books by authors or books name
- GET /books?book_id=... : get detail info of a book
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
- GET /authors/search?query=...
- GET /authors?author_id=...
- POST /authors
> JSON structure:
  { "author_name": string (mandatory),
    "bio": string,
    "social_account": string,
    "website": string,
    "profile_pic": string }
