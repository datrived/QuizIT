from django.contrib import admin

# Register your models here.
from articles.models import Articles

admin.site.register(Articles)