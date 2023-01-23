This is a set of APIS for CRUD operations in a NoSQL database (unstructured data) hosted on AWS

For you to test it, you need to have an account on AWS and create a table called 'veganrecipes' on DynamoDB (the AWS NoSQL database). This is the table that the API accesses. You also need to download AWS CLI (command line interface) from AWS site, install it in your machine and then configure it with the command below:

aws configure

The command will prompt for information related to your access key, besides othr info. For creating an access key in AWS management's console, please refer to the link below:

https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/


The main libraries used in this program were:

- Django (pip install django)
- Django REST framework (pip install djangorestframework)
- Boto3, the library for acessing AWS DynamoDB

Finally, for running the API and then testing it, you need to:

1-Bring Django server up by running the below command from your terminal's ID (i.e.: Visual Studio Code or PyCharm)

python manage.py runserver

2-Test the API either in your browser or using a tool like Postman. The API is hosted onm the address http://127.0.0.1:8000/

2.1-For testing the GET method for listing all vegan recipes, simply type http://127.0.0.1:8000/ in your browser if your Django server is up, or type it on Postman and call the GET method

2.2-For checking the recipe of a specif item, type /recipename after http://127.0.0.1:8000/, where:

recipename is the name of the recipe. Example:

http://127.0.0.1:8000/Babaganush

2.3-The DELETE method is not working. I will update GitHub once I figure out what is going on