from django.shortcuts import redirect


def login_redirect(request):
    return redirect('iron2/login')
