# AirGliders 
### Airbus Aerothon 3.0

## Problem Statement

To create an innovative solution or application that integrates the end to end user experience and application support into one single place, which is accessible as an onscreen floating widget on top of any application/webpage, with one single click and looks simple + user friendly, that connects the users with the IT product teams.

## Solution

- We decided to create a Web Application. We used very light and efficient stacks to have a fast and smooth experience. We have used various technologies and frameworks like HTML, CSS, JS, Flask for frontend and Django for backend. Moreover we used Machine Learning for sentiment analysis and voice search and OpenAI for chatbot. An easily customizable and adaptable static page for the announcements is made by using JS. For better Bug reporting and Feedback assistance we connected the functionality with the database. Data collected is secured and sorted in our database.
- Stacks we used: Flask, HTML, CSS, Django, JavaScript, Machine Learning, sqlite3, OpenAI.

## Methodologies

We developed a WebApp by using Flask, HTML, CSS, Django, JavaScript, Machine Learning, AI, sqlite3. Flask, HTML, CSS, Django, JavaScript and sqlite3 were used to build frontend and backend and few functionalities of that WebApp. Machine Learning was used for Application Navigation in voice search , AI was used for Chat Bot. Sqlite3 was used to collect necessary information from Bug Report and Application Improvement functionality. 

Moreover, we added extra functionality in Application Improvement by adding Sentiment analysis using Machine Learning.

## Demo Video

Note: Just Click on the image below and you will be redirected to YouTube.

[![AirGliders](https://img.youtube.com/vi/C_mwLWJ5M4A/0.jpg)](https://www.youtube.com/watch?v=C_mwLWJ5M4A)

## How to run this Repo

First of all, you need a beta access of OpenAI GPT 3. If you have then steps to run are:

```
pip install -r requirements.txt
cd airbusback
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

And now open http://127.0.0.1:8000/ in a browser(Preferably Google Chrome).

To see Admin Pages open http://127.0.0.1:8000/admin/ and use login credentials which were created when `python manage.py createsuperuser` was used.

> Main Page
![Main Page](./airbusback/../screenshots/Screenshot%202021-05-22%20103346.png)

> FeedBack Form
![FeedBack Form](./screenshots/Screenshot%202021-05-21.jpeg)

> Announcements
![Announcements](./screenshots/Screenshot%202021-05-22%20103411.png)

> Report Bug
![Report Bug](./screenshots/Screenshot%202021-05-22%20103311.png)

> Search
![Search](./screenshots/Screenshot%202021-05-22%20103434.png)

> Admin Page
![Admin Page](./screenshots/Screenshot%202021-05-22%20110727.png)

## Collaborators

[Tushar Goel](https://github.com/Tushar-ml), [Lokesh Koliparthi](https://github.com/Lokesh2703), [Tanmay Garg](https://github.com/gargtanmay), Shoaib
