from django.contrib import admin
from .models import CreateReviews, BookingModel

@admin.register(CreateReviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review', 'creation_date')
    search_fields = ['review']
    prepopulated_fields = {}
    list_filter = ('creation_date',)
    #summernote_fields = ('review')


@admin.register(BookingModel)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'heads', 'allergies')
    prepopulated_fields = {}
    list_filter = ('date', 'time',)

