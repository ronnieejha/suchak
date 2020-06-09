# Suchak 

Suchak is an app to give you location based news. It currenlty use Event Rigistry News Api in the backend.
<br>

This website is developed using Django and a bit of bootstrap in frontend.

I have deployed it on heroku. Check it out [Suchak](https://suchak.herokuapp.com/)
#### Development Planned:
1. Integrating twitter live feed
2. Integrating more news apis
3. Incorporating Vuejs in frontend.

### Instructions for setup

Install pipenv `pip install pipenv -U`

Install dependencies using pipenv `pipenv install`


### Running development server

Run `python3 manage.py runserver`

#### Environment variables

You need EVENT_REGISTRY_KEY in env variable to able to run this app properly.
You can obtain the key by signing up at [Event Registry](http://eventregistry.org/) 
 