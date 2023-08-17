from django.shortcuts import redirect, render
from .models import introduction, contact, socialMedia
from .forms import ContactForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from files import correct_url
from django.shortcuts import get_object_or_404


def error_404(request, exception):    
    return render(request,'404.html')


def media_admin(request):
    return {"media_url":settings.MEDIA_URL,}


# ----------------------------------------------------------------------------------------
def index(request):
    
    return render(request, 'main_app/index.html')
# ----------------------------------------------------------------------------------------

def footer(request):
    try:
        social_media = socialMedia.objects.get(is_active=True)
    except socialMedia.DoesNotExist:
        social_media = None
    return render(request, 'partials/footer.html', {'social_media':social_media})
# ----------------------------------------------------------------------------------------

def introductionView(request):
    try:
        Intro = introduction.objects.get(is_active=True)
    except introduction.DoesNotExist:
        Intro = None
    return render(request, 'partials/introduction.html', {'Intro':Intro})
# ----------------------------------------------------------------------------------------

def main_img(request):    
    try:
        Intro = introduction.objects.get(is_active=True)
        edit_intro_img =correct_url(Intro.main_img)
    except introduction.DoesNotExist:
        Intro = None
        edit_intro_img = None
    
    return render(request, 'partials/main_img.html',{'Intro':Intro,  'edit_intro_img':edit_intro_img})
# ----------------------------------------------------------------------------------------
def nav(request):
    try:
        Intro = introduction.objects.get(is_active=True)
        edit_intro_logo =correct_url(Intro.logo)
    except introduction.DoesNotExist:
        Intro = None 
        edit_intro_logo = None
    
    return render(request, 'partials/nav.html',{'Intro':Intro, 'edit_intro_logo':edit_intro_logo})
# ----------------------------------------------------------------------------------------

def download_cv(request):
    fs = FileSystemStorage()
    Intro = get_object_or_404(introduction, is_active=True)
    file_name = str(Intro.cv)
    print(file_name)
    if fs.exists(file_name):
        with fs.open(file_name) as pdf:
            response = HttpResponse(pdf, content_type = "aplication/pdf")
            response['Content-Disposition'] = "attachmant; filename=Rashin_Latify_Full_Stack_Developer.pdf"
            return response
    else:
        return HttpResponseNotFound("File not found...")
    
# ----------------------------------------------------------------------------------------

def contact_form(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        
        cd = form.cleaned_data
        msg = contact()
        msg.first_name = cd['first_name']
        msg.last_name = cd['last_name']
        msg.subject = cd['subject']
        msg.message = cd['message']
        msg.email = cd['email']
        msg.save()
        # return redirect
    context={
        'form':form
    }
    return render(request, 'main_app/contact.html', context)
    

