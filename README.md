# Postgram API

REST API for a simple social blog platform built with Django REST Framework.

## Features

* User registration
* User authorization with Token Authentication
* Post list API
* Post detail API
* Create, update and delete posts
* Comments for posts
* Custom pagination
* PostgreSQL database
* Swagger and ReDoc API documentation
* Author-only update and delete permissions for posts

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* DRF Token Authentication
* drf-yasg

## Project Structure

```text
postgram-api/
├── blog/          # Project settings, main URLs and Swagger configuration
├── post/          # Posts and comments API
├── users/         # Registration and authorization
├── requirements.txt
├── manage.py
└── README.md
```

## API Endpoints

### Posts

```text
GET     /api/v1/posts/
POST    /api/v1/posts/
GET     /api/v1/posts/<id>/
PUT     /api/v1/posts/<id>/
DELETE  /api/v1/posts/<id>/
```

### Comments

```text
GET     /api/v1/posts/<id>/comments/
POST    /api/v1/posts/<id>/comments/
```

### Users

```text
POST    /api/v1/users/registration/
POST    /api/v1/users/authorization/
```

### Documentation

```text
/swagger/
/redoc/
```

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET=your_secret_key
DEBUG=on

DB_NAME=postgram_db
DB_USER=postgram_user
DB_PASSWORD=postgram_password
DB_HOST=localhost
DB_PORT=5432
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Saikal-03/postgram-api.git
cd postgram-api
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Run the project:

```bash
python manage.py runserver
```

## Status

Educational backend project created while learning Django REST Framework, PostgreSQL, Token Authentication and API development