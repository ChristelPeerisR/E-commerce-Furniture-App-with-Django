# E-commerce-Furniture-App-with-Django

## Live Demo:

https://github.com/ChristelPeerisR/E-commerce-Furniture-App-with-Django/assets/83603996/b71c7759-c980-4458-9820-7300f4e5911c

## Functions

## Admin
- Create Admin account and Login.
- Can add new products, blogs and all required models.

## User
- Create user login (User will receive confirmation mail).
- Can add products to cart.
- Can filter products upon its's category, min-max price and offers.
- Can search for paticular products.
- Can send message to the admin using. 
- Can view Gallery.
- Can read Blogs.

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Download This Project Zip Folder and Extract it
Open Terminal and Execute Following Commands :
```bash
python -m pip install -r requirements. txt
- Move to project folder in Terminal. Then run following Commands :
```bash
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
Now enter following URL in Your Browser Installed On Your Pc
http://127.0.0.1:8000/

CHANGES REQUIRED FOR CONTACT US PAGE
In settins.py file, You have to give your email and password
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'

CHANGES REQUIRED FOR DATABASE MANAGEMENT
In settins.py file, You have to give your username and password
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB Name',
        'USER':'postgres',
        'PASSWORD':'Ypur password',
        'HOST':'localhost'
    }
}

## Contact & Feedback
Email: christelpeeris@gmail.com

