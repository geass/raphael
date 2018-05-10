# RAPHAEL - RESTAURANT LISTING APP

#### What is that ? 

Raphael is a simple Django backed React-ish Restaurant Listing App was designed and developed by Muhammet Arslan. On that project, there are 3 repositories to be required for Raphall App.
- Raphael, is a Django powered backed application. Providing the main APIs via Rest + Oauth.
- RLA, is a React-ish frontend application. Consuming APIs and serving the content to the end-user
- Platform, is a Docker-based project. Contains Localbox, Dockerfiles and Kubernet-ish (in future!) manifestos.

##### Prerequisities

- [Follow the Platform Repository Readme Steps](https://github.com/raphael-app/platform.git)

##### How to use ? 

Raphael backed application aims to providing custom rest APIs, authorized&authenticated with oAuth2, to its clients. For a simple flow, you need to obtain an access_token first, then you can just send requests to fetch datas.

##### Create an application

After you logging as a super-user, you need to browse "http://localhost:8000/o/applications/" then click on the link to create a new application and fill the form with the following data:

```
Name: just a name of your choice
Client Type: confidential
Authorization Grant Type: Resource owner password-based
```

##### Obtaining an Access-Token

Before getting the permission-required datas from Raphael, you need to obtain an acceess-token with your client credentials. And to obtain an Access-token, you need to send below request to raphael;

```
curl -X POST -d "username:password" http://localhost:8000/api-token-auth/
````

That will generate an output as below;

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNlZXJlbmUiLCJleHAiOjE1MjU4NDM2MjAsImVtYWlsIjoiaW5mb0BzZWVyZW5lLmNvbSJ9.7V-F5-yxJ5pCSw0Q2VF18H4gRSj2xbL9l3HMFhiRONI",
    "user": {
        "id": 1,
        "last_login": "2018-05-08T23:05:16.900024Z",
        "is_superuser": true,
        "username": "seerene",
        "first_name": "",
        "last_name": "",
        "email": "info@seerene.com",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2018-05-08T15:05:35.962134Z",
        "groups": [],
        "user_permissions": []
    }
}
```

And copy the access-token.

##### Fetching the DATAs!

Okay, now you are ready to use Raphaels custom APIs freely! with your access-token.

```
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNlZXJlbmUiLCJleHAiOjE1MjU4NDM2MjAsImVtYWlsIjoiaW5mb0BzZWVyZW5lLmNvbSJ9.7V-F5-yxJ5pCSw0Q2VF18H4gRSj2xbL9l3HMFhiRONI" http://localhost:8000/restaurants/
```

#### APIs

##### Login

`POST /api-token-auth/ {username, password}`

##### Refresh Token

`POST /refreshToken/ {token}`

##### Register

`POST /user/register/ {username, password, email, first_name, last_name}`

##### Restaurant List

`GET /restaurants/`

##### Restaurant Detail

`GET /restaurants/{id}`
`GET /restaurants/1`

##### Edit Restaurant

`PUT /restaurants/1 {id,slug,title,description,body,owner_id}`
