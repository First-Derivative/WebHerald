# WP_Coursework3

---
## Design Links
### [DB Schema ER Diagram](https://app.diagrams.net/#G1bOJjas5DwYNGpUWEC8jXjltAUl_HOhFL)

## Important Links
### [For Merge Conflict Reference](https://www.youtube.com/watch?v=CKAdoAR0ykc&ab_channel=AppleJuiceTeaching)
### [Django Docs: Models Fields](https://docs.djangoproject.com/en/3.1/ref/models/fields/)
### [Django Docs: Middleware](https://docs.djangoproject.com/en/3.1/topics/http/middleware/)

## Useful Links:
### [Online Python IDE for quick testing](https://repl.it/languages/python3)
### [Markdown (syntax) Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---
#### Notes for Discussion
1. Bugs

#### known bugs
1. When deleting the last comment on an article: the no comments message doesn't appear
2. Line breaks are not read for a new comment in comment_content
3. Timestamp for ajax comments different format than get request DOM
4. Timestamp for edited comments should be updated, can get updated timestamp from response.data
5. Posting a new comment should set window location to the new comment
6. Deleting parent comment does not delete child comments on DOM 

---
## Requirements:
1. Pillow
2. django-cleanup
