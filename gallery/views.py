from django.shortcuts import render

from django.http  import HttpResponse
from .models import Image

# Create your views here.
# def welcome(request):
#     return render(request, 'all_photos/index.html')
def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categorys = Category.search_by_category_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"categorys": searched_categorys})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_photos/search.html',{"message":message})
def image(request):
        image = Image.objects.all()
        return render(request, 'all_photos/index.html',{"image":image})