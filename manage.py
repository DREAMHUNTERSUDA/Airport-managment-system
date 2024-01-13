#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airport.settings')
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Error importing Django. Make sure it's installed and available on your PYTHONPATH. "
            "Did you forget to activate a virtual environment?\nOriginal error: {}".format(exc)
        )

    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print("Error executing command: {}".format(e))
