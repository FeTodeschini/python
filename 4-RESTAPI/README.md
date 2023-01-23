Commands for preparing the environment in case you want to code from scratch based on my code:

1-Create Virtual Environment:
python -m venv venv

2-Activate Virtual Environment:
. .\venv\Scripts\activate

3-Install Django:
pip install django

4- Install Django Rest Framework:
pip install djangorestframework

5-Create Django project:
django-admin startproject recipes


Testing the APIS:

1-Download the repository to your local folder

2-From the terminal (i.e.: from an IDE suc as Visual Studio Code or PyCharm), start the server by executing the command below:

python manage.py runserver

3-For querying the data using the API, type the URL below in your browser's address bar:

Querying all recipes:

http://127.0.0.1:8000/recipes/

Quering a specific recipe:

http://127.0.0.1:8000/recipes/<id>
Where:
    id is the numeric id of the recipe, such as:

    http://127.0.0.1:8000/recipes/2

4-Testing the method for adding a recipe:

Using Postman (or any other API testing tool), try the actions below. You can refer to the screenshots in this GitHub repository to see the selected options.

4.1-Select the method POST and type 127.0.0.1:8000/recipes
4.2-In the body pannel, select "raw" and then "JSON" in the dropdown next to it
4.3-Paste the JSON in the body input box. I.e.:

{
    "name": "recipe name",
    "ingredients": "recipe ingredients"
}

4.4-Click "Send"


5-Testing the method for updating a recipe:

Using Postman (or any other API testing tool), try the actions below. You can refer to the screenshots in this GitHub repository to see the selected options.

5.1-Select the method PUT and type 127.0.0.1:8000/recipes/id
Where:
    id is the id of the recipe to be updated (i.e: 3)

5.2-In the body pannel, select "raw" and then "JSON" in the dropdown next to it
5.3-Paste the JSON in the body input box. I.e.:

{
    "id": id of the recipe to be updated,
    "name": "new recipe name",
    "ingredients": "new recipe ingredients"
}

5.4-Click "Send"


6-Testing the method for deleting a recipe:

Using Postman (or any other API testing tool), try the actions below. You can refer to the screenshots in this GitHub repository to see the selected options.

5.1-Select the method DELETE and type 127.0.0.1:8000/recipes/id
Where:
    id is the id of the recipe to be deleted (i.e: 3)

5.2-Click "Send"




