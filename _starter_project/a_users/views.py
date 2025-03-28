from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import ProfileForm

def profile_view(request):
    profile = request.user.profile
    return render(request=request, template_name='a_users/profile.html', context={'profile': profile})


def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('a_users:profile')
    return render(request=request, template_name='a_users/profile_edit.html', context={'form': form})