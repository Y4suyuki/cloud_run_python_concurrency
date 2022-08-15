from locust import HttpUser, task, between


class QuickStartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def root(self):
        self.client.get("/slow")

    def on_start(self):
        pass
