from django.contrib.auth import logout
from django.http import HttpResponse
import random

from django.shortcuts import redirect


def generate_code(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.session.get('invalidate', False):
        logout(request)
        return redirect('login')

    request.session['invalidate'] = True

    code = random.randint(1000, 10000)
    return HttpResponse(code)
