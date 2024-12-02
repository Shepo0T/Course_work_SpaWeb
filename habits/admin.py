from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'owner', 'location', 'act', 'when_to_perform']
