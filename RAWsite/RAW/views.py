from django.shortcuts import render
from .models import Song
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    song_list = Song.objects.all().order_by('title')
    paginator = Paginator(song_list, 10) # Show 6 songs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page({page_number})
    context={'page_obj':page_obj}
    return render(request,'main.html', context)

def home(request):
    return render(request,'index.html')
