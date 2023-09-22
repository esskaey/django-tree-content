from django.contrib import admin
from .models import ContentModel, ExceptionContentModel
# Register your models here.
admin.site.register(ContentModel,ExceptionContentModel)