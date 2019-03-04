from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from . forms import ImageForm
from . models import Image



posts = [
    {
        'author': 'harshad',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'augest 27'

    },
    {
        'author': ' jane harshad',
        'title': 'blog post 2',
        'content': 'first222 post content',
        'date_posted': 'augest 27'

    }




]



def home(request):
    context = {
         'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')
def image_list(request):
    images= Image.objects.all()
    return render(request,'blog/image_list.html',{
        'images':images })


def upload_image(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('image_list')
    else:
         form =ImageForm()
    return render(request,'blog/upload_image.html',{
        'form':form
    })






