# README for URL Shortener Project
# Project Overview

The URL Shortener is a web application that allows users to shorten long URLs into shorter, more manageable links. This project is built using Django, a powerful web framework for Python. The application provides a simple interface where users can enter a long URL and receive a shortened URL that can be used to redirect to the original URL.

## Features

- Shorten long URLs into a 5-character base62 short URL.
- Redirect short URLs to the original long URLs.
- Basic collision handling for short URL generation.
- Simple and modern user interface.

## Technologies Used

- Python
- Django
- HTML/CSS
- JavaScript

## Prerequisites

- Python 3.x
- Django 3.x or higher

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to set up the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Open your web browser and navigate to:

    ```bash
    http://127.0.0.1:8000/
    ```
