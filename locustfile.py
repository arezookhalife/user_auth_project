from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def home(self):
        self.client.get("/accounts/home/")

    @task
    def profile(self):
        self.client.get("/accounts/profile/")

    @task
    def login(self):
        self.client.get("/accounts/login/")

    @task
    def search(self):
        self.client.get("/accounts/search/?query=test")