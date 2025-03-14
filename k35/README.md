# Weblog Hosting Site

This is a Flask-based web application that allows users to register, log in, and create blogs. Users can create new blog entries, update their blogs by adding new entries, view and edit their own past entries, and view the blogs of other users. Users cannot edit the blogs of other users. SQLite3 is used as the backend data storage system.

## Features
- User Registration
- User Login and Logout
- Create new blog entries
- Edit and update own blog entries
- View own past blog entries
- View blogs of other users

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Altaccount595/weblog-hosting-site.git
    cd weblog-hosting-site
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Initialize the SQLite3 database:
    ```sh
    python app.py
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`

3. Register a new account or log in with an existing account.

4. Create, edit, and view blog entries.

## Project Structure

```
weblog-hosting-site/
│
├── templates/
│   ├── create_blog.html
│   ├── edit_blog.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── user_blogs.html
│   └── view_blog.html
│
├── app.py
└── README.md
```

## Dependencies

- Flask
- Werkzeug
- SQLite3

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask documentation: https://flask.palletsprojects.com/
- SQLite documentation: https://www.sqlite.org/docs.html
- Werkzeug documentation: https://werkzeug.palletsprojects.com/
