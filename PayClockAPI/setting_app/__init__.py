import os

from dotenv.main import load_dotenv

# Determine which .env file to load
ENV = os.getenv('DJANGO_ENV', 'development')

if ENV == 'production':
    env_file = '.env.prod'
else:
    env_file = '.env.dev'

# Load environment variables
load_dotenv(env_file)

# Import appropriate settings
if ENV == 'production':
    from .prod import *
else:
    from .dev import *
