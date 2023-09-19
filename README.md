# Assignment 2
## My application link
my link: https://blackventory.adaptable.app/main/

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

# Assignment 3

# Explanation
## 1.What is the difference between POST form and GET form in Django?
    In Django, POST and GET are used to submit data to a web server, but both are not similar. 
1. For instance, the POST method is used for submitting data to the server  and should result in a change in the server's state. On the other hand, the GET method is used for requesting data from the server without causing any side effects or changes in the server's state.
2. Next, data that is submitted by POST method is not visible in the URL, while it is visible in GET method.

## 2.What are the main differences between XML, JSON, and HTML in the context of data delivery?
1. To begin with, XML treats all data text by default. On the other hand,JSON supports simple data types like strings, numbers, booleans, arrays, and objects. Where HTML which more focused on web structure,have specific tags for headings, paragraphs, lists, tables, images, links, forms, and more.
2. Next, XML can be use in various occasion, such as configuration files, data storage, web services (SOAP), and document markup. While JSON IS used for data interchange in web applications and APIs. On the other hand, HTML is used for creating web pages that are rendered by web browsers.

## 3.Why is JSON often used in data exchange between modern web applications?
1. JSON supports complex data structures, including nested objects and arrays, therefore it is often used to representing varies data types.
2. JSON is supported by most modern web application and is available in a wide range of programming languages.
3.JSON is not tied to any specific programming language or technology. So, it can be used in with a variety of back-end and front-end prgramming language.
## 4.Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. Create a new file inside `main.py` named `forms.py`. 
    - Create a class name `ProductForm` and use `ModelForm` as the parameter. Than, add some import in `views.py` and also create a function called `create_product`.
2. Change the `show_main` functions inside `views.py`
3. Created `create_product` function inside `urls.py` in `main` folder. Don't forget to add new path to urlpatterns. `path('create-product', create_product, name='create_product'),`.
4. Create a new html files name `create_product.html` inside `templates` subdirectory inside the `main` folder. Use POST method and also use `{% csrf_token %}` as a security. 
5. Modify `main.html` and add some code.
6. Returning data as XML.
    - Open `views.py` and add some imports.
    - Create a new function called `show_xml` which accepts requests as parameters.
    - Add a return statement to return the previously fetched data as XML.
    - ```def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    - Add path into urlpatterns in `urls.py` inside `main` directory.
7. Returning data as JSON.
    - Open `views.py` and add some imports.
    - Create a new function called `show_json` which accepts requests as parameters.
    - Add a return statement to return the previously fetched data as JSON.
    - ```def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    - Add path into urlpatterns in `urls.py` inside `main` directory
8.  Create functions called `show_xml_by_id` inside `views.py` in `main` directory. Don't forget to create URL routing for it.
- ``` def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")```
9. Create functions called `show_json_by_id` inside `views.py` in `main` directory. Don't forget to create URL routing for it.
- ``` def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json") ```

## Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
<img src="/asset/xml.jpg">
<img src="/asset/xml1.jpg">
<img src="/asset/main.jpg">
<img src="/asset/json.jpg">
<img src="/asset/json2.jpg">