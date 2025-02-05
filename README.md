# Code With Abdiwali Blog
My personal blog about technology articles. topic includes Django, Spring, RESTful API , Java, Python and more..

## Use Cases
- User can register/login.
- Registered user can review/comment blog's aritcles.
- Registered and anonymous user can receive latest articles via email
- Registered can up vote articles for userfullness.
- Only admin user can add, modify, delete and update article.
- Only admin user can publish articles.
- User can filter blog's articles by cateogry and tags
- User' can view my profile.
- User's switch theme for accessibility

## Models
- User
- Article model
- Comment
- Category
- Project
- Tag
- Subscriber

## ERD
![CodeWithAbdiwali](https://github.com/user-attachments/assets/32f49b75-1a23-41fd-b1bc-abf7c124f42a)

## RESTful API Endpoints

### Comments
| HTTP Method | Endpoint                  | Description                          | Required Arguments               | Example Request Body                          | Example Response                              |
|-------------|---------------------------|--------------------------------------|----------------------------------|-----------------------------------------------|-----------------------------------------------|
| `GET`       | `/comments`               | Get all top-level comments           | None                             | None                                          | `[{ "id": 1, "content": "Great post!", "user_id": 101, "subcomments": [...] }]` |
| `GET`       | `/comments/{id}`          | Get a specific comment by ID         | `id` (in URL path)               | None                                          | `{ "id": 1, "content": "Great post!", "user_id": 101, "subcomments": [...] }` |
| `POST`      | `/comments`               | Create a new comment                 |  `title` `content`,`article`,`user`,`parent (nullable)`,              | `{ "title": "Welcome", "conent": "I am abdiwali", "article":"EQWJTPGJASPJEWR",  "user":"EWTPFNMSDPGTIJER"}`      | `{ "title": "Welcome", "conent": "I am abdiwali", "article":"EQWJTPGJASPJEWR",  "user":"EWTPFNMSDPGTIJER"}` ` |
| `POST`      | `/comments/{id}/reply`    | Create a subcomment (reply)          |`title` `content`,`article`,`user`,`parent`,| `{ "title": "Welcome", "conent": "I am abdiwali", "article":"EQWJTPGJASPJEWR",  "user":"EQWJTPGJASPJEWR",  "parent":"EQWJTPGJASPJEWR", }`    |`{ "title": "Welcome", "conent": "I am abdiwali", "article":"EQWJTPGJASPJEWR",  "user":"EQWJTPGJASPJEWR",  "parent":"EQWJTPGJASPJEWR", }` |
| `PUT`       | `/comments/{id}`          | Update a comment                     | `id` (in URL path), `title`, `content`    | `{ "title": "My title", "content": "Updated comment!" }`           | `{"title": "My title", "content": "Updated comment!", "user_id": 101 }` |
| `DELETE`    | `/comments/{id}`          | Delete a comment                     | `id` (in URL path)               | None                                          | `{ "message": "Comment deleted successfully" }` |


    
  
