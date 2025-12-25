from import_export import resources
from .models import Event, Participation, UserProfile
from django.contrib.auth.models import User
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class EventResource(resources.ModelResource):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date_start', 'date_end', 'location',
                  'organizer__username', 'max_participants', 'is_active', 'created_at', 'updated_at')
        export_order = fields


class ParticipationResource(resources.ModelResource):
    class Meta:
        model = Participation
        fields = ('id', 'user__username', 'event__title', 'status', 'comment', 'created_at', 'updated_at')
        export_order = fields


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')
        export_order = fields



@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource
    list_display = ('title', 'date_start', 'location', 'organizer', 'is_active')
    list_filter = ('is_active', 'date_start')
    search_fields = ('title', 'description')
    date_hierarchy = 'date_start'


@admin.register(Participation)
class ParticipationAdmin(ImportExportModelAdmin):
    resource_class = ParticipationResource
    list_display = ('user', 'event', 'status', 'created_at')
    list_filter = ('status', 'event')
    search_fields = ('user__username', 'event__title')
    date_hierarchy = 'created_at'


@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ('user', 'is_volunteer', 'city', 'phone')
    list_filter = ('is_volunteer',)
    search_fields = ('user__username', 'city')


# Расширяем стандартный UserAdmin для экспорта
class UserAdmin(BaseUserAdmin, ImportExportModelAdmin):
    # Можно добавить resource_class = UserResource, если нужно
    pass


# Регистрируем User с нашим расширенным админом
admin.site.unregister(User)
admin.site.register(User, UserAdmin)