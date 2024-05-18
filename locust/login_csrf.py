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




    @task
    def t(self):
        res=self.client.get("/accounts/my_orders/")
        if res.status_code==200 and "Billing Name" in res.text:
            print("pass")
        else:
            print('fail')










class MyUser(HttpUser):
    wait_time = constant(1)
    host = "http://127.0.0.1:8000"
    tasks = [MyTaskSet]
