from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'review', 'sentiment', 'resolved')
    list_filter = ('sentiment', 'resolved')
    search_fields = ('name', 'review')
