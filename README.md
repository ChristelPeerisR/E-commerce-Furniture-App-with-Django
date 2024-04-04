# E-commerce-Furniture-App-with-Django

## Live Demo:

https://github.com/ChristelPeerisR/E-commerce-Furniture-App-with-Django/assets/83603996/b71c7759-c980-4458-9820-7300f4e5911c

## Functions

### Admin
- Create Admin account and Login.
- Can add new products, blogs and all required models.

### User
- Create user login (User will receive confirmation mail).
- Can add products to cart.
- Can filter products upon its's category, min-max price and offers.
- Can search for paticular products.
- Can send message to the admin using. 
- Can view Gallery.
- Can read Blogs.

## HOW TO RUN THIS PROJECT

### Prerequisites
- Python 3.12.0 installed (Ensure to select "Add to Path" during installation)

### Steps
1. Download the project ZIP folder and extract it.
2. Open your terminal or command prompt.

3. Install project dependencies by executing the following command:
```
python -m pip install -r requirements.txt
```
```
cd path/to/project/folder
```
```
py manage.py makemigrations
```
```
py manage.py migrate
```
```
py manage.py runserver
```
Once the server is running, open your web browser and enter the following URL:
```
http://127.0.0.1:8000/
```

These instructions provide clearer steps, organize the commands logically, and include a section on prerequisites for better understanding.

### CHANGES REQUIRED FOR CONTACT US PAGE
In settins.py file, You have to give your email and password<br>
EMAIL_HOST_USER = 'youremail@gmail.com'<br>
EMAIL_HOST_PASSWORD = 'your email password'<br>
EMAIL_RECEIVING_USER = 'youremail@gmail.com'<br>

### CHANGES REQUIRED FOR DATABASE MANAGEMENT
In settins.py file, You have to give your username and password<br>
DATABASES = {<br>
    'default': {<br>
        'ENGINE': 'django.db.backends.postgresql',<br>
        'NAME': 'DB Name',<br>
        'USER':'postgres',<br>
        'PASSWORD':'Ypur password',<br>
        'HOST':'localhost'<br>
    }<br>
}<br>

## Contact & Feedback
Email: christelpeeris@gmail.com

