from os import environ as env

try:
    __import__('envs.py')
except ImportError:
    pass

IP = env.get('IP', '0.0.0.0')
PORT = env.get('PORT', 8080)
SERVER_NAME = env.get('SERVER_NAME', 'localhost:8080')
PREFERRED_URL_SCHEME = env.get('PREFERRED_URL_SCHEME', 'https')
POSTGRESQL_USER = env.get('POSTGRESQL_USER', '')
POSTGRESQL_PASSWORD = env.get('POSTGRESQL_PASSWORD')
POSTGRESQL_DATABASE = env.get('POSTGRESQL_DATABASE', 'usersDB')
POSTGRESQL_IP = env.get('POSTGRESQL_IP')
SQLALCHEMY_DATABASE_URI = env.get(
    'SQLALCHEMY_DATABASE_URI', "postgresql://" + str(POSTGRESQL_USER) + ":" + str(POSTGRESQL_PASSWORD) + "@" + str(POSTGRESQL_IP) + "/" + str(POSTGRESQL_DATABASE) + "")
SQLALCHEMY_TRACK_MODIFICATIONS = 'False'