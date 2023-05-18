libraries

asgiref==3.5.1
bcrypt==4.0.1
black==22.3.0
click==8.1.3
colorama==0.4.4
distlib==0.3.6
Django==3.2
django-rest-framework==0.1.0
django-widget-tweaks==1.4.8
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
filelock==3.8.2
mypy-extensions==0.4.3
pathspec==0.9.0
platformdirs==2.5.2
psycopg2==2.9.6
PyJWT==2.4.0
pytz==2022.1
sqlparse==0.4.2
tomli==2.0.1
tzdata==2022.1
virtualenv==20.17.1

signup JSON
{
  "user_email": "denzel@gmail.com",
  "password": "password1234",
  "First_Name": "John",
  "Last_Name": "Doe"
}


Login JSON
{
  "email": "denzel@gmail.com",
  "password": "password1234"
}









http://127.0.0.1:8000/api/auth/login/   login endpoint
http://127.0.0.1:8000/backend/signup/   signup endpoint
