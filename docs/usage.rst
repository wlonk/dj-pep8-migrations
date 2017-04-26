=====
Usage
=====

To use Django PEP8 Migrations in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_pep8_migrations.apps.DjPep8MigrationsConfig',
        ...
    )

Add Django PEP8 Migrations's URL patterns:

.. code-block:: python

    from dj_pep8_migrations import urls as dj_pep8_migrations_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_pep8_migrations_urls)),
        ...
    ]
