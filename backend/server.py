from flask import Flask, render_template, request
from scraper import InstaScraper
import json

insta_scraper = InstaScraper()
app = Flask(__name__)


@app.route("/login", methods=['POST'])
def login():
    data = json.loads(request.data.decode("utf-8"))
    insta_scraper.login_with_auth(data['username'], data['password'])
    return {
        "data": {
            "username": data['username'],
            "password": data['password']
        }
    }


@app.route("/get_user/<username>")
def get_user(username: str):
    return {
        "data": insta_scraper.get_user_by_username(username)
    }


@app.route("/get_user_followers/<user_id>")
@app.route("/get_user_followers/<user_id>/<max_id>")
def get_user_followers(user_id: str, max_id="0"):
    return {
        "data": insta_scraper.get_friends_list(user_id, "followers", max_id)
    }


@app.route("/get_search/<query>")
def get_search(query):
    return {
        "data": insta_scraper.get_search_result(query)
    }


@app.route("/get_user_media/<end_cursor>/<user_id>")
def get_user_media(end_cursor, user_id):
    return {
        "data": insta_scraper.get_user_media(end_cursor, user_id)
    }


if __name__ == "__main__":
    app.run()
