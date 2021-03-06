from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import sense_hat_tools

@login_required
def index(request):

    context = {
        'sense_hat_data': sense_hat_tools.get_sense_hat_data(),
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'sensehat/index.html', context=context)
