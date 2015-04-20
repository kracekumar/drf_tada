# drf_tada
Django REST Framework + Todo

This repo contains Todo api using Django REST Framework. The idea behind
the repo is to demonstrate REST framwork doesn't couple Django ORM.

This is not simple TODO app. The app contains endpoints for listing user details,
TodoBucket, Task details etc ...

### Libraries
- Python 3 only
- Django 1.8
- REST Framework 3

### Endpoints

```
/users/<user_pk>/change_password/ -> Change User Password
/users/<user_pk/> -> Detail about user
/todo_bucket/ -> List all do bucket with pagination
/todo_bucket/<todo_bucket_pk>/ -> Details about Todo Bucket
/todo_bucket/<todo_bucket_pk>/tasks/ -> List of all tasks belonging to bucket
/todo_bucket/<todo_bucket_pk>/tasks/<task_pk>/ -> Specific task detail
/todo_bucket/<todo_bucket_pk>/tasks/<tasks_pk>/notes/<notes_pk> - > Specific note details.
```

### Terms

#### Todo Bucket
Todo bucket is container for task like `personal`, `coding`.

#### Task
Task is small actionable item like `pay bill`, `review pull request`.

#### Note
Note is small information on task like `paid via NetBanking`.

### Examples

#### List User Details
```json
http://localhost:8002/users/1/

{
    "id": 1,
    "email": "k@k.com",
    "username": "kracekumar",
    "first_name": "foo",
    "last_name": "foo"
}
```

#### Todo Bucket

```json
http://localhost:8002/todo_bucket/

{
    "meta": {
        "limit": 20,
        "offset": 0,
        "total": 10
    },
    "objects": [{
        "title": "coding",
        "description": "List of items I want to do in programming",
        "is_public": true,
        "created": "1428611510",
        "modified": "1428611510",
        "id": 1,
        "created_by": 1
    }, {
        "title": "Coding 1",
        "description": "List of items I want to do in programming",
        "is_public": true,
        "created": "1428611747",
        "modified": "1428954227",
        "id": 2,
        "created_by": 1
    }, {
        "title": "coding",
        "description": "List of items I want to do in programming",
        "is_public": true,
        "created": "1428611754",
        "modified": "1428611754",
        "id": 3,
        "created_by": 1
    }, {
        "title": "coding",
        "description": "List of items I want to do in programming",
        "is_public": true,
        "created": "1428740561",
        "modified": "1428740561",
        "id": 4,
        "created_by": 1
    }, {
        "title": "coding",
        "description": "List of items I want to do in programming",
        "is_public": true,
        "created": "1428740637",
        "modified": "1428740637",
        "id": 5,
        "created_by": 1
    }, {
        "title": "coding",
        "description": "List of items I want to do in programming",
        "is_public": true,
        "created": "1428740741",
        "modified": "1428740741",
        "id": 6,
        "created_by": 1
    }, {
        "title": "coding",
        "description": "List of items I want to do in programming",
        "is_public": true,
        "created": "1428740775",
        "modified": "1428740775",
        "id": 7,
        "created_by": 1
    }, {
        "title": "coding",
        "description": "List of items I want to do in programming",
        "is_public": false,
        "created": "1428740806",
        "modified": "1428740806",
        "id": 8,
        "created_by": 1
    }, {
        "title": "Ambitions",
        "description": "Amitious projects",
        "is_public": false,
        "created": "1428771606",
        "modified": "1428771606",
        "id": 9,
        "created_by": 1
    }, {
        "title": "World tour",
        "description": "places to visit",
        "is_public": false,
        "created": "1428771624",
        "modified": "1428771624",
        "id": 10,
        "created_by": 1
    }]
}
```

#### Todo Bucket details

```json
http://localhost:8002/todo_bucket/1/

{
    "title": "coding",
    "description": "List of items I want to do in programming",
    "is_public": true,
    "created": "1428611510",
    "modified": "1428611510",
    "id": 1,
    "created_by": 1
}
```

#### List of tasks in Todo Bucket

```
http://localhost:8002/todo_bucket/1/tasks/

{
    "meta": {
        "limit": 20,
        "offset": 0,
        "total": 3
    },
    "objects": [{
        "id": 7,
        "title": "Add Test",
        "created": "1429470876",
        "modified": "1429470876",
        "is_archived": false,
        "is_completed": false,
        "due_date": null,
        "reminder": null,
        "created_by": 1
    }, {
        "id": 6,
        "title": "Add README",
        "created": "1429470869",
        "modified": "1429470869",
        "is_archived": false,
        "is_completed": false,
        "due_date": null,
        "reminder": null,
        "created_by": 1
    }, {
        "id": 5,
        "title": "Complete Note View",
        "created": "1429445796",
        "modified": "1429464616",
        "is_archived": true,
        "is_completed": false,
        "due_date": null,
        "reminder": null,
        "created_by": 1
    }]
}
``
`

#### Task details

`
``
json
http: //localhost:8002/todo_bucket/2/tasks/5/

    {
        "id": 5,
        "title": "Complete Note View",
        "created": "1429445796",
        "modified": "1429464616",
        "is_archived": true,
        "is_completed": false,
        "due_date": null,
        "reminder": null,
        "notes": [{
            "id": 10,
            "description": "Write",
            "created": "1429459872",
            "modified": "1429459872",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/10/"
        }, {
            "id": 9,
            "description": "Foo",
            "created": "1429459768",
            "modified": "1429459768",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/9/"
        }, {
            "id": 8,
            "description": "Foo",
            "created": "1429459535",
            "modified": "1429459535",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/8/"
        }, {
            "id": 7,
            "description": "Foo",
            "created": "1429458788",
            "modified": "1429458788",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/7/"
        }, {
            "id": 6,
            "description": "Foo",
            "created": "1429458155",
            "modified": "1429458155",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/6/"
        }, {
            "id": 5,
            "description": "Foo",
            "created": "1429457890",
            "modified": "1429457890",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/5/"
        }, {
            "id": 4,
            "description": "Foo",
            "created": "1429457835",
            "modified": "1429457835",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/4/"
        }, {
            "id": 3,
            "description": "This is simple CRUD",
            "created": "1429446215",
            "modified": "1429446215",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/3/"
        }, {
            "id": 2,
            "description": "This is simple CRUD",
            "created": "1429446183",
            "modified": "1429446183",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/2/"
        }, {
            "id": 1,
            "description": "This is simple CRUD",
            "created": "1429446151",
            "modified": "1429446151",
            "resource_uri": "/todo_bucket/2/tasks/5/notes/1/"
        }],
        "created_by": 1
    }
```

#### Note Detail

```json
http://localhost:8002/todo_bucket/2/tasks/5/notes/1/

{
    "id": 1,
    "description": "This is simple CRUD",
    "created": "1429446151",
    "modified": "1429446151",
    "resource_uri": "/todo_bucket/2/tasks/5/notes/1/"
}
```


### Jargon

- Interactor - Business Orchestrator
- Service - Responsible to interact with Interactor and Repo. Mostly converting entity to dict for DB.
- BusinessResponse - Response originating from Interactor to view.
- Repo - Master of DB operations.

### Request

All the request requires `token` to access the details. You need to add
```
Authorization: Token <token>
Content-Type: application/json
```
in the request header.

### Improvements

- Come up helper function to reduce number of operations in update functions.
- Use `namedtuple` rather than class for `BusinessResponse`.

### How to run test

- `export DJANGO_SETTINGS_MODULE='drf_tada.settings'`
- `export PYTHONPATH='.'; py.test`
