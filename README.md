# Python-Flask-Web-App-with-Dockerize-Practice
## Why build this?
TO-DO list applications felt the most rite-of-passage way of learning a full stack application.
For other reasons, I mainly wanted to practice more of my python, docker, and web application skills. This also serves as my first practical experience with web applications and docker in general.
The idea is that I learn more how web applications work in general allowing me to adapt learnings from it to my future cybersecurity or cloud projects. 
This also served as a way for me to refresh my CRUD skills ever since my first one in my C# school project.

## Tech/Coding languages used
- Python
  - Jinja2 (from Flask)
- SQL (via Flask SQLAlchemy)
- Basic web application languages
  - HTML
  - CSS
    - SASS: Why? Tried a more compressible syntax for CSS which still ends up translated to a normal css file.
- Docker

## App structure and discussion
The application is mainly run with 3 python files:
- main.py: This is where I practiced the main setup of a Flask web application.
- routes.py: Normally, all routes present in main.py should be here when thinking of more clear, and concise code. The separation here is mainly for the purpose of me learning about public and private routes separate from the TO-DO application function. TLDR; got too lazy to delete it after trying out stuff.
- auth.py: This is part of the private route made in routes.py serving as authentication for the route.
