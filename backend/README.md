# Student management backend

## Api Endpoints

- POST url: <https://steel-league-241504.appspot.com/api/v1/students>
- GET student list url: <https://steel-league-241504.appspot.com/api/v1/students>
- GET student detail url: <https://steel-league-241504.appspot.com/api/v1/students/455>
- UPDATE(PUT) student url: <https://steel-league-241504.appspot.com/api/v1/students/455>
- DELETE student url: <https://steel-league-241504.appspot.com/api/v1/students/455>
- payload for post: `{ student_id: string, roll: integer, name: string, student_class: integer,
date_of_birth: date, address: string, email_address: string, phone_number: string, 
}`
## Run
- Install google cloud sdk
- Follow the instruction on <https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env>
- Access the root folder.
- create a virtual environment
- run `pip install -r requirements.txt` to install dependency
- run `pip install -t lib -r requirements.txt`