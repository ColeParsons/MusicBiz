#!/usr/bin/env python
import os
import sys
from django.db import models
from django.contrib import admin
from django.contrib import staticfiles

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
