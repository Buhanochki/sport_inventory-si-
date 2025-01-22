from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from core.apps.users.forms import UserLoginForm


class UserLoginView(TemplateView):
    form_class = UserLoginForm
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        if not request.user.is_anonymous:
            return redirect("main-page")
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        user_not_found = True
        if not request.user.is_anonymous:
            return redirect("main-page")
        elif form.is_valid():
            username = form.clean_username()
            password = form.clean_password()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("main-page")
        form.fields["password"].widget.attrs.update({"class": "form-control is-invalid"})
        user_not_found = form.errors.get("__all__") is not None
        return render(
            request, self.template_name, context={"form": form, "user_not_found": user_not_found}
        )


class AdminDashboard(TemplateView):
    template_name = "users/admin_main_page.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            redirect("login")
        elif request.user.status == "PT":
            return redirect("user-dashboard")
        return super().get(request, *args, **kwargs)


class UserDashboard(TemplateView):
    template_name = "users/user_main_page.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            redirect("login")
        elif request.user.status == "TC":
            return redirect("admin-dashboard")
        return super().get(request, *args, **kwargs)


def main_page(request):
    if request.user.is_anonymous:
        return redirect("login")
    elif request.user.status == "PT":
        return redirect("user-dashboard")
    return redirect("admin-dashboard")


def logout_user(request):
    logout(request)
    return redirect("login")
