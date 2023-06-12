import requests

API_URL = "https://jsonplaceholder.typicode.com"


class JSONPlaceholderAPI:
    def __init__(self):
        self.base_url = API_URL

    def get_posts(self):
        return requests.get(f"{self.base_url}/posts")

    def get_posts_by_id(self, _id=None):
        return requests.get(f"{self.base_url}/posts/{_id}")

    def post_posts(self, userId=None, title=None, body=None):
        json_dict = {"userId": userId, "title": title, "body": body}
        return requests.post(f"{self.base_url}/posts", json=json_dict)

    def delete_posts(self, _id=None):
        return requests.delete(f"{self.base_url}/posts/{_id}")