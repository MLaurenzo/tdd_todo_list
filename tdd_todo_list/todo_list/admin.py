from django.contrib import admin

from todo_list.models import Todo


class TodoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Todo, TodoAdmin)