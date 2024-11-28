from django.contrib import admin

# Register your models here.
from news.models import Company, News


admin.site.register([Company,News])