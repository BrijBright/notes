# varigfy response with catch_respose parameter

from locust import HttpUser,constant,task,SequentialTaskSet

class myseqtask(SequentialTaskSet):
    wait_time=constant(2)

    @task
    def getting_url(self):
        with self.client.get('/accounts/login/',catch_response=True) as response1:
            if response1.status_code==200 and "Don't have account?" in response1.text:
                csrf=response1.cookies.get('csrftoken')
                response1.success()
            else:
                response1.failure('fail to login')

        data={'email': 'kajoge9920@mcatag.com', 'password': 'temp'}
        headers={'X-csrftoken':csrf}
        with self.client.post('/accounts/login/',catch_response=True,data=data,headers=headers) as response2:
            if response2.status_code==200 and 'Edit Profile' in response2.text:
                response2.success()
            else:
                response2.failure(f'not able to login wit cod error{response2.status_code}')







class myuser(HttpUser):
    host='http://localhost:8000'
    tasks=[myseqtask]
