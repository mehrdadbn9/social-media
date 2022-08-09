# social-media

this is a python social media app that has been written with Django and DRF

Used Tech Stack

1. [Django](https://docs.djangoproject.com/en/4.0)
2. [Sqlite](https://www.sqlite.org/docs.html)
3. [Bootstrap](https://getbootstrap.com/)

## Installation

```bash
    $ python -m venv venv
    $ source venv/Scripts/activate
    (venv) pip install -r requirements.txt
    (venv) cd social_media
    (venv) python manage.py makemigrations
    (venv) python manage.py migrate
    (venv) python manage.py createsuperuser
    (venv) python manage.py runserver
```

## Current Features:

- [x] Login/Register
- [x] comment on the particular post
- [x] Like, Comment / Reply, Save and Search posts</li>
- [x] Follow and Unfollow users to view their posts</li>
- [x] Friend Request</li>
- [x] Notifications</li>

In  ```version 2``` of this project would update with new features
of python, django and ... also project would have Test and
better frontend that would have said in advance as well.

## To Do:

- [ ] Chats using websockets</li>
- [ ] Video Calls</li>
- [ ] Pytest
- [ ] Docker
- [ ] Redis and Celery suitable usage