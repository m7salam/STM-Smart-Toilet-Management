
from django.contrib.auth import authenticate, login, get_user_model, user_logged_in, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url


from .forms import LoginForm, RegisterForm
# Create your views here.
User = get_user_model()


class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # user_logged_in.send(user.__class__, instance=user, request=request)
            # try:
            #     del request.session['guest_email_id']
            # except:
            #     pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/accounts/login'

#
# def login_view(request):
#     form = UsersLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect("/")
#     return render(request, "login.html", {
#         "form": form,
#
#     })
#
#
# def register_view(request):
#     form = UsersRegisterForm(request.POST or None)
#     if form.is_valid():
#         user = form.save()
#         password = form.cleaned_data.get("password")
#         user.set_password(password)
#         user.save()
#         new_user = authenticate(username=user.username, password=password)
#         login(request, new_user)
#         return redirect("/accounts/login")
#     return render(request, "register.html", {
#         "form": form,
#     })
#
#


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
