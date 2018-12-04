from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Match, Rating


class MatchAdmin(SummernoteModelAdmin):
    summernote_fields = 'body'


admin.site.register(Match, MatchAdmin)

admin.site.register(Rating)
# Register your models here.
