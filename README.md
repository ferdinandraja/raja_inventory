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

# Assignment 4

# Explanation
## 1.What is UserCreationForm in Django? Explain its advantages and disadvantages.
UserCreationForm is a built-in form that eases user to create a user registration form for web application. With this form, user can create a registration form without needing to code it from scratch.
### ADVANTAGES:
1. Simple. UsercreationForm eliminates away all complexity in creating a form in django.It comes with pre-defined fields for common user attributes such as username, password, and email, making it easy to create a basic registration form quickly.
2. Integrated with Application System. It integrates with Django, such that when a user submits the form, a user account is created with a hashed password, and the user is automatically logged in.
3. Customizable. Even though it provides a default settings, user can still do some customization on it.

### DISADVANTAGES:
1. Styling. UserCreationForm has limited type of styling.
2. Basic User Attributes. It is not sufficient for more complex user profiles that require additional information. In such cases, you'll need to create custom forms and views.

## 2.What is the difference between authentication and authorization in Django application? Why are both important?
Authentication is the process of verifying the identity of a user, confirming that they are who they claim to be.Authorization, on the other hand, is the process of determining whether a user has permission to perform a specific action or access a particular resource within your application.

## 3.What are cookies in website? How does Django use cookies to manage user session data?
Cookies are small pieces of data that a web server sends to a user's web browser and are stored on the user's device. They are used to store information about the user's interactions with a website. Django uses a cookie containing a special session id to identify each browser and its associated session with the site. The actual session data is stored in the site database by default.
## 4.Are cookies secure to use? Is there potential risk to be aware of?
Cookies are a fundamental part of web development and can be secure when used correctly, but there are potential risks and security. It is possible to steal data from cookies if the cookies are not secured.

## 5.Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. Open `views.py` inside `main.py` folder and create a function called `register` that accepts `requests` as parameter. Don't forget to add some imports before.
    ```
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ```
2. Create a new file called `register.html` inside `main/templates` folder, don't forget to add the routing.
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
3. Create a logout function inside `views.py` inside `main` directory. Dont forget to also add the routing.
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
4. Gives a restriction to access the main page by:
     - import this:
     `from django.contrib.auth.decorators import login_required`
     -and add this code before `show_main`:
     `@login_required(login_url='/login')`

5. Import this into `views.py` in `main` directory.
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
6. Modify the `login_user` function
7. Inside `show_main` function, add new variables inside context with `'last_login': request.COOKIES['last_login']`
8. Modify the `logout_user` function with `response.delete_cookie('last_login')` to delete cookies after user logout.
9. Add the llast login session in the `main.html`
10. Import user into `models.py`
11. Modify Item class into:
```
class Product(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
12. Modify the `show_main` and `create_products` function such that it connects user product with user id.

# Assignment 5

# Explanation
## 1.Explain the purpose of some CSS element selector and when to use it.
1. Type Selector
The purpose of type selector is to target object that belongst to that element. People can use type selector to apply something into all subject of that particular element.
Example : `td`selector only works for all `td` elements
2. Class Selector
The purpose of class selector is to target object that have the same class attribute. Peoplpe can use class selector to apply a modification to object that belong to the same class. Example `.city` selector only target `.city` class
3. ID selector
Target element that has the same single ID. Example `#myHeader` selector only targets object that have `#myHeader` id.
## 2.Explain some of the HTML5 tags that you know.
`<header>` -> Represents container that contain introductory content. Commonly used to define the top section of a page.
`<nav>` -> Define something that represents a link
`<footer>` -> Defines a footer of a page
`<progress>` -> Creates a progress bar for some process.
## 3. What are the differences between margin and padding?
Margin is the space outside the element. So it states the radius of the element into another element outside it. On the other hand, padding is the space between the content and the border of an element. So, it states the distance between the border and the content itself. 
## 4.What are the differences between the CSS framework Tailwind and Bootstrap? When should we use Bootstrap rather than Tailwind, and vice versa?
Both Tailwind and Bootstraps are a CSS framework that both provides freedom for users to beautify their website. The difference of both is most of the times, Tailwind is more flexible than Bootstrap. For example, it is easier in Tailwind to create a gradient background than Bootstrap. Even though Bootstrap is easier to understand, Tailwind offer a greater user experience as it offer a lot more customization than Bootstrap. So if you want to create a more creatively demanding web, it is more recommended to use Tailwind than Bootstrap. On the other hand you can use Bootstrap to create a quicker start with pre-designed components and a more opinionated design system.
# Step by step:
1. add this code inside `<head>` in `base.hmtl`:
        ```<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">```
