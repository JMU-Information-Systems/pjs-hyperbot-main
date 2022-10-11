#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
# For more information about this file, visit
# https://docs.djangoproject.com/en/2.1/ref/django-admin/
"""

import os
import sys
from db_operations import databaseContact

    
if __name__ == '__main__':
    #xaml = open("test","w", encoding="utf-8")
    #writehead(xaml)

    db = databaseContact()
    #type = db.getType()

    #myxaml = xaml()
    #myxaml.replaceVariables(variables)

    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'pjshyperbot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)