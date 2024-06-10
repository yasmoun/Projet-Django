from django.contrib import admin
from .models import Patient,Avis
# Register your models here.
from embed_video.admin import AdminVideoMixin
from .models import Video

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)
admin.site.register(Patient)
admin.site.register(Avis)