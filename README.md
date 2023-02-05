# Kitchen-project
Django kitchen management project

#### Checkout it

[Kitchen service project deployed to Render](https://kitchen-project.onrender.com/)

 #### Features

* Authentication functionality for Cook/User
* Managing dishes/dish_type from website interface
* Powerful admin panel for advanced managing

#### Test user

* User: `admin`
* Password: `2105Inna75`

#### Demo
![Kitchen_project](static/kitchen/img/kitchen-photo.jpg)

#### Installation
##### Python3 must be already installed.

```
git clone  https://github.com/InnaKushnir/my-django-project.git

cd my-project

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

set DB_HOST=<your db hostname>

set DB_NAME=<your db name>

set DB_USER=<your db username>

set DJANGO_SECRET_KEY=<your django secret key>

set DB_PASSWORD=<your db user password>

python manage.py migrate

python manage.py runserver 
```