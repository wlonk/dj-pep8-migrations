# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from dj_pep8_migrations.urls import urlpatterns as dj_pep8_migrations_urls

urlpatterns = [
    url(r'^', include(dj_pep8_migrations_urls, namespace='dj_pep8_migrations')),
]
