from locust import HttpUser, task, between

import urllib

import google.auth.transport.requests
import google.oauth2.id_token
from google.auth import impersonated_credentials


CLOUD_RUN_URL = "***"


def get_token(endpoint, audience):

    req = urllib.request.Request(endpoint)

    auth_req = google.auth.transport.requests.Request()

    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

    return id_token


class QuickStartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def root(self):
        self.client.get("/")

    def on_start(self):
        url = CLOUD_RUN_URL
        token = get_token(url, url)
        self.client.headers={"Authorization": f"Bearer {token}"}
