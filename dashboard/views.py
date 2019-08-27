from django.core import serializers
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseServerError, HttpResponseRedirect
from accounts.decorators import client_required, active_user_required
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Smellsensor, Tissuesensor, Soupsensor, Company
import json
import requests
# Create your views here.

# user = get_user_model()


def calculate_percentage(level, empty):
    full = 3
    x = float(level) - full
    y = float(empty) - full
    x_div_y = x / y
    percentage = (1 - x_div_y) * 100
    pretty_percentage = round(percentage, 2)

    return pretty_percentage


@login_required(login_url='login')
@active_user_required
@client_required
def index(request):

    user = request.user.company
    user_email = request.user.email
    try:
        tissue_sensor = Tissuesensor.objects.filter(owner=user)
        smell_sensor = Smellsensor.objects.filter(owner=user)
        soup_sensor = Soupsensor.objects.filter(owner=user)
        obj =Tissuesensor.objects.get(owner_id=user)
        percentage_tissue = calculate_percentage(obj.level_tissuesensor, obj.empty_reading)
        context = {

            "tissue_sensor": tissue_sensor,
            "smell_sensor": smell_sensor,
            "soup_sensor": soup_sensor,
            "percentage_tissue": percentage_tissue
        }

        return render(request, 'index.html', context)
    except:
        pass

    # try:
    #     if percentage_tissue <= 30.00:
    #         subject = 'Alert your Tissues are about to finish'
    #         message = 'Sunway Toilet 1 tissue roll is finishing. Please refill'
    #         from_email = settings.EMAIL_HOST_USER
    #         to_list = [user_email]
    #         send_mail(subject, message, from_email, to_list, fail_silently=True)
    #     else:
    #         pass
    # except:
    #     pass


    return render(request, 'index.html', {})


@csrf_exempt
def read_data(request):

    response = request.body.decode("utf-8")
    json_dict = json.loads(response)
    print(type(json_dict))
    print(json_dict)

    sensor_id = json_dict['title']
    level = json_dict['level_tissuesensor']

    data = Tissuesensor(
        title= sensor_id,
        level_tissuesensor=level,
    )

    data.save()
    print("Successfully Saved TissueSensor Reading into the database")
    
    all_data = Tissuesensor.objects.all()
    all_data_json = serializers.serialize('json', all_data)

    # print(data)
    
    return HttpResponse(all_data.values(), content_type='application/json')
    # return HttpResponse(json_dict)




def show_data(request):
    tissue_sensor = Tissuesensor.objects.all()

    context = {
        "tissue_sensor":tissue_sensor,

    }

    return render(request, 'data.html', context)

    
def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500(request):
    data = {}
    return render(request, '500.html', data)


