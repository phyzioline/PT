from django.contrib import admin
from .models import JobPost, JobApplication

# لعرض طلبات التقديم في صفحة الوظيفة (ATS Tracking)
class JobApplicationInline(admin.TabularInline):
    model = JobApplication
    extra = 0  # عدم عرض حقول فارغة إضافية
    fields = ('applicant', 'status', 'applied_at')
    readonly_fields = ('applicant', 'applied_at', 'cover_letter')
    can_delete = False

# تحكم في عرض نموذج الوظيفة
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'is_full_time', 'posted_at')
    list_filter = ('is_full_time', 'posted_at', 'location')
    search_fields = ('title', 'description', 'company__user__username')
    inlines = [JobApplicationInline]

# تحكم في عرض نموذج طلبات التقديم
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('job__title', 'applicant__user__username')
    # السماح بتعديل الحالة فقط
    readonly_fields = ('job', 'applicant', 'applied_at', 'cover_letter')
    list_editable = ('status',)

admin.site.register(JobPost, JobPostAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