2. Customize `main.html` to become like this, this code adds a navbar and beautify the main page:
```
{% extends 'base.html' %}

{% block content %}
<style>
    .custom-btn {
    background-color: #04364A; /* Change to your desired color */
    color: #FFFFFF; /* Text color */
    border: none; /* Remove border if needed */
  }
  .custom2-btn{
    background-color: #DAFFFB; /* Change to your desired color */
    color: black; /* Text color */
    border: none; /* Remove border if needed */
  }
</style>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <h3>Hi {{name}}!</h3>
      <div class="collapse navbar-collapse" id="navbarSupportedContent" style="text-align: right;">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Last login session: {{last_login}}</a>
              </li>
              <li><a class="nav-link disabled" aria-disabled="true">Class:{{class}}</a>
            </li>
        </ul>
        </div>
      <a class="navbar-brand" href="{% url 'main:logout' %}">Logout</a>
    </button>
    </div>
</nav>
    <h1 style="text-align: left;">Raja Inventory</h1>
    <br>
    <p style="text-align: center;">You have saved {{counter}} items in this application</p>
    <table class="table table-striped table-hover">
        <thead class="thead-dark">
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Amount</th>
              <th scope="col">Price</th>
              <th scope="col">Description</th>
              <th scope="col">Date Added</th>
              <th></th>
            </tr>
        </thead>
    
        {% comment %} Below is how to show the product data {% endcomment %}
    
        {% for product in products %}
        <tbody>
            <tr>
                <td>{{product.name}}</td>
                <td><form method="post">
                    {% csrf_token %}
                    <button type="submit" class="btn custom-btn btn-sm" name="decrement" value="{{product.id}}">
                        -
                    </button>{{product.amount}}
                        <button type="submit" class="btn custom-btn btn-sm" name="increment" value="{{product.id}}">
                            +
                        </button>
                    </div>
                        </form>
                </td>
                <td>{{product.price}}</td>
                <td>{{product.description}}</td>
                <td>{{product.date_added}}</td>
                <td>
                    <form method="post">
                        {% csrf_token %}
                        <button type="submit" class="btn custom-btn btn-sm" name="delete" value="{{product.id}}">
                            Delete Item
                        </button>
                    </form>
                    <a href="{% url 'main:edit_product' product.pk %}">
                        <button class="btn custom-btn btn-sm">Edit</button>
                    </a>
                </td>
            </tr>
        </tbody>
        {% endfor %}
    </table>
    
    <br />
    
    <div class="container" style="text-align: center;">
    <a href="{% url 'main:create_product' %}">
        <button class="btn btn-primary" type="button">
            Add New Product
        </button>
    </a>
    <a href="{% url 'main:logout' %}">
        <button class="btn custom2-btn">
            Logout
        </button>
    </a>
</div>
{% endblock content %}
```
3. Customize `login.html` to add a navbar, customize the button, use cards:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}
<style>
    bac
</style>
<nav class="navbar navbar-expand-lg bg-body-tertiary" style="background: #AAA;">
    <div class="container-fluid">
    <h1>Login</h1>
    </div>
</nav>
<div class="col d-flex justify-content-center">
<div class="card p-3 text-center" style="width: fit-content,">
    <div class="card-header" style="background-color: #3085C3;">
        Login
</div>
    <div class="card-body" style="align-content: center;">
    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn btn-primary btn-block mb-4" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>
</div>
</div>

</div>

    {% if messages %}
            {% for message in messages %}
                <p align ="center">{{ message }}</p>
            {% endfor %}
    {% endif %}
    <div class="text-center">
        <p>Don't have an account yet?  <a href="{% url 'main:register' %}">Register Now!</a></p>
    </div>

</div>
{% endblock content %}
```
4. Customize `register.html` such that it uses a navbar,cards, and customize the button :
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<nav class="navbar navbar-expand-lg bg-body-tertiary" style="background: #AAA;">
    <div class="container-fluid">
    <h1>Register</h1>
    </div>
    <a class="navbar-brand" href="{% url 'main:show_main'%}">Main Menu</a>
</nav>
<div class="col d-flex justify-content-center">
    <div class="card p-3 text-center" style="width: fit-content,">
        <div class="card-header" style="background-color: #3085C3;">
            <p align="left">Register</p>
    </div>
        <div class="card-body" style="align-content: center;">
        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input class="btn btn-primary btn-sm btn-block" type="submit" value="Register"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
5. Customize `create_product.html` to uses a navbar, cards, and customize the button :
```
{% extends 'base.html' %} 

{% block content %}
<nav class="navbar navbar-expand-lg bg-body-tertiary" style="background: #AAA;">
    <div class="container-fluid">
    <h1>Add New Product</h1>
    </div>
    <a class="navbar-brand" href="{% url 'main:logout' %}">Logout</a>
    <a class="navbar-brand" href="{% url 'main:show_main'%}">Main Menu</a>
</nav>
<div class="col d-flex justify-content-center">
    <div class="card p-3 text-center" style="width: fit-content,">
        <div class="card-header" style="background-color: #3085C3;">
            <p align="left">Add Product</p>
    </div>
        <div class="card-body" style="align-content: center;">
