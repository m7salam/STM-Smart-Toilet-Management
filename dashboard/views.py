from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseServerError
from accounts.decorators import client_required, active_user_required
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Smellsensor, Tissuesensor, Soupsensor
import json
import requests
# Create your views here.

# user = get_user_model()

@login_required(login_url='login')
@active_user_required
@client_required
def index(request):

    user = request.user
    tissue_sensor = Tissuesensor.objects.filter(owner=user)
    smell_sensor = Smellsensor.objects.filter(owner=user)
    soup_sensor = Soupsensor.objects.filter(owner=user)

    context = {

        "tissue_sensor" : tissue_sensor,
        "smell_sensor"  : smell_sensor,
        "soup_sensor"   : soup_sensor,
    }
    try:
        if int(Tissuesensor.level_tissuesensor) < int(Tissuesensor.empty_reading) + 2:

                    subject = 'Alert your Tissues are about to finish'
                    message = 'Sunway Toilet 1 tissue roll is finishing. Please refill'
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [user.email]
                    send_mail(subject, message, from_email, to_list, fail_silently=True)
        else:
            pass
    except:
        pass


    return render(request, 'index.html', context)

@csrf_exempt
def read_data(request):
    data = request.POST
    data_transform = (json.loads(json.dumps(request.POST)))
    return HttpResponse(data_transform)



def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500(request):
    data = {}
    return render(request, '500.html', data)


