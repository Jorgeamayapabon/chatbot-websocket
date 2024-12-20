
# CHATBOT WEBSOCKET

This chatbot project uses Django, Django Rest Framework, and Channels to handle real-time communication over WebSockets. Redis acts as the in-memory messaging system, while PostgreSQL stores the data. Docker is used to facilitate deployment and management of the environment.


## Installation

Clone the project
```bash
  git clone https://gitlab.com/challenges2241051/chatbot-websocket.git
```

To run this project, you will need to add the following environment variables to your .env file

```bash
 DJNGO_SECRET_KEY=XXXXXXXXXXX
 POSTGRE_DB=XXXXXXXXX
 POSTGRE_USER=postgres
 POSTGRE_PASSWORD=XXXXXXXXXXX
 POSTGRE_HOST=localhost
 POSTGRE_PORT=5432
 REDIS_HOST=localhost
```

Run the following command to create the containers for the postgre, redis services and the django project
```bash
 docker compose up
```

Run migrations. First let's get the id of the container where django is
```bash
 docker ps
```

Copy the container id and run the following commands
```bash
 docker exec -it container-id python manage.py makemigrations
 docker exec -it container-id python manage.py migrate
```

Create a super admin to be able to create chat rooms. You will be asked for a username, email and password.
```bash
 docker exec -it container-id python manage.py createsuperuser
```

Log in with the credentials you created and create one or more rooms
```bash
 http://127.0.0.1:8000/admin
```

All set. Now it's time to enter the chat but first you have to go to the following site
```bash
 http://127.0.0.1:8000/register
```

