from django.db import models
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)


class CKEditorFlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CKEditorFlatPageAdmin)
