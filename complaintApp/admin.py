from django.contrib import admin
from django.urls import reverse
from .models import Complaint,FeedbackUser, Profile
from django.utils.html import format_html

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'category', 'created_at')
    list_filter = ( 'status', 'category')
    search_fields = ('title', 'description')
    actions = ['mark_as_in_progress', 'mark_as_resolved']

    def complaint_count(self, obj):
        return Complaint.objects.filter(subject=obj.subject).count()
    complaint_count.short_description = 'Number of Similar Complaints'

    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='in_progress')
    mark_as_in_progress.short_description = "Mark selected complaints as In Progress"

    def mark_as_resolved(self, request, queryset):
        queryset.update(status='resolved')
    mark_as_resolved.short_description = "Mark selected complaints as Resolved"

    def view_on_site(self, obj):
        return format_html('<a href="{}">View Statistics</a>', reverse('complaint_stats'))

admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(FeedbackUser)
admin.site.register(Profile)
