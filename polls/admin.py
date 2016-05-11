from django.contrib import admin
# Register your models here.
from .models import Choice,Question


class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 3

class QuestionAdmin(admin.ModelAdmin):
        #fieldsets = [
        #               ( None, {'fields':['question_text']}),
        #                ('Date information',{'fields': ['pub_date'],'classes':['collapse']}),
        #                (None,{'fields':['question_answer']})
        #            ]
        #fields = ['pub_date', 'question_text','question_answer']
        #inlines = [ChoiceInline]
        list_display = ('question_text','pub_date','was_published_recently')

admin.site.register(Question, QuestionAdmin)
