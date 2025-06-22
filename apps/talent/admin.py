from django.contrib import admin
from .models import Talent, TalentSocialLink

# Register your models here.
class TalentSocialLinkInline(admin.TabularInline):  # o admin.StackedInline si prefieres
    model = TalentSocialLink
    extra = 1  # cuántos formularios en blanco mostrar

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    inlines = [TalentSocialLinkInline]
    list_display = ('full_name', 'brand_name', 'is_verified', 'created_at')
    search_fields = ('full_name', 'brand_name')
    list_filter = ('is_verified',)


@admin.register(TalentSocialLink)
class TalentSocialLinkAdmin(admin.ModelAdmin):
    list_display = ('talent', 'platform', 'url')
    search_fields = ('talent__full_name', 'platform')