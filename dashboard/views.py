from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.decorators import client_required, active_user_required
# from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Smellsensor, Tissuesensor, Soapsensor, Company
import json
from .utils import send_html_mail


# Create your views here.

# user = get_user_model()


def calculate_percentage(level, empty, full):
    # full = 3
    x = float(level) - float(full)
    y = float(empty) - float(full)
    x_div_y = x / y
    percentage = (1 - x_div_y) * 100
    pretty_percentage = round(percentage, 2)

    return pretty_percentage


def smell_quality(level):
    if level > 1.00:
        return "Bad"
    else:
        return "Good"


@login_required(login_url='login')
@active_user_required
@client_required
def index(request):
    client_id = request.user.company
    user = request.user
    user_email = request.user.email

    obj = Tissuesensor.objects.filter(owner_id=client_id).last()
    obj_smell = Smellsensor.objects.filter(owner_id=client_id).last()
    obj_soap = Soapsensor.objects.filter(owner_id=client_id).last()
    percentage_tissue = calculate_percentage(obj.level_tissuesensor, obj.empty_reading, obj.initial_reading)
    quality_smell = smell_quality(float(obj_smell.level_smellsensor))
    percentage_soap = calculate_percentage(obj_soap.level_soapsensor, obj_soap.empty_reading, obj_soap.initial_reading)

    context = {

        "tissue_sensor": obj,
        "smell_sensor": obj_smell,
        "soap_sensor": obj_soap,
        "percentage_tissue": percentage_tissue,
        "quality_smell": quality_smell,
        "percentage_soap": percentage_soap
    }

    try:
        if percentage_tissue <= 30.00:

            subject = 'Alert your Tissues are about to finish'
            html_content = '<p>Sunway Toilet 1 tissue roll is finishing. Please refill</p>'
            sender = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user_email]
            send_html_mail(subject, html_content, recipient_list, sender)
            # send_mail(subject, html_content, sender, recipient_list, fail_silently=True)
    except:
        pass
    try:
        if percentage_soap <= 30.00:

            subject = 'Alert your Soap are about to finish'
            html_content = '<p>Sunway Toilet 1 Soap Holder is finishing. Please refill</p>'
            sender = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user_email]
            send_html_mail(subject, html_content, recipient_list, sender)
            # send_mail(subject, html_content, sender, recipient_list, fail_silently=True)
    except:
        pass

    return render(request, 'index.html', context)


@csrf_exempt
def read_data_tissue(request):
    response = request.body.decode("utf-8")
    json_dict = json.loads(response)
    print(type(json_dict))
    print(json_dict)

    sensor_id = json_dict['title']
    level = json_dict['level_tissuesensor']

    if float(level) < 3.00 or float(level) > 10.00:
        pass
    else:
        data = Tissuesensor(
            title=sensor_id,
            level_tissuesensor=level,
        )

        data.save()
        print("Successfully Saved TissueSensor Reading into the database")

    return HttpResponse("Received the POST request Successfully")
    # return HttpResponse(json_dict)


@csrf_exempt
def read_data_smell(request):
    response = request.body.decode("utf-8")
    json_dict = json.loads(response)
    print(type(json_dict))
    print(json_dict)

    sensor_id = json_dict['title']
    level = json_dict['level_smellsensor']

    data = Smellsensor(
        title=sensor_id,
        level_smellsensor=level,
    )

    data.save()
    print("Successfully Saved SmellSensor Reading into the database")

    return HttpResponse("Received the POST request Successfully")


@csrf_exempt
def read_data_soup(request):
    response = request.body.decode("utf-8")
    json_dict = json.loads(response)
    print(type(json_dict))
    print(json_dict)

    sensor_id = json_dict['title']
    level = json_dict['level_soapsensor']
    if float(level) < 1.00 or float(level) > 12.00:
        pass
    else:

        data = Soapsensor(
            title=sensor_id,
            level_soapsensor=level,
        )

        data.save()
        print("Successfully Saved SoapSensor Reading into the database")

    return HttpResponse("Received the POST request Successfully")


def show_data(request):
    tissue_sensor = Tissuesensor.objects.all()

    context = {
        "tissue_sensor": tissue_sensor,

    }

    return render(request, 'data.html', context)


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500(request):
    data = {}
    return render(request, '500.html', data)
