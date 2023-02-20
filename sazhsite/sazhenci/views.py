from telnetlib import LOGOUT
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


from .forms import *
from .models import *
from .utils import *

class RasteniyaHome(DataMixin, ListView):
    paginate_by = 5
    model = Rasteniya
    template_name = 'sazhenci/sorta.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Rasteniya.objects.filter(is_published=True)


# def index(request):
#     posts = Rasteniya.objects.all()

#     context = {
#         'posts': posts,
#         'lef_selected': 0,
#     }

#     return render(request, 'sazhenci/sorta.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class RasteniyaLeft(DataMixin, ListView):
    model = Rasteniya
    template_name = 'sazhenci/sorta.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Rasteniya.objects.filter(lef__slug=self.kwargs['lef_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].lef)
        context['lef_selected'] = context['posts'][0].lef_id
        return context

# def show_left(request, lef_slug):
#     posts = Rasteniya.objects.filter(lef__slug=lef_slug)

#     context = {
#         'posts': posts,
#         'lef_selected': lef_slug, 
#     }

#     return render(request, 'sazhenci/sorta.html', context=context)

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'sazhenci/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return context

# @login_required       #<----------       #Оганичитель доступа
# def add(request):
#     if request.method == "POST":
#         form = AddForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
          
#     else:
#         form = AddForm()
#     return render(request, 'sazhenci/add.html', {'form': form, 'title': 'Добавление статьи'})

def kontakti(request):
    return render(request, 'sazhenci/kontakti.html')

def o_nas(request):
    return render(request, 'sazhenci/o_nas.html')


def show_post(request, post_slug):
    post = get_object_or_404(Rasteniya, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.lef_id,
    }

    return render(request, 'sazhenci/post.html', context=context)

# def login(request):
#     return HttpResponse("Авторизация")

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'sazhenci/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'sazhenci/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'sazhenci/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

