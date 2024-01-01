from inspira import Inspira
from inspira.middlewares.sessions import SessionMiddleware

app = Inspira()
app.secret_key = "UXkuLh6o9VuNz5d7KSnxYW_y4zau2H3u0UEZMhWKsFsecoGhel"

# Update the max age for sessions
app.config['SESSION_MAX_AGE'] = 3600

# default session configuration options
# app.config["SESSION_COOKIE_NAME"]
# app.config["SESSION_MAX_AGE"]
# app.config["SESSION_COOKIE_DOMAIN"]
# app.config["SESSION_COOKIE_PATH"]
# app.config["SESSION_COOKIE_HTTPONLY"]
# app.config["SESSION_COOKIE_SECURE"]
# app.config["SESSION_COOKIE_SAMESITE"]

session = SessionMiddleware(app.secret_key)
app.add_middleware(session)
