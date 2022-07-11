import requests
import json
import os.path
from pprint import pprint
from instagramuser import InstagramUser


# from media import IGraphImage, IGraphVideo, IGraphSidecar, IChildrenGraphImage, IChildrenGraphVideo


class InstaScraper:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            "x-ig-app-id": "936619743392459",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.58",
            "x-csrftoken": "qQJv0hyg1k1EoV9j3N5QbzbRqyhGjgzo",
            "cookie": '''ig_did=B21CDBBD-A00E-4A2D-A79A-68F55DA52695; ig_nrcb=1; mid=YOzMDAALAAGZJwfrgNCC2X5jQDg0; datr=R01KYn5GMckMnqvGTMLrbPB4; csrftoken=qQJv0hyg1k1EoV9j3N5QbzbRqyhGjgzo; ds_user_id=20177310827; shbid="11196\05420177310827\0541688461289:01f7e377047ec236067198a855be21e574fd4b570374e1aae75582c9dea561985da04344"; shbts="1656925289\05420177310827\0541688461289:01f7c38ba52b068bd28d28af67436de3316c5e31527daf1796bb15ff9f3b50a02808b267"; sessionid=20177310827:55FxyXBNQn8U3y:25:AYe_Ga0kNDMFQSrNtc3Zkq92uDhJuoR0vaeWyJ80xg; rur="ASH\05420177310827\0541688596593:01f7057b1058c3b19ba7797bdbfed44300e2bfa0b03cf7434e188a9854555896eca658b5"''',
        }

    def make_get_request(self, url, params=""):
        # if not os.path.isfile("requests.json"):
        #     with open("requests.json", "w") as file:
        #         json.dump({"data": {}}, file)

        # with open("requests.json") as file:
        #     data = json.load(file)

        #     if request_type in data["data"]:
        #         print("LOCALDE BULUNDU!!!")
        #         return data["data"][request_type]

        # print("LOCALDE BULUNAMADI!")
        print("istek yapıldı!")
        session = requests.Session()
        res = session.get(url=url, params=params, headers=self.session.headers)

        return res.json()

        # try:
        #     with open("requests.json", "w") as file:
        #         data["data"][request_type] = res.json()
        #         json.dump(data, file)

        #     return res.json()
        # except requests.exceptions.JSONDecodeError:
        #     print(res.status_code)

    def login_with_auth(self, username, password):
        if os.path.isfile("headers.json"):
            print("kayıtlı kullanıcı bulundu")
            with open("headers.json") as file:
                data = json.load(file)
            self.session.headers.update(data["headers"])

            return

        print("kayıtlı kullanıcı bulunamadı")

        url = 'https://www.instagram.com/accounts/login/'
        url_main = url + 'ajax/'
        auth = {
            "enc_password": f"#PWD_INSTAGRAM:0:0:{password}",
            "username": username, }

        # to get csrf token
        req = self.session.get(url)

        self.session.headers.update({'x-csrftoken': req.cookies['csrftoken']})
        res = self.session.post(url_main, data=auth,
                                headers=self.session.headers)

        if res.status_code == 200:
            self.session.headers.update(
                {'x-csrftoken': res.cookies['csrftoken'], 'cookie': res.headers['Set-Cookie']})
            print(self.session.headers)

            update_res = self.session.get(
                f"https://i.instagram.com/api/v1/users/web_profile_info/{username}", headers=self.session.headers)

            pprint(update_res.headers)
            self.session.headers.update(
                {'cookie': update_res.headers['Set-Cookie']})

            with open("headers.json") as file:
                data = json.load(file)

            with open("headers.json", "w") as file:
                data["headers"] = self.session.headers
                json.dump(data, file)

            return res.json()
        return {"error": res.status_code}

    def get_user_by_username(self, username):
        url = "https://i.instagram.com/api/v1"
        params = {
            "username": username,
        }

        # get user data
        user_res = self.make_get_request(
            f"{url}/users/web_profile_info/", params)
        user_data = user_res["data"]["user"]

        # get user stories
        story_res = self.make_get_request(
            f"{url}/feed/user/{user_data['id']}/story/")
        story_data = story_res["reel"]

        # get user highlights
        highlights_res = self.make_get_request(
            f"{url}/highlights/{user_data['id']}/highlights_tray/")
        highlights_data = highlights_res["tray"]

        return {
            "user": user_data,
            "story": story_data,
            "highlights": highlights_data,
        }

    def get_friends_list(self, user_id, endpoint, max_id="0"):

        params = {
            "count": "12",
            "search_surface": "follow_list_page",
        }

        url = f"https://i.instagram.com/api/v1/friendships/{user_id}/{endpoint}/"

        if max_id != "0":
            params["max_id"] = max_id

        res = self.make_get_request(url, params)

        return res

    def get_user_media(self, end_cursor, user_id):
        url = "https://www.instagram.com/graphql/query/"
        params = {
            "query_hash": "69cba40317214236af40e7efa697781d"
        }

        variables = {
            "id": user_id,
            "first": "12",
            "after": end_cursor,
        }

        params["variables"] = json.dumps(variables)
        res = self.make_get_request(url, params)
        data = res["data"]

        return data

    def get_search_result(self, query):

        url = "https://www.instagram.com/web/search/topsearch/"
        params = {
            "context": "blended",
            "query": query,
            "include_reel": False,
        }

        res = self.make_get_request(url, params)
        return res
