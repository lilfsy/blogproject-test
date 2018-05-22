from django.contrib import admin
from .models import post,Category,Tag
class postAdmin(admin.ModelAdmin):
	list_display=['title','created_time','modified_time','category','author']
admin.site.register(post,postAdmin)
admin.site.register(Category)
admin.site.register(Tag)


# Register your models here.
