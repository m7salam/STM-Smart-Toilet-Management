from django.shortcuts import render
from accounts.decorators import client_required, active_user_required
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import TissueSensor, SmellSensor, SoupSensor
# Create your views here.

# user = get_user_model()

@login_required(login_url='login')
@active_user_required
@client_required
def index(request):

    user = request.user
    tissue_sensor = TissueSensor.objects.filter(owner=user)
    smell_sensor = SmellSensor.objects.filter(owner=user)
    soup_sensor = SoupSensor.objects.filter(owner=user)

    context = {

        "tissue_sensor" : tissue_sensor,
        "smell_sensor"  : smell_sensor,
        "soup_sensor"   : soup_sensor,
    }
    try:
        if int(TissueSensor.level_tissuesensor) < int(TissueSensor.empty_reading) + 2:

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


def error_404(request, exception):
    data = {}
    return render(request, '404.html', data)


def error_500(request):
    data = {}
    return render(request, '500.html', data)
