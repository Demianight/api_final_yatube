#API YATUBE
API для проекта yatube который дает такой же функционал как сам yatube, за исключением подписок, они слегка урезаны

#УСТАНОВКА
Скачиваем/форкаем проект
Желательно! Устанавливаем вируальное окружение python -m venv venv, запускаем его
Устанавливаем все зависимости, pip install -r requirements.txt
#ПРИМЕРЫ ЗАПРОСОВ К API

/api/v1/posts/
Response:{

    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": 

[

        {}
    ]

}

/api/v1/posts/
Post data:{
  "text": "string",
  "image": "string",
  "group": 0
}
Response:{

    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0

}

api/v1/jwt/create/
Post data:{

    "username": "string",
    "password": "string"

}
Response:{

    "refresh": "string",
    "access": "string"

}
