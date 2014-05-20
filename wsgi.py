import os, sys, site, django.core.handlers.wsgi

SITE_DIR = '/home/vagrant/projects/scramble'
site.addsitedir(SITE_DIR)
sys.path.append(SITE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'scramble_project.settings'
application = django.core.handlers.wsgi.WSGIHandler()
