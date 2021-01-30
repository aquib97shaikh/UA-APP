from django.contrib import admin

# Register your models here.
from .models import User,UserLoginHistory
import csv
from django.http import HttpResponse
admin.site.register(User)

# admin.site.register(UserLoginHistory)

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

@admin.register(UserLoginHistory)
class UserLoginHistoryAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("user","loginAt")
    actions = ["export_as_csv"]


