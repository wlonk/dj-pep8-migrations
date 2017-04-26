======================
Django PEP8 Migrations
======================

.. image:: https://badge.fury.io/py/dj-pep8-migrations.svg
    :target: https://badge.fury.io/py/dj-pep8-migrations

.. image:: https://travis-ci.org/wlonk/dj-pep8-migrations.svg?branch=master
    :target: https://travis-ci.org/wlonk/dj-pep8-migrations

.. image:: https://codecov.io/gh/wlonk/dj-pep8-migrations/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/wlonk/dj-pep8-migrations

Make your auto-generated migrations PEP8-compliant.

Documentation
-------------

The full documentation is at https://dj-pep8-migrations.readthedocs.io.

Quickstart
----------

Install Django PEP8 Migrations::

    pip install dj-pep8-migrations

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_pep8_migrations.apps.DjPep8MigrationsConfig',
        ...
    )

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
