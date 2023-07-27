from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import student
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User


# Create your views here.
def landingPage(request):
    return render(request, 'home.html')


def sendData(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        student.objects.create(id=id, f_name=f_name,
                               l_name=l_name, email=email)
        messages.success(request, "Your message has been successfully sent")
    return render(request, 'home.html')


def getData(request):
    data = student.objects.all()
    return render(request, 'getData.html', {'data': data})


def delete(request):
    id = request.GET['id']

    student.objects.get(id=id).delete()
    # return HttpResponse("delete")
    return HttpResponseRedirect("getData")


def edit(request):
    id = request.GET.get('id')
    data = student.objects.get(id=id)
    return render(request, 'edit.html', {'data': data})


def updateData(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')

        student.objects.filter(id=id).update(
            f_name=f_name, l_name=l_name, email=email)
        messages.success(request, "Your message has been successfully sent")

    return HttpResponseRedirect("getData")
# Authentication system


def signUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('fname')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.first_name = firstname
        user.save()
        return redirect('login')  # Correct redirection using 'redirect'

    return render(request, 'signUp.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            firstName = user.first_name
            return render(request, "home.html", {'firstName': firstName})
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
