from django.contrib import admin
from myblog.models import visitor,viewpoint,visitorhistory,author

# Register your models here.
admin.site.register(author)
admin.site.register(visitorhistory)
admin.site.register(visitor)
admin.site.register(viewpoint)
