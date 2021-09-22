# Mercado Livre API challenge
This repository was created to make a simple CRUD application as an example for Mercado Livre's challenge.
It will be used to demonstrate some concepts on the API construction process as well as on deployment and maintenance. 
Any suggested changes and improvements are welcome, so feel free to simply open up a PR :smile:

## Directory Structure
<pre>
├── README.md
├── requirements.txt
├── src
│├── local.db
│└── main.py
│├── app
│├── __init__.py
│├── actions.py
│├── context_manager.py
│├── models.py
│└── schemas.py
├── routers
│       ├── __init__.py
        └── items.py
└── test
    └── __init__.py
</pre>

## Tech Stack
To make it **faster** to test out our example and also easier to understand, I have developed this application 
using the [FastAPI framework](https://fastapi.tiangolo.com/), since it comes packed up with a bunch of functionalities to make the code simple, production-ready and fast. 

## Deployed application

The deployed application can be found [here](https://meli-api-challenge.herokuapp.com/docs). Over there you will find an OpenAPI documentation with all of the possible operations, which are:

- **GET**/Read items: get a list of all items in the table on the database
- **POST**/Create item: pass a `title` and a `description` to the Body JSON object to create an item
- **GET**/Read Item by Id: pass the id to read a specific item `title` and `description`
- **DELETE**/Delete Item by Id: delete a specific item by its ID number

## Local Development

To make sure you can run this application, make sure you have `python=>3.7` in your environment, as well as the `pip` package manager. 

### Preparing the environment
First, create a virtual environment and install all the required dependencies by running:
```bash
$ python3 -m venv .env
$ source .env/bin/activate
$ python3 -m pip install -r requirements.txt
```
>***NOTE***: If you're using windows the command to activate the environment is slightly different, so if that's your case, run: `.env\Scripts\activate` and follow along.

### Running the application
In order to run, you can use directly use the `main.py` file by running:

```bash
$ python3 main.py
```
And then your terminal will show that an application is running on 


## Further Improvements
- [ ] Dockerize application
- [ ] Deploy application
- [ ] Fill in README
- [ ] Hide sensitive variables
