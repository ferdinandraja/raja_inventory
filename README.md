# Assignment 2
## My application link
my link:

# Explanation
## 1.How do you implement the checklists? Explain in a step-by-step manner (not just copy-paste from the tutorial).
1. Create new Django project:
    - Create a virtual environment by running the following command.
    ```
    python3 -m venv env
    ```
    - Activate the virtual environment, in my case, use:
    ```
    source env/bin/activate
    ```
    - In the directory where I activated the virtual environment, I then create a file named `requirements.txt`.
    - Install the dependencies with this command `pip install -r requirements.txt`.
    - Create a Django project with this command `django-admin startproject raja_inventory.`
    - Add `"*"` to `ALLOWED_HOSTS` in `settings.py` for deployment.
    - I add a `.gitignore` file and because i use macbook, I also put `.DS_store` in my `.gitgignore file` such that there will be no error in push and pull to git process.
2. Create an app in the directory before named main.
    Run this command `python manage.py startapp main`
3. Register the main app into the project.
    - find `settings.py` in raja_inventory directory
    - find `INSTALLED_APPS` and add `main` to the dictionary
4. Create a new directory called templates inside main application. Then, create `main.html` inside the directory.
5. Modify the `models.py` file located within the main application to define a new model.
    Modify the `models.py` such that there is name,amount, and description in item app.
6. Creating and apply model migrations:
    - Run this code `python manage.py makemigrations` to create the migrations model
    - Run this code `python manage.py migrate` to apply the model
7. Modify `views.py`:
    - In my case, I add function `show_main` with `app`, `name`, and `class` that will be return by `main.html` that have been modified by adding {{`name of variables`}} on `main.html`
8. Configuring URL routing in `urls.py` to map the function in `views.py` to URL.
    - Import some configurations
    - Add app_name = 'main' into the urls.py
9. Add, commit, and push the project to github
10. Deploy in adaptable

## 2.Create a diagram explaining the flow of client requests to a Django web app and its response. Also in the diagram, explain the connections between urls.py, views.py, models.py, and the HTML file(s).
<img src="/asset/diagramPBPfinall.png">


## 3.What is the purpose of a virtual environment? Can we create a Django web app without a virtual environment?
    It purpose is to allows developers to create an isolated environment for their projects, with its own dependencies and Python version. This ensures that each dependencies are consistent and can be replicated in different environments. It is possible to create a Django web app without a virtual environment. But without a virtual environment, the dependencies for the project would be installed globally, which can lead to conflicts with other projects or system packages. 
## 4.What is MVC, MVT, and MVVM? Explain the differences between the three
    MVC is the most widely used arcitecture among the others. It separates the application into three main components: Model, View, and Controller. MVT is another variation of the MVC pattern that is used in web development frameworks like Django. It separates the application into three main components: Model, View, and Template
    MVVM is a relatively new architecture pattern that is commonly used in modern mobile and web applications. It separates the application into three main components: Model, View, and ViewModel.
    There are no major differences between MVC and MVT, except that for MVT the controller part is taken care of by the framework. On the other hand, MVVM facilitates a separation of development of the graphical user interface. The main difference between these patterns is the role of the mediator component and the entry point to the application.