.. image:: https://travis-ci.org/TwigWorld/django-genesis.png
  :target: https://travis-ci.org/TwigWorld/django-genesis

.. image:: https://coveralls.io/repos/TwigWorld/django-genesis/badge.png?branch=master
   :target: https://coveralls.io/r/TwigWorld/django-genesis?branch=master

django-genesis
==============

Allows apps to define management commands that are called from a central management command.  Likely scenarios are post-deploy configurations (insert groups/permissions, compilemessages etc.)

.. image:: http://www.classicrockmagazine.com/wp-content/uploads/2009/10/genesis.jpg

Dependencies
------------

 - Django >= 1.4

Overview
--------

 - Management command to run other management commands
 - Allows apps to "hook" onto and be run from a central management command

Installation
------------

To install ``django-genesis`` simply run::

    pip install git+ssh://git@github.com/TwigWorld/django-genesis.git@1.0.0#egg=django-genesis==1.0.0

Configuration
-------------

We need to hook ``django-genesis`` into our project.

1. Put ``genesis`` into your ``INSTALLED_APPS`` at settings module::

      INSTALLED_APPS = (
         ...
         'genesis',
      )

Usage
-----

After installation we can finally use genesis.

Let's get started quickly. Running this line::

    python manage.py let_there_be_light

On an example django project with the below installed apps::

    app_1/
        management/
            commands/
                __init__.py
                app_1_bootstrap.py
                other_stuff.py
    app_2/
        management/
            commands/
                __init__.py
                app_2_bootstrap.py
                a_new_stuff.py
    app_3/
        management/
            commands/
                __init__.py
                another_new_stuff.py

Will cause the following management commands to be run::

    app_1_bootstrap.py
    app_2_bootstrap.py

All management commands to be run from ``let_there_be_light`` MUST be named {app_name}_bootstrap.py
