# Mercado Livre API challenge
This repository was created to make a simple CRUD application as an example for Mercado Livre's challenge.
It will be used to demonstrate some concepts on the API construction process as well as on deployment and maintenance. 
Any suggested changes and improvements are welcome, so feel free to simply open up a PR :smile:

## Directory Structure

All of the domain-specific code resides on `src/app/domain`, such as the operations, schemas and models. The `src/app/infrastructure` directory contains the database context manager file. All of the routes definitions, for each API, will take place on `src/app/routers` and the main application can be fired by calling the "orchestrator" `main.py` file on the root directory. The whole structure looks like this:

<pre>
├── Procfile
├── README.md
├── main.py
├── requirements.txt
├── src
│   ├── __init__.py
│   └── app
│       ├── __init__.py
│       ├── domain
│       │   ├── actions.py
│       │   ├── models.py
│       │   └── schemas.py
│       ├── infrastructure
│       │   └── context_manager.py
│       └── routers
│           ├── __init__.py
│           └── items.py
└── test
    ├── __init__.py
    └── src
        ├── __init__.py
        └── app
            ├── __init__.py
            └── domain
                └── test_actions.py
</pre>

## Tech Stack
To make it **faster** to test out our example and also easier to understand, I have developed this application 
using Python with the [FastAPI framework](https://fastapi.tiangolo.com/), since it comes packed up with a bunch of functionalities to make the code simple, production-ready and fast. 

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
And then, your terminal will show that an application is running on [localhost:8000/](localhost:8000/). Navigate through the operations on the `/docs` page and you can get started. :rocket: 


## Further Improvements
- [ ] Deploy to a real-world database, such as Postrgres, MySQL, etc.
- [ ] Dockerize application
- [ ] Improve CRUD operations
- [ ] Make an authorization step to use the API with JWT and OAuth2
