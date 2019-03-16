from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.utils.http import is_safe_url
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
# Create your views here.
# class based view
# from crispy_forms.helper import FormHelper
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['get_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)        
           
# class based view
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/Auth/login'
    

# def home_view(request):
#     title = "Dashboard"
#     context = {
#         "title": title
#     }
#     return render(request, "dashboard.html", context)  

# function based view
# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }    
#     next_ = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next_ or next_post or None
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             try:
#                 del request.session['get_email_id']
#             except:
#                 pass
#             if is_safe_url(redirect_path, request.get_host()):
#                 return redirect(redirect_path)
#             else:
#                 return redirect("/")
#         else:
#             print("Error")
#     return render(request, "accounts/login.html", context)     
# function based view
# User = get_user_model()
# def register_page(request):
#     form RegisterForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         form.save()
#     return render(request, "accounts/register.html", context)    
    
