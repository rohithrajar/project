from django.shortcuts import render
from .models import Song
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    paginator = Paginator(Song.objects.all(),5)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except Exception:
        page_obj = paginator.get_page(1)
    context = {'page_obj': page_obj}
    return render(request,'main.html', context)

def home(request):
    return render(request,'index.html')
