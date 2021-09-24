from django.test.client import Client

c = Client()
response = c.post('/login/', {'username': 'admin', 'password': 123})
response2 = c.post('/registration/', {'username': 'student2213', 'password': 123, 'confirm_password': 123, 'email': 'z_klimovich@bk.ru'})
print(response.status_code)
print(response.content)
print(response2.content)
print(response2.status_code)