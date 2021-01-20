# Coffee Shop Full Stack

## Introduction

This project is a Coffe Shop app, with the ability to view, add, edit, and delete the drinks.

There are two types of users, barista and manager. Baristas only have view access, while managers can do it all!

This is the fourth project of my Full Stack Web Developer microdegree course through Udacity. I really enjoyed working on this app and learned a ton in this section about security and access management .

This follows the [PEP8 style guides](https://www.python.org/dev/peps/pep-0008/). (At least to the best of my ability)

<br>

## Getting Started

### Pre-requisites

This app uses Python3, pip, Ionic, and Node. So you should already have these installed on your machine. If not, I would recommend going and doing that now.

### Backend

1) Before starting it you may want to start up a virtualenv using the following commands in the backend folder: 
```
python -m virtualenv env
source env/bin/activate
```
>**Note** Or if your using Windows you will need to replace the second line with:
```
source env/Scripts/activate
```
2) Now to get the backend up and running, first `cd` into the backend folder and run `pip install -r requirements.txt`. This should download all necessary packages in order to run it.

3) To actually start up the application run the following commands:
```
cd src 
export FLASK_APP=api.py
flask run -- reload
```
>**Note** If you are using Windows and these don't work replace `export` with `set`

This will tell Flask where to look for the app and set it into development mode.

The application runs on `http://127.0.0.1:5000/` by default and is just the server for the frontend, so you won't see anything on this port in your browser.

### Frontend

The frontend is pretty simple. Open a new terminal and cd into the `frontend` folder and run the following 

```
npm i 
ionic serve
```

This will start up the app on [localhost:8100](localhost:8100) by default.





## API Reference

### Getting Started

- Base URL: This app is currently only able to be run locally. The backend runs on `http://127.0.0.1:5000/` by default.
- Authentication: This app is already all set up to use Auth0 on my personal account!

### Error Handling

All of the errors you will encounter in this app have been formatted as JSON objects in the following format: 
```json
{
  "success": false,
  "error": 400,
  "message": "Bad Request"
}
```

The following are all of the potential errors you may run into: 

| Code | Message |
| ---- | ------- |
| 404 | Not Found |
| 422 | Not Proccessable |
| 401 | authorization_header_missing |
| 401 | invalid_claims |
| 401 | invalid_header |
| 401 | token_expired |
| 400 | invalid_claims |
| 403 | unauthorized |


## Endpoints

### GET /drinks

- General
  - Returns an object containing all of the drinks in their short form
  - URL: `http://127.0.0.1:5000/drinks`

```json
{
    "drinks": [
      {
        "id": 1,
        "recipe":[
          {
            "color": "gold",
            "parts": 2
          }
        ],
        "title": "Coffee"
      }
    ],
    "success": true
}
```

### GET /drinks-detail

- General
  - Returns an object containing all of the drinks in their long form
  - URL: `http://127.0.0.1:5000/drink-details`

```json
{
    "drinks": [
      {
        "id": 1,
        "recipe":[
          {
            "color": "gold",
            "name": "caramel",
            "parts": 2
          }
        ],
        "title": "Coffee"
      }
    ],
    "success": true
}
```

### POST /drinks

- General
  - Creates a new drink with the given values.
  - Receives data to insert into record in the following format:
  ```json5
    {
      "title": "Coffee",
      "recipe": [
        {
          "color": "gold",
          "name": "caramel",
          "parts": 2
        }
      ]
    }
  ```
  - Returns a success response with the new drink.
  - URL: `http://127.0.0.1:5000/drinks`

```json
{
  "drinks": [{
    "id": 1,
    "recipe": [
      {
        "color": "gold",
        "name": "caramel",
        "parts": 2
      }
    ],
    "title": "Coffee"
  }],
  "success": true
}
```

### PATCH /drinks/<id>

- General
  - Edits a drink with the given id.
  - Receives data to update the record in the following format:
  ```json5
    {
      "title": "Coffee",
      "recipe": [
        {
          "color": "gold",
          "name": "caramel",
          "parts": 2
        }
      ]
    }
  ```
  - Returns a success response with the edited drink.
  - URL: `http://127.0.0.1:5000/drinks/<id>`

```json
{
  "drinks": [{
    "id": 1,
    "recipe": [
      {
        "color": "gold",
        "name": "caramel",
        "parts": 2
      }
    ],
    "title": "Coffee"
  }],
  "success": true
}
```

### PATCH /drinks/<id>

- General
  - Edits a drink with the given id.
  - Returns a success response deleted drinks id.
  - URL: `http://127.0.0.1:5000/drinks/<id>`

```json
{
  "delete": 1,
  "success": true
}
```
