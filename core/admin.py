from django.contrib import admin

from .models import Family, Member, Village, Attendance


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'family_name',
        'village',
        'house_number',
        'family_number',
        'contact_number',
        'area',
        'pin_code',
        'created_at',
    )

    search_fields = (
        'family_name',
        'village',
        'house_number',
        'family_number',
        'contact_number',
        'area',
        'pin_code',
    )


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'gender',
        'relation',
        'date_of_birth',
        'mobile_number',
        'alive_status',
        'family',
        'created_at',
    )

    search_fields = (
        'name',
        'mobile_number',
        'aadhaar_number',
        'family__family_name',
    )

    list_filter = (
        'gender',
        'relation',
        'alive_status',
        'bpl',
        'currently_pregnant',
    )


@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = ('id', 'village_number', 'name', 'total_houses')
    search_fields = ('village_number', 'name')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'status',
        'duty_type',
        'village',
        'check_in_time',
        'check_out_time',
        'home_visits_count',
        'patients_attended',
    )
    list_filter = ('status', 'duty_type', 'date')
    search_fields = ('tasks_completed', 'remarks')