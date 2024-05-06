# Event-management Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

<a id="introduction"></a>
## Introduction
Event Management is an **ultra-simple** **Django**-based **REST API** pet project for managing events, with some noticeable features:

- Custom User model for registration with email and password
- CRUD operations and search for event models
- JWT authentication and authorization
- Event registration
- Simple Unit tests
- Containerized in Docker

<a id="installation"></a>
## Installation with Docker
1. Clone This Project ```git clone https://github.com/serhiikravets/event-management.git```
2. cd to project directory ```cd event-management```
3. In a project directory - Run the following command to build your Docker images: ```docker-compose build```
4. Once the build process is complete, you can start your Docker containers with the following command: ```docker-compose up```
5. Then open your django container exec via docker desktop (find container, click on exec button) or by running this command ```docker exec -it container_id python manage.py migrate``` (you can get container_id with ```docker ps```)
6. Then also createsuperuser in the same exec ```docker exec -it container_id python manage.py createsuperuser```
7. Open your web browser and visit http://localhost:8000/, nothing special there :) but you can play with the app (crud and stuff) in postman or run tests by using this command: ```docker exec -it container_id python manage.py test```

<a id="usage"></a>
## Usage Guide with Postman
This guide will walk you through the process of creating and testing events using Postman.
### Prerequisites
- Postman installed on your machine
- Your Django server is running
### Steps
1. **Register a new user**
    - Open Postman and create a new request.
    - Set the request method to `POST` and the URL to `http://localhost:8000/register/`.
    - In the `Headers` tab, add a new key `Content-Type` with the value `application/json`.
    - In the `Body` tab, select `raw` and `JSON`, then enter your user data in the following format:
        ```json
        {
            "email": "your-email",
            "password": "your-password"
        }
        ```
    - Send the request. The response should include the details of the user you just registered.

2. **Get the JWT Token**
    - Create a new request.
    - Set the request method to `POST` and the URL to `http://localhost:8000/api/token/`.
    - In the `Headers` tab, add a new key `Content-Type` with the value `application/json`.
    - In the `Body` tab, select `raw` and `JSON`, then enter your login credentials in the following format:
        ```json
        {
            "email": "your-email",
            "password": "your-password"
        }
        ```
    - Send the request. The response should include your JWT token.

3. **Perform CRUD Operations on Events**
    - **Create an Event**
        - Create a new request.
        - Set the request method to `POST` and the URL to `http://localhost:8000/events/`.
        - In the `Headers` tab, add two new keys:
            - `Content-Type` with the value `application/json`.
            - `Authorization` with the value `Bearer your-token`.
        - In the `Body` tab, select `raw` and `JSON`, then enter your event data in the following format:
            ```json
            {
                "title": "Event Title",
                "description": "Event Description",
                "date": "YYYY-MM-DD",
                "location": "Event Location"
            }
            ```
        - Send the request. The response should include the details of the event you just created.

    - **Read an Event**
        - Create a new request.
        - Set the request method to `GET` and the URL to `http://localhost:8000/events/event-id/`.
        - In the `Headers` tab, add a new key `Authorization` with the value `Bearer your-jwt-token`.
        - Send the request. The response should include the details of the event.

    - **Update an Event**
        - Create a new request.
        - Set the request method to `PUT` and the URL to `http://localhost:8000/events/event-id/`.
        - In the `Headers` tab, add two new keys:
            - `Content-Type` with the value `application/json`.
            - `Authorization` with the value `Bearer your-token`.
        - In the `Body` tab, select `raw` and `JSON`, then enter your updated event data.
        - Send the request. The response should include the details of the updated event.

    - **Delete an Event**
        - Create a new request.
        - Set the request method to `DELETE` and the URL to `http://localhost:8000/events/event-id/`.
        - In the `Headers` tab, add a new key `Authorization` with the value `Bearer your-jwt-token`.
        - Send the request. The response should confirm the deletion of the event.

4. **Search for an Event**
    - Create a new request.
    - Set the request method to `GET` and the URL to `http://localhost:8000/events?search=your-search-query`.
    - In the `Headers` tab, add a new key `Authorization` with the value `Bearer your-jwt-token`.
    - Send the request. The response should include the events that match your search query.

Remember to replace `your-email`, `your-password`, `your-jwt-token`, `Event Location`, `event-id`, and `your-search-query` with your actual data.
