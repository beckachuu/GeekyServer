### Port: 5000

---
---

### URL:

- GET /login
- GET /logout
---
- GET /my_account
- POST /my_account
> JSON structure:
  { username: ...,
    name: ...,
    phone: ...,
    profile_pic: ...,
    theme: ... }
- GET /my_ratings
- POST /subscribe?author_id=...
- POST /change_role?username=...&user_role=... (0: normal user, 1: admin)
---
- GET / : main page (not finished)
- GET /books/search?query=... : search books by authors or books name
- GET /books?book_id=... : get detail info of a book
- POST /books : post a new book (admin only)
> JSON structure:
> { title: ...(mandatory),
    translator: ...,
    cover: ...,
>   page_count: ...(mandatory),
>   public_year: ...(mandatory),
>   content: ...(mandatory),
>   descript: ...(mandatory),
    republish_count=... }

- PUT /books?book_id=... : change detail for a book (admin only)
---
- GET /authors/search?query=...
- GET /authors?author_id=...
- POST /authors
> JSON structure:
> { author_name: ...(mandatory),
    bio: ...,
    social_account: ...,
    website: ...,
    profile_pic: ..., }
