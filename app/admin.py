from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Match, Rating, Match2, Rating2, Rules

admin.site.site_header = 'Event Maker administration'


class MatchAdmin(SummernoteModelAdmin):
    summernote_fields = 'body'
    list_filter = ['active']


admin.site.register(Match, MatchAdmin)


class Match2Admin(SummernoteModelAdmin):
    summernote_fields = 'body'
    list_filter = ['active']


admin.site.register(Match2, Match2Admin)


class RuleAdmin(SummernoteModelAdmin):
    summernote_fields = 'body'



admin.site.register(Rules, RuleAdmin)



@admin.register(Rating)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['user', 'score_1','score_2']



@admin.register(Rating2)
class CreditAdmin(admin.ModelAdmin):
    list_display = ['user', 'score_1']



# Register your models here.
