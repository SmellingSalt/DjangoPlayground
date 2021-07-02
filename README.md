# DjangoPlayground
This is a repository I made to play around with django.

## Initial Setup

* Installing it with anaconda can be done with the following command

  ```bash
  conda install -c anaconda django 
  ```

* You can set up an empty project with the command

  ```bash
  django-admin startproject projectname
  ```

  * This creates a folder named `projectname` within which there will be some `.py` files in.

* You can test out the created project and a simple tutorial/documentation page by running a server with the created files. `cd`into the `projectname` folder and run

  ```bash
  python manage.py runserver
  ```

  * This sets up a website that can be accessed in the browser with `localhost:8000`
