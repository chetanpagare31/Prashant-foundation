# Prashant Foundation

This project is a Django-based REST API for authentication using JWT, with MySQL as the database. The service supports user sign-up, sign-in, token refreshing, and token revocation.

## Prerequisites

- Docker
- Docker Compose

## Running the Project with Docker

To run this project using Docker, follow these steps:

1. **Clone the repository**

   git clone https://github.com/chetanpagare31/Prashant-foundation.git
   cd Prashant-foundation

2. **Build and start the Docker containers**

    docker-compose up --build

    This command will:
        Build the Docker images.
        Start the MySQL and Django containers.
        Apply migrations.


3. **Access the service**

    The API will be available at http://localhost:8000.

## Curl Commands to Test the Endpoints
    Run below commands in Git bash on path of respective working directory 

## For SignUp: Sign up (creation of user) using email and password

$ curl --location 'http://localhost:8000/api/signup/' --header 'Content-Type: application/json' --data-raw '{
    "username": "Raj",
    "email": "Raj@gmail.com",
    "password": "Raj@123"
}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   124  100    42  100    82     50     98 --:--:-- --:--:-- --:--:--   149{"username":"Raj","email":"raj@gmail.com"}


## For SignIn: a.Authentication of user credentials 
                b. A token is returned as response preferably JWT

$ curl --location 'http://localhost:8000/api/signin/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "Raj",
    "email": "Raj@gmail.com",
    "password": "Raj@123"
}
'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   623  100   540  100    83    662    101 --:--:-- --:--:-- --:--:--   764{"refresh":"your_refresh_token","access":"your_access_token","user":{"id":8,"username":"Raj","email":"raj@gmail.com"}}



## Get Users: Authorization of token


$ curl --location 'http://localhost:8000/api/users/' \
--header 'Authorization: Bearer your_access_token'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   429  100   429    0     0   1889      0 --:--:-- --:--:-- --:--:--  1898[{"id":1,"username":"chetan","email":"chetan@gmail.com"},{"id":2,"username":"vickyp","email":"vicky@gmail.com"},{"id":3,"username":"amarp","email":"amar@gmail.com"},{"id":4,"username":"Rakshit","email":"rakshit@gmail.com"},{"id":5,"username":"amit","email":"amit@gmail.com"},{"id":6,"username":"mit","email":"mit@gmail.com"},{"id":7,"username":"Sumit","email":"sumit@gmail.com"},{"id":8,"username":"Raj","email":"raj@gmail.com"}]





## For Revocation of token: 

curl --location 'http://localhost:8000/api/revoke/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer your_access_token' \
--data '{
    "refresh": "your_refresh_token"
}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   285  100    35  100   250    125    896 --:--:-- --:--:-- --:--:--  1025{"detail":"Refresh token revoked."}



## Mechanism to refresh a token

$ curl --location 'localhost:8000/api/refresh/' \
--header 'Content-Type: application/json' \
--data '{
    "refresh": "your_refresh_token"
}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   491  100   241  100   250   1072   1112 --:--:-- --:--:-- --:--:--  2191{"access":"your_access_token"}



## Notes

    Replace your_access_token and your_refresh_token with actual tokens obtained from the Sign In endpoint.

## Environment Variables

    When running the project in Docker, the following environment variables are set automatically in docker-compose.yml:

    DATABASE_NAME: The name of the MySQL database (default: social_nwk_db)
    DATABASE_USER: The MySQL user (default: root)
    DATABASE_PASSWORD: The MySQL user password (default: root)
    DATABASE_HOST: The MySQL host (default: db)
    DATABASE_PORT: The MySQL port (default: 3306)
    When running the project locally, these can be set in your environment or will default to the values specified above.

## Project Structure

    Prashant-foundation/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── manage.py
    ├── .dockerignore
    ├── socialNetworkingProject/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── accounts/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── requirements.txt
    └── README.md

## Troubleshooting

    If you encounter any issues, please ensure that:

    Docker and Docker Compose are installed correctly.
    The ports 8000 and 3306 are available and not being used by other services.
    The environment variables are set correctly if running locally.
    Feel free to open an issue on the GitHub repository if you need further assistance. 


### Summary

    This setup ensures that everything is done with a single Docker command (`docker-compose up --build`), and the API is ready to be tested with the provided curl commands. The `Dockerfile` and `docker-compose.yml` handle the setup, including migrations. Copy these configurations and the updated `README.md` file into your project, commit, and push the changes to your GitHub repository. If you have any further questions or need additional adjustments, let me know!
