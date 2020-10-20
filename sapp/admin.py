from django.contrib import admin

from .models import StudentInformation, Answers, Makequestion
# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_number', 'first_name', 'last_name', 'email', 'phone', 'father_name')
    list_per_page = 25

admin.site.register(StudentInformation, StudentsAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_1', 'question_2', 'question_3', 'question_4', 'question_5')

    list_per_page = 25

admin.site.register(Answers, QuestionAdmin)



class MakequestionAdmin(admin.ModelAdmin):
    list_display = ('question_title', 'mcq_1', 'mcq_2')

    list_per_page = 25

admin.site.register(Makequestion, MakequestionAdmin)




