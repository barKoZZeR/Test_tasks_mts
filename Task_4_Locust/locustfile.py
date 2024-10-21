from locust import HttpUser, TaskSet, task, between


class ApiTasks(TaskSet):

    @task
    def inverse(self):
        self.client.post("/api/inverse/", json={"key1": "value1"})

    @task
    def unstable(self):
        self.client.get("/api/unstable/")


class ApiUser(HttpUser):
    tasks = [ApiTasks]
    wait_time = between(1, 2)
    host = "http://127.0.0.1:8000"