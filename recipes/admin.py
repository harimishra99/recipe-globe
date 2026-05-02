from django.contrib import admin
from django.utils.html import format_html
from .models import (RegionalLanguage, Country, State, Cuisine,
                     Category, Recipe, RecipeTranslation,
                     Ingredient, RecipeStep, UserSavedRecipe, RecipeRating)


@admin.register(RegionalLanguage)
class RegionalLanguageAdmin(admin.ModelAdmin):
    list_display  = ['name', 'native_name', 'code', 'script', 'is_active']
    list_editable = ['is_active']
    search_fields = ['name', 'code']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display  = ['flag_emoji', 'name', 'code', 'default_language', 'is_active']
    list_editable = ['is_active']
    search_fields = ['name', 'code']


class StateLanguageInline(admin.TabularInline):
    model  = State.additional_languages.through
    extra  = 1
    verbose_name = 'Additional Language'


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display  = ['name', 'native_name', 'code', 'region', 'primary_language', 'country', 'is_active', 'order']
    list_editable = ['order', 'is_active']
    list_filter   = ['region', 'country', 'is_active']
    search_fields = ['name', 'code']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal   = ['additional_languages']
    fieldsets = (
        ('Basic Info',   {'fields': ('country', 'name', 'slug', 'native_name', 'code', 'capital', 'region')}),
        ('Language',     {'fields': ('primary_language', 'additional_languages')}),
        ('Content',      {'fields': ('description', 'cuisine_summary', 'banner_image_url')}),
        ('Settings',     {'fields': ('is_active', 'order')}),
    )


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display        = ['name', 'is_active']
    list_editable       = ['is_active']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal   = ['states']
    search_fields       = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['emoji', 'name', 'category_type', 'color_swatch', 'max_time_minutes', 'order']
    list_editable = ['order', 'category_type']
    list_filter   = ['category_type']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

    def color_swatch(self, obj):
        return format_html(
            '<span style="background:{};padding:3px 14px;border-radius:4px;color:#fff;font-size:11px">{}</span>',
            obj.color, obj.color)
    color_swatch.short_description = 'Color'


class IngredientInline(admin.TabularInline):
    model  = Ingredient
    extra  = 3
    fields = ['order', 'quantity', 'unit', 'name', 'notes']


class RecipeStepInline(admin.TabularInline):
    model  = RecipeStep
    extra  = 2
    fields = ['step_number', 'instruction', 'tip', 'time_minutes']


class TranslationInline(admin.TabularInline):
    model  = RecipeTranslation
    extra  = 1
    fields = ['language', 'title', 'description']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display  = ['thumb', 'title', 'state', 'cuisine', 'diet_type',
                     'difficulty', 'total_time_col', 'is_trending',
                     'is_featured', 'is_published', 'view_count']
    list_editable = ['is_trending', 'is_featured', 'is_published']
    list_filter   = ['state', 'cuisine', 'diet_type', 'difficulty',
                     'is_trending', 'is_featured', 'is_published', 'categories']
    search_fields = ['title', 'description', 'festival_tag']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal   = ['categories']
    autocomplete_fields = ['state', 'cuisine', 'country', 'author']
    readonly_fields     = ['view_count', 'created_at', 'updated_at', 'image_preview']
    inlines             = [IngredientInline, RecipeStepInline, TranslationInline]

    fieldsets = (
        ('Basic',       {'fields': ('title', 'slug', 'description', 'author')}),
        ('Geography',   {'fields': ('country', 'state', 'cuisine')}),
        ('Classification', {'fields': ('categories', 'diet_type', 'difficulty', 'festival_tag')}),
        ('Timing',      {'fields': ('prep_time', 'cook_time', 'servings', 'calories_per_serving')}),
        ('Media',       {'fields': ('image', 'image_preview', 'image_url')}),
        ('Status',      {'fields': ('is_published', 'is_trending', 'is_featured',
                                    'view_count', 'created_at', 'updated_at')}),
    )

    def thumb(self, obj):
        return format_html(
            '<img src="{}" style="width:52px;height:42px;object-fit:cover;border-radius:6px">',
            obj.image_display)
    thumb.short_description = ''

    def image_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-width:320px;border-radius:10px">',
            obj.image_display)
    image_preview.short_description = 'Preview'

    def total_time_col(self, obj):
        return f"{obj.total_time} min"
    total_time_col.short_description = 'Time'


@admin.register(RecipeRating)
class RecipeRatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe', 'rating', 'created_at']
    list_filter  = ['rating']

@admin.register(UserSavedRecipe)
class UserSavedAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe', 'saved_at']
