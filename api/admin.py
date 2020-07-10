from django.contrib import admin

from .models import FastaEntry,Sequence

admin.site.register(FastaEntry)
admin.site.register(Sequence)