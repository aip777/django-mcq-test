from django import forms
from .models import StudentInformation, Answers

class StudentInfo(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = (
            'id_number', 'department', 'first_name','last_name', 'email','phone','father_name','mother_name', 'guidancephone', 'cgpa'
        )

class QuestionsForms(forms.ModelForm):
    class Meta:
        model = Answers
        fields = (
            'question_1', 'question_2','question_3','question_4','question_5'
        )

