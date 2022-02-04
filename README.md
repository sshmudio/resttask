### Start ###

1. Clone this repo
2. cd code && docker-compose up


### api edpoints ###

# Отправте post запрос для добавления пользователей

curl -X POST -H "Content-Type: application/json" -d '{"username": "exampleuser1", "email": "exampleuser@gmail.com", "password": "superencryptpassword111"}' http://0.0.0.0:8000/api/v1/user/

# Запрос на получение списка пользователей

curl -X GET http://0.0.0.0:8000/api/v1/user-list/

# Запрос на получение пользователя с конкретным pk, api/v1/user/{pk}.

curl -X GET http://0.0.0.0:8000/api/v1/user/1

# PUT

curl -X PUT -H "Content-Type: application/json" -d '{"username": "newusername2", "password": "superpasswords", "email": "linuxize@example.com"}' http://0.0.0.0:8000/api/v1/user/1


# DELETE удаление

curl -X DELETE http://0.0.0.0:8000/api/v1/user/1

Можем проверить удалилась ли запись curl -X GET http://0.0.0.0:8000/api/v1/user/1
Ответ:
    {"detail":"Not found."}