from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from siteroot.forms import EditUserForm

def index(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def edit_user(request):

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():

            request.user.save()
            return HttpResponseRedirect(reverse('edit_user_done') )

    else:
        form = EditUserForm(instance=request.user)

    context = {
        'form': form,
        'user': request.user,
    }

    return render(request, 'users/edit_user.html', context=context)

def edit_user_done(request):
    return render(request, 'users/edit_user_done.html')