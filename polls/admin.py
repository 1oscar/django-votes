from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #        (None,               {'fields': ['question_text']}),
    #        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    #    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchies = ['pub_date']
    Change_list_pagination = ['choice_text']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

