from django.http.request import HttpRequest
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView
from .models import StudentInformation, Answers, Makequestion
from .forms import StudentInfo, QuestionsForms

def create_question(request):
    questionlist = Makequestion.objects.all()
    context = {
        'questionlist': questionlist,
    }
    return render(request, 'questions.html', context)


def home(request):
    qs = StudentInformation.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
            'qs': qs,
            'users':users
    }
    return render(request, 'studentinfo.html', context)

def question(request):
    # user_contacts = Questions.objects.all()
    user_contacts = Answers.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'qs':user_contacts,
    }
    return render(request, 'exam_result.html', context)

class QuestionView(LoginRequiredMixin, CreateView):
    template_name = 'questions.html'
    form_class = QuestionsForms
    success_url = '/question'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_id = self.request.user.id
        obj.save()
        return HttpResponseRedirect('/question')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(QuestionView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['examqs'] = Makequestion.objects.all()
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create-form.html'
    form_class = StudentInfo
    success_url = '/'



class StudentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StudentInfo
    login_url = '/login/'
    template_name = 'detail-update.html'
    success_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().first_name
        context['title'] = f'Update Restaurant: {name}'
        return context

    def get_queryset(self):
        return StudentInformation.objects.all()


@login_required
def delete(request, pk):
    student = StudentInformation.objects.get(id=pk)
    student.delete()
    messages.error(request, 'Student was deleted successfully!')

    return redirect('/')

class ProfileList(ListView):
    template_name = 'table.html'
    model = StudentInformation
    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     if query:
    #         object_list = self.model.objects.filter(name__icontains=query)
    #     else:
    #         object_list = self.model.objects.none()
    #     return object_list

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = StudentInformation.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
        print(object_list)
        return object_list




