from locust import User, constant, events, TaskSet, task, SequentialTaskSet, HttpUser

class MyTaskSet(SequentialTaskSet):
    def __init__(self, parent):
        super().__init__(parent)
        self.csrf = ''
    wait_time = constant(5)

    def on_start(self):
        req = self.client.get('/accounts/login/', name='getting login page')
        self.csrf = req.cookies["csrftoken"]
        print('login page stats =', req.status_code)

        data = {'email': 'kajoge9920@mcatag.com', 'password': 'temp'}
        headers = {"X-CSRFToken": self.csrf}
        res = self.client.post("/accounts/login/", data=data, headers=headers)
        print("login status=", res.status_code)



    # update profile picture
    @task
    def t(self):
        req = self.client.get('/accounts/edit_profile/', name='for probile')
        self.csrf = req.cookies["csrftoken"]
        print('login page stats =', req.status_code)

        data = {
            "first_name": "Brijkishor",
            "last_name": "Gupta",
            "phone_number": "986531",
            "address_line_1": "123 Main Street",
            "address_line_2": "Apt 101",
            "city": "Cityville",
            "state": "Stateville",
            "country": "Countryland"
        }

        headers = {"X-CSRFToken": self.csrf}
        res = self.client.post("/accounts/edit_profile/", data=data, headers=headers)
        print("login status=", res.status_code)










class MyUser(HttpUser):
    wait_time = constant(1)
    host = "http://127.0.0.1:8000"
    tasks = [MyTaskSet]
