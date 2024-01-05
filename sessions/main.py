from inspira import Inspira
from inspira.config import Config
from inspira.middlewares.sessions import SessionMiddleware


config = Config()
config['SESSION_MAX_AGE'] = 3600
# default session configuration options
# config["SESSION_COOKIE_NAME"]
# config["SESSION_MAX_AGE"]
# config["SESSION_COOKIE_DOMAIN"]
# config["SESSION_COOKIE_PATH"]
# config["SESSION_COOKIE_HTTPONLY"]
# config["SESSION_COOKIE_SECURE"]
# config["SESSION_COOKIE_SAMESITE"]

app = Inspira(secret_key="UXkuLh6o9VuNz5d7KSnxYW_y4zau2H3u0UEZMhWKsFsecoGhel", config=config)

session = SessionMiddleware()
app.add_middleware(session)
