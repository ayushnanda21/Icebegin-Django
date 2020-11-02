from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable': "this is sent"
    }
    
    return render(request, 'index.html',context)         #to send back html file.
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')         #to send back html file.
   # return HttpResponse("this is aboutpage")

def services(request):
    return render(request, 'services.html')         #to send back html file.
   # return HttpResponse("this is servicespage")

def contact(request):
    #to add data to form contact to database made made we have writtem this few lines till next  #
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact= Contact(name= name, email =email, phone = phone , desc =desc, date= datetime.today())

        contact.save()
        messages.success(request, 'Your message has been sent!')


    return render(request, 'contact.html')         #to send back html file.
    #return HttpResponse("this is contactpage")