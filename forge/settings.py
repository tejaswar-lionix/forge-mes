
import os; from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev')
DEBUG=os.environ.get('DEBUG','1')=='1'
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','channels','apps.orders','apps.bom','apps.workcenters','apps.machines','apps.shifts','apps.production','apps.quality','apps.maintenance','apps.inventory','apps.procurement','apps.dispatch','apps.workers','apps.analytics','apps.downtime','apps.traceability','apps.andon']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware']
ROOT_URLCONF='forge.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True}]
WSGI_APPLICATION='forge.wsgi.application'
ASGI_APPLICATION='forge.asgi.application'
DATABASES={'default':{'ENGINE':os.environ.get('DB_ENGINE','django.db.backends.postgresql'),'NAME':os.environ.get('DB_NAME','forge')}}
if os.environ.get('USE_SQLITE','1')=='1': DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
CHANNEL_LAYERS={'default':{'BACKEND':'channels.layers.InMemoryChannelLayer'}}



import os; from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev')
DEBUG=os.environ.get('DEBUG','1')=='1'
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','channels','apps.orders','apps.bom','apps.workcenters','apps.machines','apps.shifts','apps.production','apps.quality','apps.maintenance','apps.inventory','apps.procurement','apps.dispatch','apps.workers','apps.analytics','apps.downtime','apps.traceability','apps.andon']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware']
ROOT_URLCONF='forge.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True}]
WSGI_APPLICATION='forge.wsgi.application'
ASGI_APPLICATION='forge.asgi.application'
DATABASES={'default':{'ENGINE':os.environ.get('DB_ENGINE','django.db.backends.postgresql'),'NAME':os.environ.get('DB_NAME','forge')}}
if os.environ.get('USE_SQLITE','1')=='1': DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
CHANNEL_LAYERS={'default':{'BACKEND':'channels.layers.InMemoryChannelLayer'}}



import os; from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev')
DEBUG=os.environ.get('DEBUG','1')=='1'
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','channels','apps.orders','apps.bom','apps.workcenters','apps.machines','apps.shifts','apps.production','apps.quality','apps.maintenance','apps.inventory','apps.procurement','apps.dispatch','apps.workers','apps.analytics','apps.downtime','apps.traceability','apps.andon']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware']
ROOT_URLCONF='forge.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True}]
WSGI_APPLICATION='forge.wsgi.application'
ASGI_APPLICATION='forge.asgi.application'
DATABASES={'default':{'ENGINE':os.environ.get('DB_ENGINE','django.db.backends.postgresql'),'NAME':os.environ.get('DB_NAME','forge')}}
if os.environ.get('USE_SQLITE','1')=='1': DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
CHANNEL_LAYERS={'default':{'BACKEND':'channels.layers.InMemoryChannelLayer'}}



import os; from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev')
DEBUG=os.environ.get('DEBUG','1')=='1'
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','channels','apps.orders','apps.bom','apps.workcenters','apps.machines','apps.shifts','apps.production','apps.quality','apps.maintenance','apps.inventory','apps.procurement','apps.dispatch','apps.workers','apps.analytics','apps.downtime','apps.traceability','apps.andon']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware']
ROOT_URLCONF='forge.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True}]
WSGI_APPLICATION='forge.wsgi.application'
ASGI_APPLICATION='forge.asgi.application'
DATABASES={'default':{'ENGINE':os.environ.get('DB_ENGINE','django.db.backends.postgresql'),'NAME':os.environ.get('DB_NAME','forge')}}
if os.environ.get('USE_SQLITE','1')=='1': DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
CHANNEL_LAYERS={'default':{'BACKEND':'channels.layers.InMemoryChannelLayer'}}



import os; from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev')
DEBUG=os.environ.get('DEBUG','1')=='1'
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','channels','apps.orders','apps.bom','apps.workcenters','apps.machines','apps.shifts','apps.production','apps.quality','apps.maintenance','apps.inventory','apps.procurement','apps.dispatch','apps.workers','apps.analytics','apps.downtime','apps.traceability','apps.andon']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware']
ROOT_URLCONF='forge.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True}]
WSGI_APPLICATION='forge.wsgi.application'
ASGI_APPLICATION='forge.asgi.application'
DATABASES={'default':{'ENGINE':os.environ.get('DB_ENGINE','django.db.backends.postgresql'),'NAME':os.environ.get('DB_NAME','forge')}}
if os.environ.get('USE_SQLITE','1')=='1': DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
CHANNEL_LAYERS={'default':{'BACKEND':'channels.layers.InMemoryChannelLayer'}}



import os; from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev')
DEBUG=os.environ.get('DEBUG','1')=='1'
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','channels','apps.orders','apps.bom','apps.workcenters','apps.machines','apps.shifts','apps.production','apps.quality','apps.maintenance','apps.inventory','apps.procurement','apps.dispatch','apps.workers','apps.analytics','apps.downtime','apps.traceability','apps.andon']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware']
ROOT_URLCONF='forge.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True}]
WSGI_APPLICATION='forge.wsgi.application'
ASGI_APPLICATION='forge.asgi.application'
DATABASES={'default':{'ENGINE':os.environ.get('DB_ENGINE','django.db.backends.postgresql'),'NAME':os.environ.get('DB_NAME','forge')}}
if os.environ.get('USE_SQLITE','1')=='1': DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
CHANNEL_LAYERS={'default':{'BACKEND':'channels.layers.InMemoryChannelLayer'}}



import os; from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev')
DEBUG=os.environ.get('DEBUG','1')=='1'
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','channels','apps.orders','apps.bom','apps.workcenters','apps.machines','apps.shifts','apps.production','apps.quality','apps.maintenance','apps.inventory','apps.procurement','apps.dispatch','apps.workers','apps.analytics','apps.downtime','apps.traceability','apps.andon']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware']
ROOT_URLCONF='forge.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True}]
WSGI_APPLICATION='forge.wsgi.application'
ASGI_APPLICATION='forge.asgi.application'
DATABASES={'default':{'ENGINE':os.environ.get('DB_ENGINE','django.db.backends.postgresql'),'NAME':os.environ.get('DB_NAME','forge')}}
if os.environ.get('USE_SQLITE','1')=='1': DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
CHANNEL_LAYERS={'default':{'BACKEND':'channels.layers.InMemoryChannelLayer'}}



import os; from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev')
DEBUG=os.environ.get('DEBUG','1')=='1'
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','channels','apps.orders','apps.bom','apps.workcenters','apps.machines','apps.shifts','apps.production','apps.quality','apps.maintenance','apps.inventory','apps.procurement','apps.dispatch','apps.workers','apps.analytics','apps.downtime','apps.traceability','apps.andon']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware']
ROOT_URLCONF='forge.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True}]
WSGI_APPLICATION='forge.wsgi.application'
ASGI_APPLICATION='forge.asgi.application'
DATABASES={'default':{'ENGINE':os.environ.get('DB_ENGINE','django.db.backends.postgresql'),'NAME':os.environ.get('DB_NAME','forge')}}
if os.environ.get('USE_SQLITE','1')=='1': DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
CHANNEL_LAYERS={'default':{'BACKEND':'channels.layers.InMemoryChannelLayer'}}