<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product" class="btn btn-primary "/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
6. Customize the `edit_product.html` to uses navbar, cards, and customize the button:
```
{% extends 'base.html' %}

{% load static %}

{% block content %}
<nav class="navbar navbar-expand-lg bg-body-tertiary" style="background: #AAA;">
    <div class="container-fluid">
    <h1>Edit Product</h1>
    </div>
    <a class="navbar-brand" href="{% url 'main:logout' %}">Logout</a>
    <a class="navbar-brand" href="{% url 'main:show_main'%}">Main Menu</a>
</nav>
<div class="col d-flex justify-content-center">
    <div class="card p-3 text-center" style="width: fit-content">
        <div class="card-header" style="background-color: #3085C3;">
            <p align="left">Edit Product</p>
    </div>
        <div class="card-body" style="align-content: center;">

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product" class="btn btn-primary btn-sm btn-block"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
7. Customize the `name` in context inside `show_main` in `views.py` to become like this:
```
context = {
        'name': request.user.username
```
Such that the name will changes depend on the user logged in
8. Git add, commit, and push to the github.

# Assignment 6

# Explanation
## 1. Explain the difference between asynchronous programming and synchronous programming.
Asynchronous programming is designed to handle tasks that may take time to complete without blocking the program's execution. In this kind of program, when a task is executed, instead of waiting for it to be finish, the program continues to execute another tasks. On the other hand, synchronous programming follows a straight execution model. Which means that for this kind of program, when a task is executed, he program will wait for it to complete before moving on to the next task, unlike asynchronous program.
## 2. In the implementation of JavaScript and AJAX, there is an implemented paradigm called the event-driven programming paradigm. Explain what this paradigm means and give one example of its implementation in this assignment.
Event driven programming pardigm is a programming model that uses interactions from user or event to determined the flow of the program. In this kind of porgram, the program responds to user interaction or events, which will be treanslated and triggered the program to do something. In this assignment, the example is
```
document.getElementById("button_add").onclick = addProduct
```
Which means when the user click the `button_add`, the event driven approach is applied.

## 3. Explain the implementation of asynchronous programming in AJAX
Asynchronous programming in AJAX allows user to retrieve data from a server and update parts of a web page without needing to refresh the entire page. This possible because AJAX allow web to make HTTP request without blocking the main execution of the browser

## 4.In this semester, the implementation of AJAX is done using the Fetch API rather than the jQuery library. Compare the two technologies and write down your opinion which technology is better to use
To begin with, Fetch API is a part of modern Javascript and also lighter in size than jQuery. On the other hand, jQuery provides a simplified and consistent API for making AJAX requests and also needed to maintain older websites that still use it.
In summary, for most modern web development projects, the Fetch API is the better choice due to its native support in JavaScript, Promise-based approach, and better performance. However, for legacy projects and situations where cross-browser compatibility and ease of use are critical, jQuery AJAX remains a viable option. The choice should be made based on the specific requirements of your project and the development team's expertise.

## 5. Explain how you implemented the checklist above step-by-step (not just following the tutorial).
1. Create a new function on`views.py` called `get_product_json`, `incrementItem`, `decrementItem`, and `delete_product`.
Don't forget to do the routing for all functions on `urls.py`
2. Create a new function on`views.py` called `add_product_ajax` that accepts request as parameter. Also add a decorator above the function. So it becomes:
```
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
Don't forget to do the routing for it.
3. Delete the previous table code inside `main.html` and add a script at the last part of the file.
```
    <script>
        async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }
        async function refreshProducts() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getProducts()
        let htmlString = `<tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
            <th></th>
        </tr>`
        products.forEach((item) => {
            htmlString += `\n
            <body>
            <tr>
            <td>${item.fields.name}</td>
            <td>
                <a href="decrement/${item.pk}">
                        <button class="btn custom-btn btn-sm">-</button>
                    </a>
                ${item.fields.amount}
                <a href="increment/${item.pk}">
                        <button class="btn custom-btn btn-sm">+</button>
                    </a>
            </td>
            <td>${item.fields.price}</td>
            <td>${item.fields.description}</td>
            <td>
                ${item.fields.date_added}
            </td>
            <td>
                <a href="delete/${item.pk}">
                        <button class="btn custom-btn btn-sm">Delete</button>
                    </a>
                    <a href="edit-product/${item.pk}">
                        <button class="btn custom-btn btn-sm">Edit</button>
                    </a>
                </td>
            </tr>
        </tbody>` 
        })
        
        document.getElementById("product_table").innerHTML = htmlString
    }

    refreshProducts()

    function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }

    document.getElementById("button_add").onclick = addProduct
    </script>
```
4. Add a modal that is mean to create the table:
```
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form id="form" onsubmit="return false;">
                        {% csrf_token %}
                        <div class="mb-3">
                            <label for="name" class="col-form-label">Name</label>
                            <input type="text" class="form-control" id="name" name="name"></input>
                        </div>
                        <div class="mb-3">
                            <label for="amount" class="col-form-label">Amount</label>
                            <input type="number" class="form-control" id="amount" name="amount"></input>
                        </div>
                        <div class="mb-3">
                            <label for="price" class="col-form-label">Price</label>
                            <input type="number" class="form-control" id="price" name="price"></input>
                        </div>
                        <div class="mb-3">
                            <label for="description" class="col-form-label">Description</label>
                            <textarea class="form-control" id="description" name="description"></textarea>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                </div>
            </div>
        </div>
    </div>
```
5. Inside the `cards`, add a button for AJAX add product:
```
 <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
```
6. Git add, commit, and push