from django.shortcuts import render

from django.http  import HttpResponse
from .models import Image

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        images = Image.search_by_category_name(search_term)
        message = f"{search_term}"

        return render(request, 'all_photos/search.html',{"message":message,"image":images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_photos/search.html',{"message":message})
def image(request):
        image = Image.objects.all()
        return render(request, 'all_photos/index.html',{"image":image})
def filter_by_location(request,location_id):
  image = Image.filter_by_location(id=location_id )
  return render (request,"all_photos/location.html", {"image":image})

