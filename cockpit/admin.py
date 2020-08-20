from django.contrib import admin

from .models import ReferenceServiceAnalytic, PubType, SaglamaAnalytic, SaglamaReport
# Register your models here.
admin.site.register(ReferenceServiceAnalytic)
admin.site.register(PubType)
admin.site.register(SaglamaAnalytic)
admin.site.register(SaglamaReport)


