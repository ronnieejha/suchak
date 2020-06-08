import os
ENV = os.environ.get('ENV', 'dev')

if ENV == 'dev':
  from suchak.settings.dev import *
elif ENV == 'prod':
  from suchak.settings.prod import *
else:
  raise ValueError('Invalid config ' + ENV)