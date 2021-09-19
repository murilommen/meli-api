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
using the [FastAPI framework](https://fastapi.tiangolo.com/) since it comes packed up with a bunch of functionalities to make the code simple, production-ready and fast.

## Basic Usage

## Further Improvements
- [] Unit and integration testing 
- [] 