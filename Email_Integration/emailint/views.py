from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
def registrationForm(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            fname = form.cleaned_data['first_name']
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            form.save()
            subject = 'Registration Successfull!'
            message = f'name:-{fname}\n username:-{uname}\n password:-{pwd}'

            send_mail(subject,
                      message,
                      'sudhakanaje1997@gmail.com',
                      [email],
                      fail_silently=False,

                      )
            return redirect('success')

    context = {'form': form}
    template_name = 'signup.html'
    return render(request, template_name, context)


def registrationSuccess(request):
    template_name = 'registerSuccess.html'
    return render(request, template_name)