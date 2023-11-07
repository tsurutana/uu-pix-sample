from django.shortcuts import render, redirect
from django.http import Http404
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import pix.threshold as th

# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        file = request.FILES["imagefile"]
        fs = FileSystemStorage(location=str(settings.MEDIA_ROOT))
        file_path = fs.save(file.name, file)
        file_url = fs.url(file_path)
        context['image'] = file_url
        context['converted'] = th.getThresholdImage(file_url)
        request.session['image'] = context['image']
        request.session['converted'] = context['converted']
        return render(request, 'pix/create.html', context)
    return render(request, 'pix/index.html', context)

def create(request):
    return redirect(index)
